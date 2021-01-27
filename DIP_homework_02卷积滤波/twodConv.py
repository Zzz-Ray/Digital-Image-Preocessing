import numpy as np
#卷积函数定义，缺省填充方式为zero
def twodConv(f,w,padding='zero'):
    [m,n] = f.shape
    [p,q] = w.shape
    x = np.zeros((m + p - 1, n + q - 1))     #初始化图像填充矩阵
    y = np.zeros((m,n))                      #初始化m*n输出矩阵
    for i in range(0, m):
        for j in range(0, n):
            x[i + p//2][j + q//2] = f[i][j]  #在新矩阵内部的m*n矩阵中复制原图像
    if padding=='zero':
        pass
    if padding=='replicate':#填充方式为复制
        del_h=p//2          #需要填充p行，图片上下各有p//2行
        del_w=q//2          #需要填充q列，图片左右各有q//2列     
        for i in range(del_h):
            x[i,del_w:del_w+n] = f[0,:]             #填充图片正上方矩阵（复制第一行）
            x[m+del_h+i,del_w:del_w+n] = f[-1,:]    #填充图片正下方矩阵（复制最后一行）
        for j in range(del_w):
            x[del_h:m+del_h,j]=f[:,0]               #填充图片正左方矩阵（复制第一列）
            x[del_h:m+del_h,n+del_w+j]=f[:,-1]      #填充图片正右方矩阵（复制最后一列）

        x[0:del_h,0:del_w] = f[0,0]               #左上角小矩阵填充
        x[0:del_h,n+del_w:n+q] = f[0,-1]          #右上角小矩阵填充
        x[m+del_h:m+p,0:del_w] = f[-1,0]          #左下角小矩阵填充
        x[m+del_h:m+p,n+del_w:n+q] = f[-1,-1]     #右下角小矩阵填充
    #将卷积核矩阵左右、上下翻转
    new_w=w.reshape(w.size)
    new_w=new_w[::-1]
    new_w=new_w.reshape(w.shape)
    #翻转后的卷积核在图像上扫描
    for i in range(0,m):
        for j in range(0,n):
            y[i,j]=np.sum(x[i:i+p,j:j+q]*new_w)
        
    # 去掉矩阵乘法后的小于0的和大于255的原值,重置为0和255
    y = y.clip(0, 255)
    y = np.rint(y).astype('uint8')

    return y