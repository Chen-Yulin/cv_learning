import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('mj.png',cv2.IMREAD_UNCHANGED)
reflect101=cv2.copyMakeBorder(img,150,150,150,150,cv2.BORDER_REFLECT101)
cv2.imshow('rf101',reflect101)
cv2.waitKey(0)







