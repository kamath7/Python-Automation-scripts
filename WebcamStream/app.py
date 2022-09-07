import cv2
from flask import Flask, render_template, Response

video = cv2.VideoCapture(0)

def get_frame():
    success, frame = video.read()
    sc, encoded_image = cv2.imencode('.jpg', frame)
    frame = encoded_image.tobytes()
    yield(b'--frame\r\nContent-Type: image/jpeg\r\n'+frame+b'\r\n')


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

