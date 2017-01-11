# -*- coding: utf-8 -*

import gpioset
from flask import Flask, render_template , Response, send_from_directory

# emulated camera
from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera
        
app=Flask(__name__,static_folder = "file")

#連結到樹梅派的時候會打開網頁
@app.route('/')
def index():
	return render_template('index.html')
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#產生Jpeg檔案        
def capture(camera):
        capture = open('file/capture.jpeg','wb')
        capture.write(camera.get_frame())
        capture.close()
        frame = camera.get_frame()
        return (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#將截圖結果傳送到網頁端顯示
@app.route('/capture_feed')
def capture_feed():
        return Response(capture(Camera()),
                        mimetype='multipart/x-mixed-replace;boundary=frame')

#引導網頁端到截圖檔案位置
@app.route('/get_image')
def get_image():
    return send_from_directory(directory='file',filename='capture.jpeg',
                               mimetype='image/jpeg')

#前進
@app.route('/forward')
def forward():
	gpioset.MotorController('F')

@app.route("/left")
#左轉
def left():
	gpioset.MotorController('L')

#停止
@app.route("/stop")
def stop():
	gpioset.MotorController('S')

#右轉
@app.route("/right")
def right():
	gpioset.MotorController('R')

#後退
@app.route("/back")
def back():
	gpioset.MotorController('B')

#threaded設定為True啟動Multi-Thread
if __name__ == '__main__':
	app.run(host='0.0.0.0', threaded=True)
