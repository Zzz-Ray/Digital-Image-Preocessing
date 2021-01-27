# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:58:41 2019

@author: Zhang Ray
"""

def scanLine4e(f,I,loc):
    if loc=='row':
        return f[I,:]
    if loc=='column':
        return f[:,I]


import matplotlib
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
#第一张图片
f1=matplotlib.image.imread('assignment01_images/cameraman.tif')
[m,n]=np.shape(f1)
x1=range(0,n)
x2=range(0,m)

s1=scanLine4e(f1,m//2,'row')
s2=scanLine4e(f1,n//2,'column')
#绘制中心行灰度分布图
ax1=plt.subplot(221)
ax1.set_title('PIC1:the Grayscale Distribution of Central Row')
ax1.set_xlabel('Column Number')
ax1.set_ylabel('Gray_Value')
plt.plot(x1,s1)
#绘制中心列灰度分布图
ax2=plt.subplot(222)
ax2.set_title('PIC1:the Grayscale Distribution of Central Column')
ax2.set_xlabel('Row Number')
ax2.set_ylabel('Gray_Value')
plt.plot(x2,s2)

#第二张图片
f2=matplotlib.image.imread('assignment01_images/einstein.tif')
[p,q]=np.shape(f2)
x3=range(0,q)
x4=range(0,p)

s3=scanLine4e(f2,p//2,'row')
s4=scanLine4e(f2,q//2,'column')
#绘制中心行灰度分布图
ax3=plt.subplot(223)
ax3.set_title('PIC2:the Grayscale Distribution of Central Row')
ax3.set_xlabel('Column Number')
ax3.set_ylabel('Gray_Value')
plt.plot(x3,s3)
#绘制中心列灰度分布图
ax4=plt.subplot(224)
ax4.set_title('PIC2:the Grayscale Distribution of Central Column')
ax4.set_xlabel('Row Number')
ax4.set_ylabel('Gray_Value')
plt.plot(x4,s4)

plt.show()
plt.savefig('homework01_1.tif')