import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('mj.jpg',cv2.IMREAD_UNCHANGED)
print(img.shape)
img_grey=cv2.imread('mj.jpg',cv2.IMREAD_GRAYSCALE)
img_cut=img[200:500,200:500]
print(img_grey)
cv2.imwrite('mj_grey.jpg',img_grey)
#cv2.imshow('mj_grey',img_grey)
#cv2.waitKey(1000)
#cv2.imshow('mj',img)
#cv2.waitKey(0)
#cv2.imshow('img_cut',img_cut)
#cv2.waitKey(0)
img_b,img_g,img_r = cv2.split(img)
img_cur=img.copy()
img_cur[:,:,2]=0
img_cur[:,:,1]=0
cv2.imshow('img_cur',img_cur)
cv2.waitKey(0)



