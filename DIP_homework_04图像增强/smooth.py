import numpy as np
def smoothFunc(I,padding='zero'):
    m,n=I.shape
    img=np.zeros((m,n))
    I1=np.zeros((m+4,n+4))
    #周围填充0保证输出图像尺寸不变
    for i in range(m):
        for j in range(n):
            I1[i+2,j+2]=I[i,j]
            
    #根据不同的填充方式来填充           
    if padding=='zero':
        pass
    if padding=='replicate':#填充方式为复制
        
        for i in range(2):
            I1[i,2:2+n] = I[0,:]             #填充图片正上方矩阵（复制第一行）
            I1[m+2+i,2:2+n] = I[-1,:]    #填充图片正下方矩阵（复制最后一行）
        for j in range(2):
            I1[2:m+2,j]=I[:,0]               #填充图片正左方矩阵（复制第一列）
            I1[2:m+2,n+2+j]=I[:,-1]      #填充图片正右方矩阵（复制最后一列）
      
        I1[0:2,0:2] = I[0,0]               #左上角小矩阵填充
        I1[0:2,n+2:n+4] = I[0,-1]          #右上角小矩阵填充
        I1[m+2:m+4,0:2] = I[-1,0]          #左下角小矩阵填充
        I1[m+2:m+4,n+2:n+4] = I[-1,-1]     #右下角小矩阵填充    
    #掩膜计算
    for i in range(2,m+2):
        for j in range(2,n+2):
            #3*3正方形掩膜
            mean=[]
            var=[]
            A1=I1[(i-1):(i+1),(j-1):(j+1)]
            mean.append(np.mean(A1))
            var.append(np.var(A1))      
            #五边形掩膜-1（上）
            A2=[I1[i-2,j-1],I1[i-2,j],I1[i-1,j+1],I1[i-1,j-1],I1[i-1,j],I1[i-1,j+1],I1[i,j]]
            mean.append(np.mean(A2))
            var.append(np.var(A2))
            #五边形掩膜-2（下）
            A3=[I1[i+2,j-1],I1[i+2,j],I1[i+1,j+1],I1[i+1,j-1],I1[i+1,j],I1[i+1,j+1],I1[i,j]]
            mean.append(np.mean(A3))
            var.append(np.var(A3))
            #五边形掩膜-3（左）
            A4=[I1[i-1,j-2],I1[i,j-2],I1[i+1,j-2],I1[i-1,j-1],I1[i,j-1],I1[i+1,j-1],I1[i,j]]
            mean.append(np.mean(A4))
            var.append(np.var(A4))
            #五边形掩膜-4（右）
            A5=[I1[i-1,j+2],I1[i,j+2],I1[i+1,j+2],I1[i-1,j+1],I1[i,j+1],I1[i+1,j+1],I1[i,j]]
            mean.append(np.mean(A5))
            var.append(np.var(A5))
            #六边形掩膜-1（左上）
            A6=[I1[i-2,j-2],I1[i-1,j-2],I1[i-2,j-1],I1[i-1,j-1],I1[i,j-1],I1[i-1,j],I1[i,j]]
            mean.append(np.mean(A6))
            var.append(np.var(A6))
            #六边形掩膜-1（右上）
            A7=[I1[i-2,j+2],I1[i-1,j+2],I1[i-2,j+1],I1[i-1,j+1],I1[i,j+1],I1[i-1,j],I1[i,j]]
            mean.append(np.mean(A7))
            var.append(np.var(A7))
            #六边形掩膜-1（左下）
            A8=[I1[i+2,j-2],I1[i+1,j-2],I1[i+2,j-1],I1[i+1,j-1],I1[i,j-1],I1[i+1,j],I1[i,j]]
            mean.append(np.mean(A8))
            var.append(np.var(A8))
            #六边形掩膜-1（右下）
            A9=[I1[i+2,j+2],I1[i+1,j+2],I1[i+2,j+1],I1[i+1,j+1],I1[i,j+1],I1[i+1,j],I1[i,j]]
            mean.append(np.mean(A9))
            var.append(np.var(A9))
            #提取最小方差掩膜的均值
            a=var.index(min(var))
            img[i-2,j-2]=mean[a]            
    return np.array(img,dtype='uint8')


