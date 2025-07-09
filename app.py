import csv
from flask import Flask, render_template, Response
import cv2
import numpy as np
from datetime import datetime
import os

app = Flask(__name__)
camera = cv2.VideoCapture(0)

# Load the pre-trained face detection cascade classifier
cascade_path = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            # Draw rectangle around faces and log attendance
            for (x, y, w, h) in faces:
                # Draw rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # Add "Person Detected" label
                cv2.putText(frame, 'Person Detected', (x, y-10), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                # Log attendance
                now = datetime.now()
                current_date = now.strftime("%Y-%m-%d")
                current_time = now.strftime("%H-%M-%S")
                
                # Create attendance log
                with open(current_date + '.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    if os.path.getsize(current_date + '.csv') == 0:
                        writer.writerow(['Time', 'Status'])
                    writer.writerow([current_time, 'Person Detected'])

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
