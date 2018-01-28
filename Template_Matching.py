import cv2
import numpy as np
import pyscreenshot as pp

#image = cv2.imread('Page.JPG')
##  --------- OR --------
image = cv2.imread(np.array(pp.grab(bbox=(0,0,300,300))))
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#template = cv2.imread('Capture0.JPG',0)
##  --------- OR --------
template = cv2.imread(np.array(pp.grab(bbox=(0,0,300,300))),0)

w ,h = template.shape[::-1]
res= cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.85
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0]+w, pt[1]+h), (255,0,0), 2)

cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
