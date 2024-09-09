#blobs untuk mencari countur biru (centroid, luas keliling ukuran dan komparasu)

import cv2 # menyertakan library cv2 dari opencv
import numpy as np


image = cv2.imread("circles.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lowBlue = np.array([30, 10, 10])
highBlue = np.array([40, 255, 255])

lowRed = np.array([0, 10, 10])
highRed = np.array([10, 255, 255])

mask = cv2.inRange (img, lowBlue, highBlue)
mask2 = cv2.inRange (img, lowRed, highRed)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    #RETR_EXTERNAL = ambil kontur terbesar, jka di dlm kontur ada contur
contours2, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print (len(contours))#jumlah countur
print (len(contours2))#jumlah countur

print(cv2.contourArea(contours[0])) #Luas
print(cv2.contourArea(contours2[0]))

M = cv2.moments(contours[0])

cx=int(M['m10']/M['m00'])#koordinat x
cy=int(M['m01']/M['m00'])#coordinat y
print("Centroid: ({}, {})".format(cx,cy))

M = cv2.moments(contours2[0]) # menghitung moment (pusat masa)
cx2=int(M['m10']/M['m00'])#koordinat x
cy2=int(M['m01']/M['m00'])#coordinat y
print("Centroid: ({}, {})".format(cx2,cy2))

imgx = cv2.drawContours(image, contours, -1, (0,255,0), 3) #memunculkan countour
cv2.circle(imgx, (cx2, cy2), 5,(0,125,0), -1) #memunculkan centroid pada gambar

imgx = cv2.drawContours(image, contours2, -1, (255,255,0), 2) #memunculkan countour
cv2.circle(imgx, (cx, cy), 5,(0,255,0), -1) #memunculkan centroid pada gambar

#result=cv2.bitwise_and(image, image, mask=masking)

cv2.imshow("display", imgx)
cv2.waitKey(0)
cv2.destroyAllWindows()




