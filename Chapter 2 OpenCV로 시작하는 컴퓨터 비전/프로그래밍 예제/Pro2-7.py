import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/girl_laughing.jpg')

if img is None:
    sys.exit('파일이 존재하지 않습니다.')
    
def draw(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+200, y+200), (0, 255, 255), 2)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), 2)
    cv.imshow('Drawing', img)
    
cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)
while True:
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break