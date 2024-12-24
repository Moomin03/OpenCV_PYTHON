# 연습문제 9번
# 붓의 크기가 +를 누르면 커지고, -를 누르면 작아지도록 만들어라
import cv2 as cv
import sys
 
img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/연습문제/girl_laughing.jpg')
if img is None:
    sys.exit('파일이 존재하지 않습니다.')
    
global radius
radius=5
def painting(event, x, y, flags, params):
    if event==cv.EVENT_LBUTTONDOWN and flags==cv.EVENT_FLAG_LBUTTON:
            cv.circle(img, (x, y), radius, (255, 0, 0), -1)
    cv.imshow('Painting', img)

cv.imshow('Painting', img)
cv.setMouseCallback('Painting', painting)

while True:
    key = cv.waitKey(1)
    if key==ord('+'):
        radius+=1
    elif key==ord('-'):
        radius-=1
    elif key==ord('q'):
        break
    
cv.destroyAllWindows()