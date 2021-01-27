import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import histequal              #导入自编写的函数模块

I=np.array(Image.open('assignment01_images\einstein.tif'))#读取图像
img=histequal.histequal4e(I)                               #直方图均衡化
img1= cv2.equalizeHist(I)     #使用Opencv库直方图均衡化函数

plt.gray()
plt.figure(figsize=(15,8))

plt.subplot(231)
plt.title('(a)Original Image')
plt.imshow(I)     #绘制原始图像
plt.subplot(232)
plt.title('(b)After My_Histogram_equalization')
plt.imshow(img)  #绘制自编直方图均衡化函数作用后的图像
plt.subplot(233)
plt.title('(c)After Opencv_Histogram_equalization')
plt.imshow(img1) #绘制opencv库函数均衡后的图像
plt.subplot(234)
plt.title('(e)The histogram of origin image')
plt.hist(I.ravel(),256,[0,256]) #绘制原始图像的灰度直方图(ravel函数将多维数组降为一维数组)
plt.subplot(235)
plt.title('(f)Histogram:Using My histequal_function')
plt.hist(img.ravel(),256,[0,256]) #绘制自编写函数均衡化后的直方图
plt.subplot(236)
plt.title('(g)Histogram:Using cv2.equalizeHist')
plt.hist(img1.ravel(),256,[0,256])#绘制opencv库函数均衡化后图像的直方图

plt.savefig('hist-equalization.jpg')   


