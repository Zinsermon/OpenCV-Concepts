import cv2
import numpy as np

cap  = cv2.VideoCapture(0)

while (1):
    _, frame  = cap.read()
    hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    upper_bound =  np.array([10,5,5])
    lower_bound =  np.array([200,90,90])

    mask = cv2.inRange(hsv, upper_bound,lower_bound)
    res  = cv2.bitwise_and(frame, frame, mask=mask)

    kernel =  np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(res,-1,kernel)

    guessBlur = cv2.GaussianBlur(res,(15,15),0)
    medBlur = cv2.medianBlur(res,15)
    bilaterBlur = cv2.bilateralFilter(res,15,75,75)

    ## Morphological Transformation
    kernel_02 = np.ones((5,5),np.uint8)
    errosion = cv2.erode(res,kernel_02,iterations=1)
    dilation = cv2.dilate(res, kernel_02,iterations=1)

    opening = cv2.morphologyEx(res,cv2.MORPH_OPEN,kernel_02)
    closing = cv2.morphologyEx(res,cv2.MORPH_CLOSE,kernel_02)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
