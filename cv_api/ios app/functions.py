import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--i", required = True)
args = vars(ap.parse_args())
im = cv2.imread(args["i"])
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
