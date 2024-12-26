import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 3 영상 처리/soccer.jpg')
if img is None:
    sys.exit('파일이 존재하지 않습니다.')

cv.imshow('Original_RGB', img)
cv.imshow('Upper left half', img[:img.shape[0]//2, :img.shape[1]//2, :])
cv.imshow('Center half', img[:img.shape[0]//2, img.shape[1]//4*2:img.shape[1]//4*3, :])

cv.imshow('B channel', img[:, :, 0])
cv.imshow('G channel', img[:, :, 1])
cv.imshow('R channel', img[:, :, 2])

cv.waitKey()
cv.destroyAllWindows()