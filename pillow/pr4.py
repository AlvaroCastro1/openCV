import numpy as np
import matplotlib.pyplot as plt

#Config para imagenes en gris
plt.rcParams['image.cmap'] = 'gray'

img1 = np.zeros((20,30))    #Para escala de grisesq

#print( img1.shape)
img1[5:12, 10:20] = 255
plt.subplot(121)
plt.imshow(img1, vmin=0, vmax=1)
#plt.show()

img2 = np.ones( (20,30) )
img2[5:12, 10:20] = 0
plt.subplot(122)
plt.imshow(img2, vmin=0, vmax=1)
plt.show()
