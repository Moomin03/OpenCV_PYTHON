import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/home/kali/Documents/Git/Computer_Vision/Chapter 3 영상 처리/soccer.jpg')
h = cv.calcHist(images=[img], channels=[2], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(h, color='red')
plt.show()