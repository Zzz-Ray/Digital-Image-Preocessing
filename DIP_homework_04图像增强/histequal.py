import numpy as np

def histequal4e(I):
    #对输入I的类型以及数据类型进行检测，如果不满足则程序运行终止
    assert(type(I)==np.ndarray)
    assert(I.dtype==np.uint8)#要求输入的图像是8比特图像
    #直方图统计
    hist=[0 for x in range(256)] #新建一个长度为256的0元素列表
    m,n=I.shape
    img=np.zeros((m,n))          #新建一个与输入同尺寸的零矩阵作为输出
    for i in range(m):
        for j in range(n):
            hist[I[i,j]]+=1
    #归一化处理
    for i in range(256):
        hist[i]=hist[i]/(n*m)
    #直方图累加
    for i in range(1,256):
        hist[i]+=hist[i-1]
    #均衡化得到新的灰度分布   
    for i in range(256):
        hist[i]=np.uint8(hist[i]*255)
    #得到输出图像的对应像素灰度值
    for i in range(m):
        for j in range(n):
            img[i,j]=hist[I[i,j]]
    
    return img



    
    
