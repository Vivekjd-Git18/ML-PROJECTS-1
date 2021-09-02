import cv2
import gray as gray

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.default.xml')
cap = cv2.VideoCapture(0)

"""while True:
    img = cap.read()
    cap = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h),(2555, 0, 0), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()"""

from functools import reduce

fib = lambda N