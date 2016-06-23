from Tkinter import *
import cv2
import numpy as np
import argparse

win = Tk()
f = Frame(win)
b1 = Button(f)



def blur():
	image = cv2.blur(image,(5,5))
	return image

b1.configure(command=blur)

ap=argparse.ArgumentParser()
ap.add_argument('-i')
args = vars(ap.parse_args())
image = cv2.imread(args['i'])
cv2.imshow('image',image)
cv2.waitKey(0)

b1.pack(side=LEFT)
l = Label(win,"This label is over all buttons")
l.pack()
f.pack()

	

