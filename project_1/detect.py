import cv2
import numpy as np

def cv_show(img):
	cv2.imshow('img',img)
	cv2.waitKey()
	cv2.destroyAllWindows()

def detect_H(img):
	kernel=np.ones((3,3),np.uint8)
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,10)
	thresh_open=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)
	thresh_close=cv2.morphologyEx(thresh_open,cv2.MORPH_CLOSE,kernel,iterations=1)
	cv2.imshow('thresh_close',thresh_close)
	contour, hierarchy=cv2.findContours(thresh_close,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	res_img=img.copy()
	cv2.imshow('res',res_img)
	area=[]

	for i in range(len(contour)):
		epsl=0.002*cv2.arcLength(contour[i],True)
		approx=(cv2.approxPolyDP(contour[i],epsl,True))
		area.append(cv2.contourArea(contour[i]))
	max_index=area.index(max(area))
	res=cv2.drawContours(res_img,contour[max_index],-1,(0,255,0),2)
	if cv2.contourArea(contour[max_index])>20000:
		center,radius=cv2.minEnclosingCircle(contour[max_index])
		center = np.int0(center)
		cv2.circle(res_img, tuple(center), int(radius), (0, 0, 255), 2)
		cv2.imshow('res',res_img)





field=cv2.VideoCapture('field.mp4')
if field.isOpened():
	Open,frame=field.read()
else:
	Open=False

while Open:
	ret, frame=field.read()
	if frame is None:
		break
	if ret is True:
		detect_H(frame)
		if cv2.waitKey(1) & 0xFF==27:
			break

field.release()
cv2.destroyAllWindows()
