import cv2
import numpy as np


image = cv2.imread('Capture01.PNG')
img  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1.5)

cv2.imshow('image01',image)
cv2.imshow('thresh',th)

cv2.waitKey(0)
cv2.destroyAllWindows()
