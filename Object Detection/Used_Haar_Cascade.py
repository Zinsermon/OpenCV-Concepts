import cv2
import numpy as np

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
smile = cv2.CascadeClassifier('haarcascade_smile.xml')
#cap = cv2.VideoCapture(0)

#while(True):
#    _,frame = cap.read()
frame =cv2.imread('me.JPG')
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

face_points = face.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in face_points:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    roi = frame[y:y+h , x:x+w]
    roi_gray = gray[y:y+h , x:x+w]

    eye_points = eye.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eye_points:
        cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


    smile_points = smile.detectMultiScale(roi_gray)
    for (sx,sy,sw,sh) in smile_points:
        cv2.rectangle(roi,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

cv2.imshow('Frame',frame)

k = cv2.waitKey(0) #& 0xff
   # if k == 27:
   #     break

cv2.destroyAllWindows()
#cap.release()
