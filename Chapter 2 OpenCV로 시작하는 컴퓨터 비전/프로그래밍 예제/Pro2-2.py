import cv2 as cv
import sys
img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/soccer.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
print(img.shape)
cv.imshow('Image Display', img)
cv.waitKey()
cv.destroyAllWindows()