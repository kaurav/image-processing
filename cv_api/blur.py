import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('images/bhagat.jpg')

blur = cv2.blur(image,(21,21))


plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')

plt.show()
