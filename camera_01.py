#coding:utf-8

import picamera
import time

with picamera.PiCamera() as camera:
#     filename = raw_input('File Name?> ')
    filename = input('File Name?> ')
#     res = int(raw_input('Resolution(1:320x240, 2:640x480, 3:1024x768)'))
    res = int(input('Resolution(1:320x240, 2:640x480, 3:1024x768)'))
    
    if res == 3:
        camera.resolution = (1024, 768)
    elif res == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)

    camera.start_preview()
    time.sleep(1)
    camera.stop_preview()
#     camera.capture(filename + '.jpg')
    camera.capture('testshot.jpg')
