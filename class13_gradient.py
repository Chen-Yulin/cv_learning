import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('dige.png')
kernel=np.ones((5,5),np.uint8)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

cv2.imshow('gradient',gradient)
cv2.waitKey(0)

top=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow('top',top)
cv2.waitKey(0)

black=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel,2)
cv2.imshow('black',black)
cv2.waitKey(0)

