import cv2
import numpy as np
def gamma(img, c, v):
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    output_img = cv2.LUT(img, lut)
    output_img = np.array(output_img,np.uint8)  # 这句一定要加上
    return output_img

def custom_blur_demo(image):
  kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #锐化
  dst = cv2.filter2D(image, -1, kernel=kernel)
  return dst

