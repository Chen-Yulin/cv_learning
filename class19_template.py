import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(img):
	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

lena=cv2.imread('img/lena.jpg',0)
cv_show(lena)
lena_t=cv2.imread('img/lena_temp.jpg',0)
cv_show(lena_t)
res=cv2.matchTemplate(lena,lena_t,cv2.TM_CCOEFF_NORMED)
print(lena_t.shape)
h,w=lena_t.shape[:2]
cv_show(res)
print(res,res.shape)


methods=['cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF_NORMED']

for meth in methods:
	lena2=lena.copy()

	#匹配方法的真值
	method=eval(meth)
	print(method)
	res=cv2.matchTemplate(lena,lena_t,method)
	min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
	if method in [cv2.TM_SQDIFF_NORMED]:
		topleft=min_loc
	else:
		topleft=max_loc
	bottomright=(topleft[0]+w,topleft[1]+h)
	
	#draw rectangle
	cv2.rectangle(lena2,topleft,bottomright,255,2)
	
	plt.subplot(121),plt.imshow(res,cmap='gray')
	plt.subplot(122),plt.imshow(lena2,cmap='gray')
	plt.show()






