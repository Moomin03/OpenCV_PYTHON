import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 3 영상 처리/soccer.jpg')
t, otsu_img = cv.threshold(img[:, :, 2], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘에서 찾은 최적 임곗값 : ' + str(t))

cv.imshow('R Channel', img[:, :, 2])
cv.imshow('R Channel Binarization', otsu_img)

cv.waitKey()
cv.destroyAllWindows()