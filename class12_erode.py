import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('dige.png')
cv2.imshow('img',img)
cv2.waitKey(0)

kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)

cv2.imshow('erosion',erosion)
cv2.waitKey(0)

dilate=cv2.dilate(erosion,kernel,iterations=1)

cv2.imshow('dilate',dilate)
cv2.waitKey(0)



