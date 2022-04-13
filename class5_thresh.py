import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('mj.png',cv2.IMREAD_UNCHANGED)
print(img.shape)
img_grey=cv2.imread('mj.png',cv2.IMREAD_GRAYSCALE)
ret,thresh1 = cv2.threshold(img_grey,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img_grey,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img_grey,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img_grey,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img_grey,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','THRESH_TOZERO_INV']

images=[img_grey,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)

