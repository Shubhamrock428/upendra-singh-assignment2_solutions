import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Norway.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("img", img)

plt.hist(img.ravel(), 256, [0, 256])
plt.show()
