import cv2
import numpy as np
import argparse
choose = ['upload','camera']
print choose
choose = raw_input("enter your choice from above: ")
for i in choose:
	if choose == 'upload':
		print 'browse a file'
		ap=argparse.ArgumentParser()
		ap.add_argument('-i')
		args = vars(ap.parse_args())
		image = cv2.imread(args['-i'])
		cv2.imshow('image',image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	if choose == 'camera':
		print 'take your position'
		cap = cv2.VideoCapture(100)
		ret,frame = cap.read()
		cv2.imshow('dsfvds',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			#cv2.imshow('image',image)
			#cv2.waitKey(0)
			cv2.destroyAllWindow()
