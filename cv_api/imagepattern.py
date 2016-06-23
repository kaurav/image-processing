import cv2
import numpy as np
import argparse

m matplotlib import pyplot as plt
image1 = cv2.imread('cat.jpg')

#ap=argparse.ArgumentParser()
#ap.add_argument('-i','--i', required = True)
#args = vars(ap.parse_args())
#image = cv2.imread(args['i'])








cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
