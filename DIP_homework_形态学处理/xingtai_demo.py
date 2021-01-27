'''形态学提取骨架并裁剪'''
import numpy as np
from PIL import Image
import rgb1gray    #自编写灰度化模块
import IM2BW       #自编写二值模块
import matplotlib.pyplot as plt
import ErodeDilate as ED # 自编写的腐蚀膨胀函数库
import CutImage as CI   #自编写裁剪模块

I=rgb1gray.rgb1gray(np.array(Image.open('fingerprint/smallfingerprint.jpg')))
I1=~(IM2BW.IM2BW(I))  #将原图转换为二值图像，并取反
SE=np.array([[0,1,0],[1,1,1],[0,1,0]])#结构元SE
m,n=I1.shape
sum_sk=I1&(~ED.imdilate(ED.imerode(I1,SE),SE))#二值图像I1减去自身的开操作
Ik=I1#Ik初始化为原二值图像I1（进行了0次腐蚀）
while np.any(Ik!=False):
    Ik1=ED.imdilate(ED.imerode(Ik,SE),SE)#对Ik进行开操作得到Ik1
    sk=Ik&(~Ik1)          #上一轮腐蚀操作的结果Ik减去其开操作Ik1
    sum_sk=sum_sk|sk     #将sk并集
    Ik=ED.imerode(Ik,SE) #再进行一次Ik的腐蚀操作
I_sk=sum_sk         #提取的骨架
I_cut=CI.Cut(I_sk)  #裁剪后的骨架
d=I_sk&(~I_cut)     #骨架裁剪掉的部分
plt.gray()
plt.figure(figsize=(16,8))
plt.subplot(141)
plt.imshow(I1)
plt.axis('off')
plt.title('(a)Binary Image(Inverted)')
plt.subplot(142)
plt.imshow(I_sk)
plt.axis('off')
plt.title('(b)Extracted skeleton')
plt.subplot(143)
plt.imshow(I_cut)
plt.axis('off')
plt.title('(c)After Prunning')
plt.subplot(144)
plt.imshow(d)
plt.axis('off')
plt.title('(d)Difference of (b) and (c)')

plt.savefig('形态学骨架提取.jpg')

