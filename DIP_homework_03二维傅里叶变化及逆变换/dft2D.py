import numpy as np
def dft2D(f):
    #两轮一维FFT实现
    m,n=f.shape                   #输入图像的尺寸
    F1=np.zeros((m,n),dtype='complex128')#创建两个m*n的复数类型的零矩阵
    F2=np.zeros((m,n),dtype='complex128')
    for i in range(m):
        F1[i,:]=np.fft.fft(f[i,:])    #对原始图像f的第i行进行一维fft
    for j in range(n):
        F2[:,j]=np.fft.fft(F1[:,j])   #对已经进行过“行fft”的矩阵第j列进行一维fft
    return F2

'''
通过与numpy库函数比较，验证自定义二维FFT函数的正确性
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=dft2D(a)
c=np.fft.fft2(a)
print('a=','\n',a,'\n','\n','b=dft2D(a)=','\n',b,'\n','\n','c=np.fft.fft2(a)=','\n',c,'\n','\n','b-c=','\n',b-c)
'''  
 

