import numpy as np
def laplace_sharpen(I,c=0.1,padding='zero'):
    #c锐化系数，这里设置缺省值为0.1;padding为填充方式，默认为零元素填充
    # 拉普拉斯算子
    laplace_filter = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0],
    ]) 
    m,n=I.shape
    I1=np.zeros((m+2,n+2))
    #周围填充0保证输出图像尺寸不变
    for i in range(m):
        for j in range(n):
            I1[i+1,j+1]=I[i,j]       
    #根据不同的填充方式来填充           
    if padding=='zero':
        pass
    if padding=='replicate':#填充方式为复制
        I1[0,1:1+n] = I[0,:]         #复制第一行
        I1[-1,1:1+n] = I[-1,:]    #复制最后一行
        I1[1:m+1,0]=I[:,0]           #复制第一列
        I1[1:m+1,-1]=I[:,-1]      #复制最后一列
        I1[0,0] = I[0,0]             #左上角填充
        I1[0,-1] = I[0,-1]          #右上角填充
        I1[-1,0] = I[-1,0]          #左下角填充
        I1[-1,-1] = I[-1,-1]       #右下角填充
    I1=np.array(I1,dtype='uint8')

    img_out = np.copy(I1)  # 复制填充后的图像作为输出图像
    for i in range(1, m+1):
        for j in range(1, n+1):
            # 拉普拉斯算子在图像上卷积计算
            R = np.sum(laplace_filter * I1[i - 1:i + 2, j - 1:j + 2])  
            #将算子计算结果乘以锐化系数叠加到原图像上作为输出
            img_out[i, j] = I1[i, j] - c * R
    img_out = img_out[1:m+1, 1:n+1]  # 把输出图像周围多余填充区域裁剪

    return img_out

