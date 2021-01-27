import numpy as np
from PIL import Image
import rgb1gray
import IM2BW  #二值化模块
import matplotlib.pyplot as plt
import ErodeDilate as ED # 自编写的腐蚀膨胀函数模块
import CutImage as CI  #裁剪模块

I=rgb1gray.rgb1gray(np.array(Image.open('fingerprint/smallfingerprint.jpg')))
II=~(IM2BW.IM2BW(I))      #将灰度图转换为二值图像并取反
SE=np.array([[0,1,0],[1,1,1],[0,1,0]])#结构元SE
I1=ED.imdilate(II,SE)&~II     #膨胀结果减去原二值图得到边界图像I1
A=np.array(I1,dtype='float64') #转换I1的数值类型便于计算距离
m,n=A.shape
for i in range(m):
    for j in range(n):
        if A[i,j]==0:
            A[i,j]=100#将图像背景值为100
#进行距离变换
#从上至下，从左至右
for i in range(1,m):
    for j in range(1,n-1):
        temp0=A[i,j]
        temp1=min([A[i,j-1]+3,temp0])
        temp2=min([A[i-1,j-1]+4,temp1])
        temp3=min([A[i-1,j]+3,temp2])
        temp4=min([A[i-1,j+1]+4,temp3])
        
        A[i,j]=temp4
#从下至上，从右至左
for i in range(m-2,-1,-1):
    for j in range(n-2,0,-1):
        temp0=A[i,j]
        temp1=min([A[i,j+1]+3,temp0])
        temp2=min([A[i+1,j-1]+4,temp1])
        temp3=min([A[i+1,j]+3,temp2])
        temp4=min([A[i+1,j+1]+4,temp3])
        A[i,j]=temp4
D=A
m,n=D.shape
D1=np.zeros((m,n))#存放距离变换的竖直方向差分梯度
D2=np.zeros((m,n))#存放距离变换的水平方向差分梯度
D3=np.zeros((m,n))#提取到的骨架（未转变为Bool型）
#计算水平与竖直方向的差分（梯度）         
for i in range(1,m-1):
    for j in range(1,n-1):
        D1[i,j]=D[i+1,j]-D[i-1,j]#竖直方向
        D2[i,j]=D[i,j+1]-D[i,j-1]#水平方向
for i in range(1,m-1):
    for j in range(1,n-1):
        #判断局部极大值
        if ((D1[i,j]>0)&(D1[i+1,j]<=0))or((D2[i,j]>=0)&(D2[i,j+1]<0)):
            D3[i,j]=1
        else:
            D3[i,j]=0
for i in range(m):
    for j in range(n):
        #将局部极大值点与原图进行对比筛选最终的骨架
        if (D3[i,j]!=0)and(II[i,j]==True):
            D3[i,j]=1
        else:
            D3[i,j]=0
I_sk=np.array(D3,dtype='bool')#转换为Bool型，即提取的骨架
I_cut=CI.Cut(I_sk)     #裁剪后的骨架
d=I_sk&(~I_cut)        #裁剪掉的部分

plt.gray()
plt.figure(figsize=(15,12))
plt.subplot(231)
plt.imshow(I)
plt.axis('off')
plt.title('(a)Original Image')
plt.subplot(232)
plt.imshow(II)
plt.axis('off')
plt.title('(b)Binary Image(Inverted)')
plt.subplot(233)
plt.imshow(I1)
plt.axis('off')
plt.title('(c)Edge of Iamge')
plt.subplot(234)
plt.imshow(I_sk)
plt.axis('off')
plt.title('(d)Extracted skeleton')
plt.subplot(235)
plt.imshow(I_cut)
plt.axis('off')
plt.title('(e)After Prunning')
plt.subplot(236)
plt.imshow(d)
plt.axis('off')
plt.title('(f)Difference of (d) and (e)')

plt.savefig('距离变换骨架提取.jpg')

    