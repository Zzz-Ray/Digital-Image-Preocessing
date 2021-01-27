import numpy as np
from scipy import signal#为了调用其二维卷积函数
def imdilate(I,SE):
    IM=np.array(I,dtype='uint8')       #转换输入图像数值类型
    IM_SE=signal.convolve(IM,SE,'same')#结构元SE与图像IM卷积
    m,n=IM.shape
    for i in range(m):
        for j in range(n):
            if IM_SE[i,j]!=0:#卷积结果不为0，则结果赋值为1（True），否则为0
                IM_SE[i,j]=1
            else:
                IM_SE[i,j]=0
    return np.array(IM_SE,dtype='bool')

def imerode(I,SE):
    IM=np.array(I,dtype='uint8')       #转换输入图像数值类型
    IM_SE=signal.convolve(IM,SE,'same')#结构元SE与图像IM卷积
    m,n=IM.shape
    s=np.sum(SE)   #统计结构元SE中“1”的个数
    for i in range(m):
        for j in range(n):
            if IM_SE[i,j]==s:   
                #卷积结果=结构元“1”的个数时,说明结构元覆盖区域包含结构元“1”的范围
                IM_SE[i,j]=1
            else:
                IM_SE[i,j]=0
    return np.array(IM_SE,dtype='bool')


