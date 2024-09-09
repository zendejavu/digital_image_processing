#memilih warna biru saja pada gambar gambar 
import cv2 # menyertakan library cv2 dari opencv
import numpy as np


img = cv2.imread("circles.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lowBlue = np.array([100, 10, 10])
highBlue = np.array([140, 255, 255])

mask = cv2.inRange (img, lowBlue, highBlue)

cv2.imshow("display", mask)
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


