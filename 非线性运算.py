# -- coding: utf-8 --
import cv2
import matplotlib.pyplot as plt
import numpy as np
from math import log10
img=cv2.imread("1.jpg",0)

img=np.double(img)
result=img**0.5
result= np.uint8(result*255/np.max(result))

# 显示图形
plt.figure(num='comparison')
titles = ['gray Image', 'r=0.5']
images = [img, result]
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
