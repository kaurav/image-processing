import cv2
import numpy as np
import matplotlib.pyplot as plt
m = cv2.imread('images/foto.jpg',0)
ret,thresh1 = cv2.threshold(m,127,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(m,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(m,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(m,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [m, thresh1, thresh3, thresh4, thresh5]

for i in xrange(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
