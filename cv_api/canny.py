import numpy as np
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-avi')#,required = True, help = 'fdgadgvdf')
args = vars(ap.parse_args())

image = cv2.imread(args['avi'])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#st = cv2.StereoBM_create(numDisparities = 16, blockSize=15)
#image = st.computer(image)

#image = cv2.GaussianBlur(image, (5,5),0)
#image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
 #         cv2.THRESH_BINARY,11,2) 
cv2.imshow('image',image)

#canny = cv2.Canny(image, 30,150)
#cv2.imshow('canny',canny)
cv2.waitKey(0)
