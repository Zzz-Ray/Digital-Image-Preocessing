from PIL import Image
import numpy as np
from pylab import* 
import cv2
import gaussKernel#高斯核
import twodConv#卷积
import rgb1gray#真彩转灰度

#读取图片
img1=np.array(Image.open('assignment01_images\cameraman.tif'))
img2=np.array(Image.open('assignment01_images\einstein.tif'))
img3=np.array(Image.open('assignment01_images\lena512color.tiff'))
img4=np.array(Image.open('assignment01_images\mandril_color.tif'))
#其中的真彩图像用NTSC方式转换为灰度图像
img3=rgb1gray.rgb1gray(img3,method='NTSC')
img4=rgb1gray.rgb1gray(img4,method='NTSC')

w1=gaussKernel.gaussKernel(1)
w2=gaussKernel.gaussKernel(2)
w3=gaussKernel.gaussKernel(3)
w4=gaussKernel.gaussKernel(5)
gray()
#分别对4张图片进行sig=1、2、3、5的高斯核卷积运算得到新的图像(填充方式选用复制replicate)
img_out1=twodConv.twodConv(img1,w1,padding='replicate')
img_out2=twodConv.twodConv(img1,w2,padding='replicate')
img_out3=twodConv.twodConv(img1,w3,padding='replicate')
img_out4=twodConv.twodConv(img1,w4,padding='replicate')

img_out5=twodConv.twodConv(img2,w1,padding='replicate')
img_out6=twodConv.twodConv(img2,w2,padding='replicate')
img_out7=twodConv.twodConv(img2,w3,padding='replicate')
img_out8=twodConv.twodConv(img2,w4,padding='replicate')

img_out9=twodConv.twodConv(img3,w1,padding='replicate')
img_out10=twodConv.twodConv(img3,w2,padding='replicate')
img_out11=twodConv.twodConv(img3,w3,padding='replicate')
img_out12=twodConv.twodConv(img3,w4,padding='replicate')

img_out13=twodConv.twodConv(img4,w1,padding='replicate')
img_out14=twodConv.twodConv(img4,w2,padding='replicate')
img_out15=twodConv.twodConv(img4,w3,padding='replicate')
img_out16=twodConv.twodConv(img4,w4,padding='replicate')

#对卷积后的图像进行绘制并存储
figure(figsize=(25,7))
subplot(141)
imshow(img_out1)
title('sigma=1',size=30)
subplot(142)
imshow(img_out2)
title('sigma=2',size=30)
subplot(143)
imshow(img_out3)
title('sigma=3',size=30)
subplot(144)
imshow(img_out4)
title('sigma=5',size=30)
savefig('result_img1.jpg')

figure(figsize=(25,7))
subplot(141)
imshow(img_out5)
title('sigma=1',size=30)
subplot(142)
imshow(img_out6)
title('sigma=2',size=30)
subplot(143)
imshow(img_out7)
title('sigma=3',size=30)
subplot(144)
imshow(img_out8)
title('sigma=5',size=30)
savefig('result_img2.jpg')

figure(figsize=(25,7))
subplot(141)
imshow(img_out9)
title('sigma=1',size=30)
subplot(142)
imshow(img_out10)
title('sigma=2',size=30)
subplot(143)
imshow(img_out11)
title('sigma=3',size=30)
subplot(144)
imshow(img_out12)
title('sigma=5',size=30)
savefig('result_img3.jpg')

figure(figsize=(25,7))
subplot(141)
imshow(img_out13)
title('sigma=1',size=30)
subplot(142)
imshow(img_out14)
title('sigma=2',size=30)
subplot(143)
imshow(img_out15)
title('sigma=3',size=30)
subplot(144)
imshow(img_out16)
title('sigma=5',size=30)
savefig('result_img4.jpg')

#利用自带函数进行高斯核卷积操作，其中sigma=1
def gaussian_kernel_2d_opencv(kernel_size = 3,sigma = 0):
    kx = cv2.getGaussianKernel(kernel_size,sigma)
    ky = cv2.getGaussianKernel(kernel_size,sigma)
    return np.multiply(kx,np.transpose(ky)) #利用opencv库自带一维高斯核函数构造二维高斯核函数
wb=gaussian_kernel_2d_opencv(7,1)           #生成与w1相同尺寸、相同标准差的高斯核

img_outI = cv2.filter2D(img2, -1, wb)       #调用opencv中卷积函数-第一张图
img_difI=abs(img_out5-img_outI)
img_outII = cv2.filter2D(img4, -1, wb)      #调用opencv中卷积函数-第二张图
img_difII=abs(img_out13-img_outII)

figure(figsize=(15,10))
subplot(231)
imshow(img_out5)
title('Using my function (sigma=1)',size=15)
subplot(232)
imshow(img_outI)
title('Using internal functions (sigma=1)',size=15)
subplot(233)
imshow(img_difI)
title('The difference (sigma=1)',size=15)
subplot(234)
imshow(img_out13)
title('Using my function (sigma=1)',size=15)
subplot(235)
imshow(img_outII)
title('Using internal functions (sigma=1)',size=15)
subplot(236)
imshow(img_difII)
title('The difference (sigma=1)',size=15)
savefig('result_diffence.jpg')

#比较其他参数条件不变的情况下像素复制和补零下滤波结果在边界上的差别
img_out_zero1=twodConv.twodConv(img1,w1,padding='zero')
img_out_replicate1=twodConv.twodConv(img1,w1,padding='replicate')
img_out_zero2=twodConv.twodConv(img4,w1,padding='zero')
img_out_replicate2=twodConv.twodConv(img4,w1,padding='replicate')
figure(figsize=(20,10))

subplot(241)
imshow(img_out_zero1)
title('zero-padding (sigma=1)',size=17)
axis("off")

subplot(242)
imshow(img_out_replicate1)
title('Replication-padding (sigma=1)',size=17)
axis("off")

subplot(243)
covdif1=abs(img_out_replicate1-img_out_zero1)
imshow(covdif1)
title('difference (sigma=1)',size=17)
axis("off")

subplot(244)
imshow(255-covdif1)
axis("off")
title('difference[reverse] (sigma=1)',size=17)

subplot(245)
imshow(img_out_zero2)
title('zero-padding (sigma=1)',size=17)
axis("off")

subplot(246)
imshow(img_out_replicate2)
title('Replication-padding (sigma=1)',size=17)
axis("off")

subplot(247)
covdif2=abs(img_out_replicate2-img_out_zero2)
imshow(covdif2)
title('difference (sigma=1)',size=17)
axis("off")

subplot(248)
imshow(255-covdif2)
axis("off")
title('difference[reverse] (sigma=1)',size=17)
savefig('covdif.jpg')

show()





