import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import laplace #拉普拉斯增强函数模块

img=np.array(Image.open('assignment01_images/cameraman.tif'))
img_laplace1=laplace.laplace_sharpen(img,0.1)#锐化系数为0.1
img_laplace2=laplace.laplace_sharpen(img,0.5)#锐化系数为0.5
img_laplace3=laplace.laplace_sharpen(img,1)#锐化系数为1
plt.gray()
plt.figure(figsize=(10,10))
plt.subplot(221)
plt.title('(a) Original Image')
plt.imshow(img)
plt.subplot(222)
plt.title('(b) laplace_sharpen c=0.1')
plt.imshow(img_laplace1)
plt.subplot(223)
plt.title('(c) laplace_sharpen c=0.5')
plt.imshow(img_laplace2)
plt.subplot(224)
plt.title('(d) laplace_sharpen c=1')
plt.imshow(img_laplace3)

plt.savefig('laplace_sharpen_result.jpg')




