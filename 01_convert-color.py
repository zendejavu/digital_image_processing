#Konversi Warna ke Abu-abu
import cv2 
import numpy as np 

img = cv2.imread("/Users/zendejavu/Documents/Politeknik Negeri Samarinda/01 - Pendidikan & Pengajaran/Pengolahan Citra Digital (Semester V)/02 - Pengantar Citra Digital/lands.jpg")
cv2.imshow("Original", img)

row, col = img.shape[0:2]

for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow("Hasil", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
