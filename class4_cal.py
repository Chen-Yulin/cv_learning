import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('mj.png',cv2.IMREAD_UNCHANGED)
img_add=img+40

cv2.imshow('img_add',img_add)
cv2.waitKey(500)
img_add2=cv2.add(img,40)
cv2.imshow('img_add2',img_add2)
cv2.waitKey(500)


