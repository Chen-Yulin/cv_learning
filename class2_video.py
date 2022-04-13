import cv2
import numpy as np
mad = cv2.VideoCapture('mad.mp4')

if mad.isOpened():
	open, frame = mad.read()
else:
	open = False

while open:
	ret, frame = mad.read()
	if frame is None:
		break
	if ret is True:
		sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=3)
		sobelx=cv2.convertScaleAbs(sobelx)
		sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=3)
		sobely=cv2.convertScaleAbs(sobely)
		sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
		cv2.imshow('sobel',sobelxy)
		if cv2.waitKey(50) & 0xFF == 27:  #will keep step forward untill ESC is pressed
			break
mad.release()
cv2.destroyAllWindows()
