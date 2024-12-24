import cv2 as cv
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 2 OpenCV로 시작하는 컴퓨터 비전/girl_laughing.jpg')

if img is None:
    sys.exit('파일이 존재하지 않습니다.')
    
def draw(event, x, y, flag, params):
    global ix, iy
    if event==cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event==cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)
        
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)
cv.waitKey()
cv.destroyAllWindows()