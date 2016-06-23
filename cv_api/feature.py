import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.jpg',0)

cor = cv2.goodFeaturesToTrack(img,True,.150,100)
cor = np.int0(cor)

for i in cor:
	x,y = i.ravel()
	cv2.circle(img,(x,y),3,255,-1)
        print i

plt.imshow(img)
plt.show()
