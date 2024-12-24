# 연습문제 8번
# 왼쪽버튼은 그대로 두고 오르느쪽 버튼의 경우 클릭한 곳이 원의 중심이고, 오른쪽 버튼을 놓은 곳이 원주다
import cv2 as cv
import sys
import numpy as np

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/연습문제/girl_laughing.jpg')
img = cv.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)

def drawing(event, x, y, flags, params):
    global ix, iy
    if event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+200, y+200), (255, 0, 0), 3)
    elif event==cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event==cv.EVENT_LBUTTONUP:
        cv.circle(img, (ix,iy), int(np.sqrt((ix-x)**2+(iy-y)**2)), (0, 255, 0), 3)
    cv.imshow('Painting', img)

cv.imshow('Painting', img)
cv.setMouseCallback('Painting', drawing)
cv.waitKey()
cv.destroyAllWindows()