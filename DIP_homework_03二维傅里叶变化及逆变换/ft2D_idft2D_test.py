import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import dft2D
import idft2D

img=np.array(Image.open('assignment01_images\\rose512.tif'))
f=(img-np.min(img))/(np.max(img)-np.min(img))#归一化图像
F=dft2D.dft2D(f)
g=idft2D.idft2D(F)       
a=np.array((f-g),dtype='uint8')   #计算原图像与其差值，并将差值规范为uint8型

plt.figure(figsize=(10,5))
plt.subplot(121)
plt.title('Original Image')
plt.imshow(img)
plt.subplot(122)
plt.title('f-g')
plt.imshow(a)

plt.savefig('dft_idft.jpg')

