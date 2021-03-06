import numpy as np
import cv2

image = cv2.imread('images/brick.jpeg',0)

#imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#canny = cv2.Canny(image, 30,150)
ret,thresh = cv2.threshold(image,127,255,0)
c,h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, c, -1, (0,255,0), 3)
cnt = c[4]

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
hull = cv2.convexHull(cnt)

#hull = cv2.convexHull(cnt,returnPoints = False)
#defects = cv2.convexityDefects(cnt,hull)

#for i in range(defects.shape[0]):
 #   s,e,f,d = defects[i,0]
  #  start = tuple(cnt[s][0])
  #  end = tuple(cnt[e][0])
  #  far = tuple(cnt[f][0])
  #  cv2.line(img,start,end,[0,255,0],2)
  #  cv2.circle(image,far,5,[0,0,255],-1)

#m = cv2.moments(image)
area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt,True)

cv2.imshow('ferger',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print 'area'
print   area
print 'approx'
print   approx
print 'peri'
print   perimeter
