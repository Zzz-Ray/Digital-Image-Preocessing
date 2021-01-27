import numpy as np
import matplotlib.pyplot as plt
import CutImage as CI
a=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
    [0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0],
    [0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],dtype='bool')
a1=CI.Cut(a)
plt.figure()
plt.subplot(121)
plt.title('Original Image')
plt.axis('off')
plt.imshow(a)
plt.subplot(122)
plt.imshow(a1)
plt.title('After Cutting')
plt.axis('off')
plt.savefig('Cut_test.jpg')
