import numpy as np
def IM2BW(I):
    m,n=I.shape
    B=np.zeros((m,n))
    th=np.floor(np.max(I)+np.min(I))/2#定义阈值
    for i in range(m):
        for j in range(n):
            if I[i,j]>=th:
                B[i,j]=True        #灰度大于等于阈值，为True
            else:
                B[i,j]=False       #灰度小于阈值，为False
    return np.array(B,dtype='bool')

