import cv2 as cv
import sys
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 3 영상 처리/JohnHancocksSignature.png',
                cv.IMREAD_UNCHANGED)

print(img.shape)
t, img = cv.threshold(img[:,:,3], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.imshow(img, cmap='gray')
plt.show()

b = img[img.shape[0]//2:, :img.shape[1]//4]
plt.imshow(b, cmap='gray')
plt.show()

se = np.uint8([[0, 1, 0],
               [1, 1, 1],
               [0, 1, 0]])

b_dilation = cv.dilate(b, se, iterations=1)
plt.imshow(b_dilation, cmap='gray')
plt.show()

b_erosion = cv.erode(b, se, iterations=1)
plt.imshow(b_erosion, cmap='gray')
plt.show()

b_closing = cv.erode(cv.dilate(b, se, iterations=1), se, iterations=1)
plt.imshow(b_closing, cmap='gray')
plt.show()