# 연습문제 6번
# 화살표 그리고, laugh를 직사각형에서 좀 떨어뜨려 표시하시오
import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/연습문제/girl_laughing.jpg')
if img is None:
    sys.exit('파일이 존재하지 않습니다.')
img = cv.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)
    
cv.rectangle(img, (406, 11), (484, 103), (0, 255, 0), 3)
cv.arrowedLine(img, (335, 55), (393, 55), (255, 0, 0), 3)
cv.putText(img, 'laugh', (250, 55), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255))
cv.imshow('Window', img)

cv.waitKey()
cv.destroyAllWindows()