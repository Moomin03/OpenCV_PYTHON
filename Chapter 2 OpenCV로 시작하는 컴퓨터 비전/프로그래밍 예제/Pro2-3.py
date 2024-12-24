# I = round(0.299*R+0.587*G+0.114*B)
import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/soccer.jpg')
if img is None:
    sys.exit('파일이 존재하지 않습니다.')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5)

cv.imshow('gray_image', gray_small)
cv.waitKey()
cv.destroyAllWindows()