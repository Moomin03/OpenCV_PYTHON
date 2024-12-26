import cv2 as cv
import matplotlib.pyplot as plt
import sys

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 3 영상 처리/forest.jpg', 
                cv.IMREAD_UNCHANGED)
if img is None:
    sys.exit('파일이 존재하지 않습니다.')
    
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
t, otsu_img = cv.threshold(img[:,:,2], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    
plt.imshow(otsu_img, cmap='gray')
plt.show()