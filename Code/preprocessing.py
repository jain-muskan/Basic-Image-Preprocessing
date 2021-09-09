import cv2
import numpy as np
img = cv2.imread('files/i3.jpg',0)
scale_percent = 80 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
dst = cv2.fastNlMeansDenoising(img, None, 8, 7, 21) 
img = cv2.addWeighted(dst, 1.4, np.zeros(img.shape, img.dtype), 0, 0)
ret,thresh11 = cv2.threshold(img,190,255,cv2.THRESH_BINARY)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,2)
cv2.imwrite("files/dem.jpg", th3)
 