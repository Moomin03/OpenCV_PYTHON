# 연습문제 7번
# 왼쪽을 클릭하면 직사각형, 오른쪽을 클릭하면 원이 그려지도록 확장하시오
import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/연습문제/girl_laughing.jpg')
img = cv.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)

def drawing(event, x, y, flags, params):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+200, y+200), (255, 0, 0), 3)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 10, (0, 255, 0), 3)
    cv.imshow('Painting', img)

cv.imshow('Painting', img)
cv.setMouseCallback('Painting', drawing)
cv.waitKey()
cv.destroyAllWindows()