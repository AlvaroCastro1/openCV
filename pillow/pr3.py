import numpy as np
import matplotlib.pyplot as plt

# #Config para imagenes en gris
# plt.rcParams['image.cmap'] = 'gray'

img1 = np.zeros((20,30, 3))    #Para escala de grisesq

print( img1.shape )

img1[5:12, 10:20] = (20,20,2)

img1[6:7, 16:17] = 0
img1[6:7, 12:13] = 0


img1[10:11, 12:18] = 0

plt.imshow(img1, vmin=0, vmax=1)
plt.show()
