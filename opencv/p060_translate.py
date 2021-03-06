# coding: utf-8
import cv2
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

mpl.rcParams['toolbar'] = 'None'

img = cv2.imread('messi5.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

plt.imshow( dst )
plt.show() 