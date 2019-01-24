import cv2
import numpy as np

img = cv2.imread("Norway.Png", cv2.IMREAD_GRAYSCALE)
print(img.shape)

print(img[0, 0])
print(img[0, 250])
print(img[0, 499])

_, threshold_binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

cv2.imshow("Image", img)
cv2.imshow("th binary", threshold_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()

           
