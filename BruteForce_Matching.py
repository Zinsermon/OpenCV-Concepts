import cv2
import numpy as np
import matplotlib.pyplot as plt

image1= cv2.imread('image.jpg',0)
image2 = cv2.imread('template.jpg',0)

orb_detector = cv2.ORB_create()

keypoints_1, descriptor_1  = orb_detector.detectAndCompute(image1,None)
keypoints_2, descriptor_2  = orb_detector.detectAndCompute(image2,None)

bfMatcher =cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bfMatcher.match(descriptor_2,descriptor_1)
matches = sorted(matches, key = lambda x:x.distance)

img  = cv2.drawMatches(image2,keypoints_2,image1,keypoints_1,matches[:15],None,flags = 2)
plt.imshow(img)
plt.show()
