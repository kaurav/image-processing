mport cv2
import numpy as np
img = cv2.imread('brick.jpeg',0)

sift = cv2.SIFT()
kp = sift.detect(img,None)

kp,des = sift.compute(img,kp)

#img = cv2.drawKeypoints(img, kp) 

cv2.imshow('dfewfewf',kp)
cv2.waitKey(0)
cv2.destroyAllWindows()
