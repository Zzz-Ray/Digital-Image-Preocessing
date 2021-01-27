import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import smooth
import SaltPepper

I=np.array(Image.open('assignment01_images/cameraman.tif'))  #读取图像   
I_sp=SaltPepper.sp_noise(I,snr=0.9)         #加入椒盐噪声
I_smooth1=smooth.smoothFunc(I_sp,'zero') #使用有选择保边缘平滑滤波(零元素填充)
I_smooth2=smooth.smoothFunc(I_sp,'replicate') #使用有选择保边缘平滑滤波(复制填充)
difference=abs(I_smooth2-I_smooth1)

plt.gray()
plt.figure(figsize=(15,10))       
plt.subplot(231)   
plt.title('(a)Original Image')         
plt.imshow(I)
plt.subplot(232)
plt.title('(b)Add Salt_Pepper noise')
plt.imshow(I_sp)
plt.subplot(233)
plt.title('(c)After filtering(padding=zero)')
plt.imshow(I_smooth1)
plt.subplot(234)
plt.title('(d)After filtering(padding=replicate)')
plt.imshow(I_smooth2)
plt.subplot(235)
plt.title('(e)Difference between (c)and(d)')
plt.axis('off')
plt.imshow(difference)
plt.subplot(236)
plt.title('(f)Reverse image(e)')
plt.axis('off')
plt.imshow(255-difference)

plt.savefig('smooth_test.jpg')


