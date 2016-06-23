from visual import *
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('brick.jpeg')
tex = materials.texture(data = image, interpolate = false)
a = box(axis = (0,0,1), material=image)
plt.imshow('dssdfsd',a)
plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindow()

