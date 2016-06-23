import numpy as np
import cv2

im = cv2.imread('images/BrickYard.JPG',0)
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#im = cv2.Canny(im, 30,150)
#im = cv2.blur(im,(10,10))
ret,thresh = cv2.threshold(im,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[4]
img = cv2.drawContours(im, [cnt], -1, (0,255,0), 3)
m=cv2.moments(cnt)
print m
#epsilon = 0.1*cv2.arcLength(cnt,True)
#approx = cv2.approxPolyDP(cnt,epsilon,True)

#cx = int(m['m10']/m['m01'])
#cy = int(m['m01']/m['m01'])
#print cx,cy
#img = cv2.drawContours(im, contours, -1, (0,255,255), 3)
m,n=im.shape
count=np.array(img)
co = 0
print m,n
for i in range(m):
	for j in range(n):
	#	for k in range(n):
			a=im[i][j],
                        if (a != 0)and(a<=255):  
				co+=count+a
				#print count
				j=j+1
			else:
				continue#j=j+1
#for r in 
		

#cv2.imshow('qwedqw',con)
cv2.imshow("title", im)
cv2.waitKey()
