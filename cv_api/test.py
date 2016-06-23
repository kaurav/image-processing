import cv2
import numpy as np

img = cv2.imread('images/brick-wallpaper-4.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
#cv2.drawContours(img, contours, -1, (0,255,0), 3)
cnt = contours[4]
img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
#cnt = contours[0]
#M = cv2.moments(cnt)
#print M

#epsilon = 0.1*cv2.arcLength(cnt,True)
#approx = cv2.approxPolyDP(cnt,epsilon,True)
#print approx
cv2.imshow('asdasd',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
