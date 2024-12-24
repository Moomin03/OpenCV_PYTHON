import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/girl_laughing.jpg')
if img is None:
    sys.exit('파일이 존재하지 않습니다.')
cv.rectangle(img, (830, 30), (1000, 200), (0, 0, 255), 2)
cv.putText(img, 'laugh', (830, 24), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv.imshow('laugh', img)
cv.waitKey()
cv.destroyAllWindows()