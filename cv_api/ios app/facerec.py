import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#faces = face_cascade.detectMultiScale(image, 1.3, 5)
image = cv2.imread('bha.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5,flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
print "found {0} faces!" .format(len(faces))

for (x,y,w,h) in faces:
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
   #roi_gray = gray[y:y+h, x:x+w]
   #roi_color = image[y:y+h, x:x+w]

    cv2.imshow('image',image)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
