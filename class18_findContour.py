import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(img):
	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

img=cv2.imread('img/contours2.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

cv_show(thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#origin contours
draw_img=img.copy()
res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
cv_show(res)

# approximated shape
epsilon=0.07*cv2.arcLength(contours[0],True)
approx=cv2.approxPolyDP(contours[0],epsilon,True)
draw_img2=img.copy()
res = cv2.drawContours(draw_img2,[approx],-1,(0,0,255),2)
cv_show(res)

#rectangular contour
x,y,w,h=cv2.boundingRect(contours[0])
draw_img3=img.copy()
rect_img=cv2.rectangle(draw_img3,(x,y),(x+w,y+h),(0,255,0),2)
cv_show(rect_img)



print(cv2.contourArea(contours[0]),cv2.contourArea(contours[1]))





