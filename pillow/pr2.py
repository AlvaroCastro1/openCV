import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("kodim23.png")

print( img.shape )
print( img.size )   # tamaño de la imagen

red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]
print("Rojo: ", red.shape )
print("Verde: ", green.shape )
print("Azul: ", blue.shape )

plt.figure(1)
plt.subplot(221)
plt.imshow(img)
plt.title("RGB")

plt.subplot(222)
plt.imshow(red)
plt.title("Rojo")
#plt.axis("off")

plt.subplot(223)
plt.imshow(green)
plt.title("Verde")

plt.subplot(224)
plt.imshow(blue)
plt.title("Azul")
plt.show()


plt.imshow(green, cmap="gray")
plt.title("Verde")
plt.axis("off")
plt.show()

#Obtener histograma. ravel regresa un arreglo continuo
plt.hist( red.ravel(), bins=256 )  #8by
plt.title("Rojo 256")
plt.show()

plt.hist( red.ravel(), bins=128 ) #6
plt.title("Rojo 128")
plt.show()

plt.hist( red.ravel(), bins=64 ) #4
plt.title("Rojo 64")
plt.show()
