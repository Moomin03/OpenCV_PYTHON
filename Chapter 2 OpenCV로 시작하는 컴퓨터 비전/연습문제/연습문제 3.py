# 연습문제 3번
# 서로 다른 두개의 영상을 읽고 각각 화면에 띄우시오
import cv2 as cv
import sys
img1 = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/연습문제/girl_laughing.jpg')
img2 = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/연습문제/soccer.jpg')

img1 =cv.resize(img1, dsize=(0, 0), fx=0.5, fy=0.5)
img2 =cv.resize(img2, dsize=(0, 0), fx=0.5, fy=0.5)

cv.imshow('Girl', img1)
cv.imshow('Soccer', img2)
cv.waitKey()
cv.destroyAllWindows()