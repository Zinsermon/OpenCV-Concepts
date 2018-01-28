import cv2
import numpy as np

import pyscreenshot as pp


image =  cv2.imread(np.array(pp.grab(bbox=(0,0,300,300))))
gray  =  cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

cv2.imshow('image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()
