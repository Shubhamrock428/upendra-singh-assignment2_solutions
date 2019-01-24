import cv2

image = cv2.imread("Norway.png")

cv2.imshow("Norway", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
