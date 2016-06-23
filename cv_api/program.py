import numpy as np
import cv2
image = cv2.imread('images/index4.jpeg',0)
ret,thresh = cv2.threshold(image,127,255,0)

cont1, hie1 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cont2,hie2 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 

img1 = image.copy()
img2 = image.copy()


cv2.drawContours(img1, cont1, -1, (255,0,0), 3)
cv2.drawContours(img2, cont2, -1, (255,0,0), 3)

out = np.hstack([img1, img2])

# Now show the image
cv2.imshow('Output', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
