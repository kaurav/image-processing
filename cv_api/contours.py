import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('12004098_927290344010344_4926236181970543565_n.png',0)

ret, thresh = cv2.threshold(image,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0,255,0), 3)
print image
#cnt = contours[4]
#image = cv2.drawContours(image, [cnt], 0, (0,255,0), 3)


cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

