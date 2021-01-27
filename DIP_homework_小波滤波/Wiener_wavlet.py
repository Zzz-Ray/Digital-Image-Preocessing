import numpy as np
import pywt
from PIL import Image
import matplotlib.pyplot as plt
def weina(Y,HH):#Y为小波域图像，HH为双高通子图
    sigma_n=np.median(np.abs(HH))/0.6745
    X=np.copy(Y)
    m,n=Y.shape
    M=m*n
    sigma2=np.sum(Y**2)/M-sigma_n**2
    X=Y*sigma2/(sigma2+sigma_n**2)
    return X

def gen_gaussian_noise(signal,SNR):
    """
    :param signal: 原始信号
    :param SNR: 添加噪声的信噪比
    :return: 生成的噪声
    """
    noise=np.random.randn(*signal.shape) # *signal.shape 获取样本序列的尺寸
    noise=noise-np.mean(noise)
    signal_power=(1/signal.shape[0])*np.sum(np.power(signal,2))
    noise_variance=signal_power/np.power(10,(SNR/10))
    noise=(np.sqrt(noise_variance)/np.std(noise))*noise
    noise=noise.reshape((signal.shape[0],signal.shape[1]))#噪声序列reshape成与图形长宽相同的矩阵
    return noise+signal

X = np.array(Image.open("assignment01_images/lena.tif"))
img=gen_gaussian_noise(X,10)#添加高斯噪声，指定信噪比
#一次小波分解进行维纳滤波
cA,(cH,cV,cD)=pywt.dwt2(img,'haar')
cH=weina(cH,cD)
cV=weina(cV,cD)
cD=weina(cD,cD)
w1=pywt.idwt2((cA, (cH, cV, cD)),'haar')#重建
#两次小波分解进行维纳滤波
cA1,(cH1,cV1,cD1)=pywt.dwt2(img,'haar')
cA2, (cH2, cV2, cD2)=pywt.dwt2(cA1,'haar')
cH1=weina(cH1,cD1)
cV1=weina(cV1,cD1)
cD1=weina(cD1,cD1)
cH2=weina(cH2,cD1)
cV2=weina(cV2,cD1)
cD2=weina(cD2,cD1)
w2_1=pywt.idwt2((cA2, (cH2, cV2, cD2)),'haar')
w2=pywt.idwt2((w2_1, (cH1, cV1, cD1)),'haar')#重建
#三次小波分解进行维纳滤波
CA1,(CH1,CV1,CD1)=pywt.dwt2(img,'haar')
CA2, (CH2, CV2, CD2)=pywt.dwt2(CA1,'haar')
CA3, (CH3, CV3, CD3)=pywt.dwt2(CA2,'haar')
CH3=weina(CH3,CD1)
CV3=weina(CV3,CD1)
CD3=weina(CD3,CD1)
CH2=weina(CH2,CD1)
CV2=weina(CV2,CD1)
CD2=weina(CD2,CD1)
CH1=weina(CH1,CD1)
CV1=weina(CV1,CD1)
CD1=weina(CD1,CD1)
w3_1=pywt.idwt2((CA3, (CH3, CV3, CD3)),'haar')
w3_2=pywt.idwt2((w3_1, (CH2, CV2, CD2)),'haar')
w3=pywt.idwt2((w3_2,(CH1,CV1,CD1)),'haar')#重建

plt.figure(figsize=(25,5))
plt.gray()
plt.subplot(151)
plt.imshow(X)
plt.axis('off')
plt.title('(a) Original image')
plt.subplot(152)
plt.imshow(img)
plt.axis('off')
plt.title('(b) Image(Add noise)')
plt.subplot(153)
plt.imshow(w1)
plt.axis('off')
plt.title('(c) After filtering(1)')
plt.subplot(154)
plt.imshow(w2)
plt.axis('off')
plt.title('(d) After filtering(2)')
plt.subplot(155)
plt.imshow(w3)
plt.axis('off')
plt.title('(e) After filtering(3)')
plt.savefig('小波域维纳滤波.jpg')


