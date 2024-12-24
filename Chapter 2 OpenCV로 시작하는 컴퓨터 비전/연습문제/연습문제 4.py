# 연습문제 4번
# 0.1부터 1.0으로 축소한 영상 10개를 서로 다른 윈도우에 표시하시오
import cv2 as cv
import sys
import numpy as np
np.set_printoptions(precision=1)
img1 = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/연습문제/girl_laughing.jpg')
for i in np.arange(0.1, 1.1, 0.1):
    img = cv.resize(img1, dsize=(0, 0), fx=i, fy=i)
    cv.imshow('Girl', img)
    cv.waitKey()
    cv.destroyAllWindows()