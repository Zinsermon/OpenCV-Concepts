import numpy as np
import cv2

cap = cv2.VideoCapture(0)
foreground = cv2.createBackgroundSubtractorMOG2()

while(True):
    _,frame = cap.read()
    maskMOG = foreground.apply(frame)

    cv2.imshow('Video',frame)
    cv2.imshow('MOG',maskMOG)
    kernel_02 = np.ones((5,5),np.uint8)
#    guessBlur = cv2.GaussianBlur(maskMOG,(15,15),0)
#    medBlur = cv2.medianBlur(maskMOG,15)
#    cv2.imshow('medBlur',medBlur)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
