import cv2
import numpy as np
	

cap  = cv2.VideoCapture(0)
fourcc =  cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter('game.avi',fourcc,20.0,(640,480))

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret== True:
        recorder.write(frame)
        cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
