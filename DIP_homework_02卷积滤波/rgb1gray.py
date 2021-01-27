import numpy as np
def rgb1gray(f,method='NTSC'):
    if method=='average':
        
        g=f[:,:,0]/3+f[:,:,1]/3+f[:,:,2]/3
        return np.array(g,dtype='uint8')
    if method=='NTSC':
        R=0.2989
        G=0.5870
        B=0.1140
        g=(R*f[:,:,0]+G*f[:,:,1]+B*f[:,:,2])
        return np.array(g,dtype='uint8')