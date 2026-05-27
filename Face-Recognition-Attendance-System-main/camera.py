cat > camera.py << 'EOF'
import cv2
import face_recognition
import numpy as np
from database import Student, Attendance, db
from datetime import datetime
import os

known_encodings = []
known_names = []
known_rolls = []
camera_instance = None

def load_faces():
    global known_encodings, known_names, known_rolls
    known_encodings = []
    known_names = []
    known_rolls = []
    students = Student.query.all()
    for student in students:
        if student.photo_path and os.path.exists(student.photo_path):
            try:
                img = face_recognition.load_image_file(student.photo_path)
                enc = face_recognition.face_encodings(img)
                if enc:
                    known_encodings.append(enc[0])
                    known_names.append(student.name)
                    known_rolls.append(student.roll_no)
            except:
                pass
    print(f'Loaded {len(known_names)} faces')

def mark_attendance_face(roll, name, period, subject, teacher):
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")
    
    existing = Attendance.query.filter_by(
        roll_no=roll, date=today, period=period
    ).first()
    
    if existing:
        return False
    
    attendance = Attendance(
        roll_no=roll,
        student_name=name,
        date=today,
        time=now,
        period=period,
        subject=subject,
        status="Present",
        department=teacher.department,
        marked_by=teacher.username
    )
    db.session.add(attendance)
    db.session.commit()
    return True

def get_camera():
    global camera_instance
    if camera_instance is None or not camera_instance.isOpened():
        for i in range(3):
            try:
                camera_instance = cv2.VideoCapture(i, cv2.CAP_DSHOW)
                if camera_instance.isOpened():
                    print(f'Camera {i} opened')
                    return camera_instance
            except:
                continue
        camera_instance = None
        return None
    return camera_instance

def release_camera():
    global camera_instance
    if camera_instance is not None:
        camera_instance.release()
        camera_instance = None

def generate_frames(period, subject, current_user):
    global camera_instance
    
    release_camera()
    camera = get_camera()
    
    if camera is None:
        while True:
            frame = np.zeros((480, 640, 3), dtype=np.uint8)
            cv2.putText(frame, "CAMERA NOT FOUND", (200, 240), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            ret, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        return
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        
        if len(known_encodings) > 0:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                name = "Unknown"
                roll = "N/A"
                
                if True in matches:
                    match_index = matches.index(True)
                    name = known_names[match_index]
                    roll = known_rolls[match_index]
                    
                    if current_user.is_authenticated:
                        mark_attendance_face(roll, name, period, subject, current_user)
                
                for (top, right, bottom, left) in face_locations:
                    top, right, bottom, left = top*4, right*4, bottom*4, left*4
                    color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                    cv2.putText(frame, f"{name}", (left, top-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
EOF