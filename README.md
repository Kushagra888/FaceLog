# 🧠 FaceLog – Face Detection Attendance System

**FaceLog** is a Python-based real-time face detection system that automates attendance tracking using a webcam. It detects faces in real-time and logs the detection time to a CSV file.

## 📸 Features

- Real-time face detection via webcam
- Modern web interface using Flask and Bootstrap
- Automatic attendance logging with timestamps
- CSV-based attendance records (one file per day)
- Visual feedback with bounding boxes
- Simple setup with minimal dependencies

## 🛠️ Technologies Used

- Python 3.10+
- Flask 2.3.2
- OpenCV (cv2) with Haar Cascade Classifier
- Bootstrap 5.3.0

## 🚀 Setup & Installation

1. Clone this repository:
```bash
git clone https://github.com/Kushagra888/FaceLog.git
cd FaceLog
```

2. Install the required dependencies:
```bash
pip install opencv-python flask
```

## 💻 Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. The system will automatically:
   - Detect faces in the webcam feed
   - Draw boxes around detected faces
   - Log detections in a daily CSV file

## 📝 Attendance Logs

- Attendance is logged in CSV files named with the current date (YYYY-MM-DD.csv)
- Each entry includes:
  - Time of detection (HH-MM-SS)
  - Detection status

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

