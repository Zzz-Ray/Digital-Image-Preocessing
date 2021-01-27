import numpy as np
import dft2D
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=dft2D.dft2D(a)
c=np.fft.fft2(a)
print('a=','\n',a,'\n','\n','b=dft2D(a)=','\n',b,'\n','\n','c=np.fft.fft2(a)=','\n',c,'\n','\n','b-c=','\n',b-c)
