# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:12:58 2019

@author: Zhang Ray
"""

def rgb1gray(f,method='NTSC'):
    if method=='average':
        
        g=f[:,:,0]/3+f[:,:,1]/3+f[:,:,2]/3
        return np.array(g,dtype='uint8')
    if method=='NTSC':
        R=0.2989
        G=0.5870
        B=0.1140
        g=(R*f[:,:,0]+G*f[:,:,1]+B*f[:,:,2])
        return np.array(g,dtype='uint8')

import matplotlib.pyplot as plt
import numpy as np
#第一张图片
f1=plt.imread('assignment01_images/mandril_color.tif')
g11=rgb1gray(f1,'average')
g12=rgb1gray(f1,'NTSC')
#第二张图片
f2=plt.imread('assignment01_images/lena512color.tiff')
g21=rgb1gray(f2,'average')
g22=rgb1gray(f2,'NTSC')

plt.figure(figsize=(7,7))

ax1=plt.subplot(221)
ax1.set_title('PIC1:method=average')
plt.imshow(g11,cmap="gray")

ax2=plt.subplot(222)
ax2.set_title('PIC1:method=NTSC')
plt.imshow(g12,cmap="gray")

ax3=plt.subplot(223)
ax3.set_title('PIC2:method=average')
plt.imshow(g21,cmap="gray")

ax4=plt.subplot(224)
ax4.set_title('PIC2:method=NTSC')
plt.imshow(g22,cmap="gray")

plt.show()
plt.savefig('homework01_2.tif')


