import numpy as np
from matplotlib import pyplot as plt
import dft2D

#自定义中心化移位函数
def FFT_SHIFT(img): 
    M,N = img.shape
    F=np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            #令f(x,y)=f(x,y)*(-1)^(x+y)实现中心化
            F[i,j]=img[i,j]*np.power(-1,i+j)
    return F

#初始化矩形物体图像
img_test=np.zeros((512,512))
img_test[(512//2-30):(512//2+30),(512//2-5):(512//2+5)]=255
#归一化
img_test=(img_test-np.min(img_test))/(np.max(img_test)-np.min(img_test))

test_fft=np.abs(dft2D.dft2D(img_test))    #FFT

#对中心化的图像矩阵进行二维FFT，并取模
test_shift=np.abs(dft2D.dft2D(FFT_SHIFT(img_test)))


#绘制图像
plt.gray()
plt.figure(figsize=(10,10))
plt.subplot(221)
plt.title('Original Image')
plt.imshow(img_test)                     #源图像
plt.subplot(222)
plt.title('Spectrum')
plt.imshow(test_fft)                     #谱图像
plt.subplot(223)
plt.title('Centered Spectrum')
plt.imshow(test_shift)                   #中心化谱图像
plt.subplot(224)
plt.title('Spectrum After a Log Transformation')
plt.imshow(np.log(1+np.abs(test_shift))) #对数谱图像

plt.savefig('spectrum.jpg')

