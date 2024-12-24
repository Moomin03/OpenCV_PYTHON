# 연습문제 5번
# g를 입력하면 명암 영상을, c를 입력하면 컬러영상을 디스플레이하도록 하시오
import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/연습문제/soccer.jpg')
if img is None:
    sys.exit('파일이 존재하지 않습니다.')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.namedWindow('Normal Picture')

while True:    
    if cv.waitKey()==ord('g'):
        cv.imshow('Normal Picture', gray_img)
    elif cv.waitKey()==ord('c'):
        cv.imshow('Normal Picture', img)
    elif cv.waitKey()==ord('q'):
        break
cv.destroyAllWindows()