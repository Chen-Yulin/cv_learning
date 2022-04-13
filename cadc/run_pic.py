import cv2
import detect
import preProcess

img=cv2.imread('./img2.png')
rect_list,ROI=detect.detect_target(img)
cv2.waitKey(0)
detect.get_numberShot(img,rect_list,ROI)
cv2.waitKey(0)
img=cv2.imread('./img.png')
rect_list,ROI=detect.detect_target(img)
cv2.waitKey(0)
detect.get_numberShot(img,rect_list,ROI)
cv2.waitKey(0)
