import cv2
import numpy as np
l=40
b=20
size = l*b

img = cv2.imread('index5.jpeg')
#blur = cv2.blur(img,(5,4))
#image = cv2.GaussianBlur(img, (5,5),0)
#thr = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
           # cv2.THRESH_BINARY,11,2)

canny = cv2.Canny(img,size,100,200)
#length = len(canny)
count = 0
for i in range(len(canny)):

	count=canny[i]+1	
	print count

#kernel = np.ones((5,5),np.uint8)
#dilate = cv2.dilate(canny,kernel)

#black = makeColor(0,0,0)
#white = makeColor(255,255,255)
#numblacks = numbers = 0
#for pixel in getPixels(img):
#	color = getColor(pixel)
#	if color == black: numblacks +=1
#	elif color ==white: numbers +=1





cv2.imshow('imgage',count)


cv2.waitKey(0)
cv2.destroyAllWindows()

