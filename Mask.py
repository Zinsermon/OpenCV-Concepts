import cv2
import numpy as np

img1= cv2.imread('Data Science 02.PNG' )
img2= cv2.imread('Capture.JPG' )

rows, col ,channels = img2.shape
roi=  img1[0:rows,0:col]

#print(rows,col,channels)
#cv2.imshow('roi',roi)


img2GrayScale = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2GrayScale,220,225,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
img1_back = cv2.add(roi,roi,mask=mask_inv)
img2_front  = cv2.add(img2,img2,mask=mask)

dst = img2_front+img1_back

img1[0:rows,0:col] = dst


cv2.imshow('so',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
