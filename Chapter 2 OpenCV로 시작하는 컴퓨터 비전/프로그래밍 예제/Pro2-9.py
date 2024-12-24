import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/girl_laughing.jpg')
if img is None:
    sys.exit('파일이 존재하지 않습니다.')

def painting(event, x, y, flags, params):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 5, (255, 0, 0), -1)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x, y), 5, (255, 0, 0), -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    
    cv.imshow('Painting', img)

cv.namedWindow('Painting')
cv.imshow('Painting', img)
cv.setMouseCallback('Painting', painting)

while True:
    if cv.waitKey()==ord('q'):
        cv.destroyAllWindows()
        break