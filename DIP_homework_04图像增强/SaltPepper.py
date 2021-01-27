import numpy as np
#椒盐噪声函数
def sp_noise(img,snr=0.9):
    #img:原图像；snr：信噪比
    m,n=img.shape
    img1=img.copy()      # 复制原图形模板
    sp=m*n               # 计算图像像素点个数
    NP=int(sp*(1-snr))   # 计算图像椒盐噪声点个数
    for i in range (NP):
        x=np.random.randint(1,m-1)   # 生成一个 1 至 m-1 之间的随机整数
        y=np.random.randint(1,n-1)   # 生成一个 1 至 n-1 之间的随机整数
        if np.random.random()<=0.5:  #随机生成一个 0 至 1 之间的浮点数
            img1[x,y]=0              #椒噪声（黑色）
        else:
            img1[x,y]=255            #盐噪声（白色）
    return img1
