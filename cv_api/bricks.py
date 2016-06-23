import cv2
import numpy as np
img = cv2.imread('images/foto.jpeg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

edge = cv2.Canny(thresh1,200,200)
for num in edge:
	cv2.imshow('dsfds',edge)

	cv2.waitKey(0)
	cv2.destroyAllWindow()


