import numpy as np
import ErodeDilate as ED
def Cut(I):
    I_copy=I
    #定义结构元B1~B8。
    #因为B1~B4中存在元素为"x"，因此定义B1_1~B4_1作为对应的翻转结构元
    B1=np.array([[0,0,0],[1,1,0],[0,0,0]])
    B1_1=np.array([[0,1,1],[0,0,1],[0,1,1]])
    B2=np.array([[0,1,0],[0,1,0],[0,0,0]])
    B2_1=np.array([[0,0,0],[1,0,1],[1,1,1]])
    B3=np.array([[0,0,0],[0,1,1],[0,0,0]])
    B3_1=np.array([[1,1,0],[1,0,0],[1,1,0]])
    B4=np.array([[0,0,0],[0,1,0],[0,1,0]])
    B4_1=np.array([[1,1,1],[1,0,1],[0,0,0]])
    B5=np.array([[1,0,0],[0,1,0],[0,0,0]])
    B6=np.array([[0,0,1],[0,1,0],[0,0,0]])
    B7=np.array([[0,0,0],[0,1,0],[0,0,1]])
    B8=np.array([[0,0,0],[0,1,0],[1,0,0]])
    SE=np.array([[1,1,1],[1,1,1],[1,1,1]])
    k=0#计数值
    N=3#进行N次操作
    while k<N:#N次结构元细化操作
        I1=~(ED.imerode(I,B1)&ED.imerode(~(I),B1_1))
        I2=~(ED.imerode(I,B2)&ED.imerode(~(I),B2_1))
        I3=~(ED.imerode(I,B3)&ED.imerode(~(I),B3_1))
        I4=~(ED.imerode(I,B4)&ED.imerode(~(I),B4_1))
        I5=~(ED.imerode(I,B5)&ED.imerode(~(I),np.ones((3,3))-B5))
        I6=~(ED.imerode(I,B6)&ED.imerode(~(I),np.ones((3,3))-B6))
        I7=~(ED.imerode(I,B7)&ED.imerode(~(I),np.ones((3,3))-B7))
        I8=~(ED.imerode(I,B8)&ED.imerode(~(I),np.ones((3,3))-B8))
        I=I&I1&I2&I3&I4&I5&I6&I7&I8
        k=k+1
    X1=I
    #每个结构元进行击中击不中变换提取端点集合
    I1=ED.imerode(I,B1)&ED.imerode(~(I),B1_1)
    I2=ED.imerode(I,B2)&ED.imerode(~(I),B2_1)
    I3=ED.imerode(I,B3)&ED.imerode(~(I),B3_1)
    I4=ED.imerode(I,B4)&ED.imerode(~(I),B4_1)
    I5=ED.imerode(I,B5)&ED.imerode(~(I),1-B5)
    I6=ED.imerode(I,B6)&ED.imerode(~(I),1-B6)
    I7=ED.imerode(I,B7)&ED.imerode(~(I),1-B7)
    I8=ED.imerode(I,B8)&ED.imerode(~(I),1-B8)
    X2=I1|I2|I3|I4|I5|I6|I7|I8
    X3=X2
    k=0
    while k<N:#进行N次在原图像I的限定下的膨胀
        X3=I_copy&ED.imdilate(X3,SE)
        k=k+1
    X4=X1|X3
    return np.array(X4,dtype='bool')

