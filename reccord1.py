#!python3

import cv2 as cv 

vcap = cv.VideoCapture("rtsp://192.168.1.2:8080/out.h264")
while(1):
    ret, frame = vcap.read()
    cv.imshow('VIDEO', frame)
    cv.waitKey(1)