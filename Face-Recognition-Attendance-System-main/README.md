Yeh raha aapke project ke liye `README.md` file:

```markdown
# 🎓 QUEST University - AI Face Recognition Attendance System

## 📋 Project Overview
An intelligent attendance management system using **Face Recognition Technology** for QUEST University, Nawabshah. This system automates the attendance marking process using facial recognition, providing both manual and automated options for teachers.

## 👨‍💻 Developer
**Sikandar Ali**  
Roll No: 23BSCS44  
Computer Science Department  
QUEST University, Nawabshah

## ✨ Features

### 🔐 Multi-Teacher System
- 5 different teachers with separate logins
- Each teacher manages their own subject
- Teachers can only see their subject's attendance

### 📚 Subjects Available
1. **Artificial Intelligence** (ai_teacher)
2. **Compiler Construction** (cc_teacher)
3. **Computer Networks** (cn_teacher)
4. **Numerical Analysis** (numerical_teacher)
5. **Technical Writing** (english_teacher)

### 🕐 Time Periods
- 8:00 - 9:00
- 9:00 - 10:00
- 10:00 - 11:00
- 11:00 - 12:00
- 12:00 - 13:00
- 14:00 - 15:00

### 🎯 Key Features
- ✅ **Face Recognition Auto-Attendance** - Automatic marking when face detected
- ✅ **Manual Attendance** - Mark attendance manually with one click
- ✅ **Real-time Camera Feed** - Live face detection with visual feedback
- ✅ **Subject-wise Reports** - Export attendance to Excel
- ✅ **Student Management** - Register/Delete students with face photos
- ✅ **Dashboard Statistics** - View attendance statistics in real-time
- ✅ **Period-wise Attendance** - Separate attendance for each period

## 🚀 Installation Guide

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package manager)
Webcam (for face recognition)
```

### Step 1: Install Required Libraries
```bash
pip install flask flask-login flask-sqlalchemy werkzeug opencv-python face-recognition numpy openpyxl
```

### Step 2: Download face_recognition dependencies (Windows)
```bash
# For Windows, you might need:
pip install cmake
pip install dlib
pip install face-recognition
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access the System
Open browser and go to: `http://localhost:5000`

## 🔑 Login Credentials

| Subject | Username | Password |
|---------|----------|----------|
| Artificial Intelligence | ai_teacher | teacher123 |
| Compiler Construction | cc_teacher | teacher123 |
| Computer Networks | cn_teacher | teacher123 |
| Numerical Analysis | numerical_teacher | teacher123 |
| Technical Writing | english_teacher | teacher123 |

## 📱 How to Use

### 1. First Time Setup
1. Login with any teacher credentials
2. Go to **Students** page
3. Register students with their clear face photos
4. Add roll number, name, and semester

### 2. Taking Attendance (Manual)
1. Go to **Manual Attendance**
2. Select the period
3. Click on student cards to mark Present/Absent
4. Click **Save Attendance**

### 3. Taking Attendance (Auto Face Recognition)
1. Go to **Camera Attendance**
2. Select the period
3. Click **Start Camera**
4. Students look at the camera
5. **Yellow Box** = Face detected
6. **Green Box with ✓** = Attendance marked automatically
7. Attendance saved automatically in database

### 4. View Reports
1. Go to **Reports** page
2. Click **Download Excel** to export attendance data

## 🗂️ Project Structure
```
QUEST-Attendance-System/
│
├── app.py                 # Main application file
├── quest_attendance.db    # SQLite database
├── students_images/       # Folder for student photos
│   ├── 23BSCS44.jpg
│   └── ...
├── static/               # Static files (logo, etc.)
└── README.md             # Project documentation
```

## 🗄️ Database Schema

### User Table
- id, username, password, role, full_name, subject, teacher_id

### Student Table
- id, roll_no, name, email, semester, section, photo_path

### Attendance Table
- id, roll_no, student_name, date, time, period, subject, status, marked_by

## 🎨 Color Coding in Camera Feed
- 🟢 **Green Box** - Face recognized & attendance marked
- 🟡 **Yellow Box** - Face detected (marking in progress)
- 🔴 **Red Box** - Unknown face

## 📊 Features in Detail

### Dashboard
- Total students count
- Present/Absent count for today
- Attendance percentage
- Today's attendance list

### Student Management
- Register new students with photos
- Delete existing students
- Auto-load faces for recognition

### Reports
- Export attendance to Excel
- Subject-wise data filtering
- Date-wise records

## ⚠️ Troubleshooting

### Camera not working?
- Check if webcam is connected
- Allow browser permission for camera
- Try different USB port

### Face not recognized?
- Take clear front-facing photo
- Ensure good lighting
- Student should look directly at camera

### Attendance not saving?
- Check if period is selected
- Verify student is registered
- Check database connection

## 🔧 Technical Stack
- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy
- **Face Recognition**: face_recognition library
- **Camera**: OpenCV (cv2)
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Flask-Login
- **Reports**: openpyxl (Excel export)

## 📈 Future Enhancements
- [ ] Email notifications to parents
- [ ] Mobile app integration
- [ ] Cloud backup of attendance data
- [ ] Multiple face detection in one frame
- [ ] Anti-spoofing detection
- [ ] Voice announcements

## 🙏 Acknowledgments
- QUEST University, Nawabshah
- Computer Science Department
- Project Supervisor

## 📞 Contact
**Sikandar Ali**  
Roll No: 23BSCS44  
Email: sikandar@quest.edu.pk  

---
**© 2024 QUEST University - AI Attendance System**  
*Made with ❤️ by Sikandar Ali (23BSCS44)*
```


