import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('lenaNoise.png',cv2.IMREAD_UNCHANGED)
print(img.shape)

blur=cv2.blur(img,(3,3))

box=cv2.boxFilter(img,-1,(3,3),normalize=False)

Gauss=cv2.GaussianBlur(img,(5,5),1)

median=cv2.medianBlur(img,3)

res = np.hstack((blur,Gauss,median))
cv2.imshow('all blur',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


