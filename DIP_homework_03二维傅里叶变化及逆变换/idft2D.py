import numpy as np
def idft2D(F):
    #类似正向变换实现逆变换
    M,N=F.shape
    F=F.conjugate()    #对原图像取共轭
    f1=np.zeros((M,N),dtype='complex128')
    f2=np.zeros((M,N),dtype='complex128')
    for i in range(M):
        f1[i,:]=np.fft.fft(F[i,:])   #对第i行进行一维FFT
    for j in range(N):
        f2[:,j]=np.fft.fft(f1[:,j])  #对第j列进行一维FFT
    f2=np.abs((f2/(M*N)).conjugate()) #添加1/MN的系数并取共轭,最后取模
    
    return f2    


'''
import dft2D
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=dft2D.dft2D(a)
c=idft2D(b)
print('a=','\n',a,'\n','\n','b=dft2D(a)=','\n',b,'\n','\n','c=idft2D(b)=','\n',c,'\n','\n','a-c=','\n',a-c)
  '''

