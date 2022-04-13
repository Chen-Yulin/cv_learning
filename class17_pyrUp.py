import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(img):
	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



img=cv2.imread('img/AM.png')
cv_show(img)
up=cv2.pyrUp(img)
cv_show(up)

down=cv2.pyrDown(img)
cv_show(down)

#Laplace pyr

down_up=cv2.pyrUp(down)
l_1=img-down_up
cv_show(l_1)





