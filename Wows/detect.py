import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(img):
	cv2.imshow('img',img)
	cv2.waitKey()
	cv2.destroyAllWindows()

def find_ship_bound(img):
		#cv_show(img)
		kernel=np.ones((1,3),np.uint8)
		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,3)
		cv2.imshow('thresh',thresh)
		thresh_close=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=2)
		cv2.imshow('closed',thresh_close)
		
		contours, hierarchy = cv2.findContours(thresh_close,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
		detected=0
		
		for i in range(len(contours)):
			epsl=0.01*cv2.arcLength(contours[i],True)
			approx=cv2.approxPolyDP(contours[i],epsl,True)
			if detected==1:
				break
			if (cv2.arcLength(approx,True)>250) & (cv2.arcLength(approx,True)<900):
				#print(i,end="  ")
				#print(cv2.arcLength(contours[i],True))
				print(cv2.arcLength(approx,True))
				x,y,w,h=cv2.boundingRect(contours[i])
				if (w/h) >3:
					draw_img=img.copy()
					res = cv2.drawContours(draw_img,[approx],-1,(0,255,0),2)
					res2=cv2.rectangle(res,(x,y),(x+w,y+h),(255,0,0),1)
					cv2.imshow('detect',res2)
					detected=1
		if detected==0:
			cv2.imshow('detect',img)
				


bb=cv2.VideoCapture('img/bb.mp4')
if bb.isOpened():
	open,frame=bb.read()
else:
	open=False

while open:
	ret,frame=bb.read()
	if frame is None:
		break
	if ret is True:
		find_ship_bound(frame)
		if cv2.waitKey(200) & 0xFF == 27:
			break

bb.release()
cv2.destroyAllWindows()



