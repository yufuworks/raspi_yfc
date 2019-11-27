from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    output_image = image.copy()
    detector = cv.QRCodeDetecor()
    data, points, straight_qrcode = detector.detectAndDecode(image)
    
    if data:
        print(f'decoded data: {data}')
        for i in range(4):
            cv.line(output_image, tuple(points[i][0]), tuple(points[(i + 1) % len(points)][0]), (0, 0, 255), 4)
        cv.imshow('QR', output_image)
        print(f'QR code version: {((straight_qrcode.shape[0] - 21) / 4) + 1}')
    
    cv.imshow("Frame", image)
    key = cv.waitKey(1) & 0xFF
    rawCapture.trancate(0)
    
    if key == ord("q"):
        break