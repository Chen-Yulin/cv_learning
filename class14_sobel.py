import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(img):
	cv2.imshow('img',img)
	cv2.waitKey()
	cv2.destroyAllWindows()

img=cv2.imread('img/pie.png')
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
cv_show(sobelx)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely=cv2.convertScaleAbs(sobely)
cv_show(sobely)


sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
cv_show(sobelxy)
