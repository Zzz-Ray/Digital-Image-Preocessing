import sys
import numpy as np
def gaussKernel(sig,m=0):
    if m==0:#当m没有输入时默认值为0，此时根据公式计算m大小
        m=round(3*sig)*2+1
    if m<(round(3*sig)*2+1):#如果m输入值过小，则程序运行终止，提示重新输入m值
        print("输入的m值过小，请重新输入m")
        sys.exit(0)
        return 0
    
    kernel=np.zeros((m,m))#一个m*m的零矩阵作为高斯核的初始化矩阵
    center=m//2           #计算中心位置
    s=sig**2
    sum=0
    for i in range(m):
        for j in range(m):
            x, y = i-center, j-center              #核内元素到中心点的距离           
            kernel[i, j] = np.exp(-(x**2+y**2)/(2*s))#高斯公式计算滤波核元素值
            sum += kernel[i, j]                    #高斯核所有元素总和
    kernel = kernel/sum   #归一化处理
    return kernel



