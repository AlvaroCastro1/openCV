import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("kodim23.png")

print( type(img) )

plt.subplot(211)        # The subplot() command specifies numrows, numcols, plot_number
                        # where plot_number ranges from 1 to numrows*numcols.
plt.imshow( img )
#plt.show()                 # The show() command blocks the input of additional
                            # commands until you manually kill the plot window.

plt.subplot(212)
opr = img ** 0.5
opr = np.cos(img)
plt.imshow( opr )
plt.show()

corte = img[0:400, 0:200]   #[x1:x2 , y1:y2]  #F, C
plt.imshow(corte)
plt.show()

plt.imsave("Corte1.png", corte)
