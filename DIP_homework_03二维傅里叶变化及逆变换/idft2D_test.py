import numpy as np
import idft2D
import dft2D
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=dft2D.dft2D(a)
c=idft2D.idft2D(b)
print('a=','\n',a,'\n','\n','b=dft2D(a)=','\n',b,'\n','\n','c=idft2D(b)=','\n',c,'\n','\n','a-c=','\n',a-c)