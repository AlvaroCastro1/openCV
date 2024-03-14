import cv2
from suma import sum_images
from resta import rest_images
from multi import multiplicar_imagen
from division import division_imagen

img1 = "C:/Users/Hp245-User/Desktop/openCV/images/lc3.tiff"
img2 = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"

imagen1 = cv2.imread(img1)
imagen2 = cv2.imread(img2)

imagen1 = cv2.resize(imagen1, (300, 300))
imagen2 = cv2.resize(imagen2, (300, 300))

imagenes = cv2.hconcat([imagen1, imagen2])

import matplotlib.pyplot as plt

# Crear un subplot
plt.figure(figsize=(10, 5))

# Mostrar la primera imagen
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB))
plt.title('Imagen 1')
plt.axis('off')

# Mostrar la segunda imagen
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB))
plt.title('Imagen 2')
plt.axis('off')

# Mostrar el subplot
plt.show()


"""
modos para poder hacer la operacion
truncar
ciclico
promedio
"""

suma_truncar = sum_images(img1, img2,"truncar")
suma_ciclico = sum_images(img1, img2,"ciclico")
suma_promedio = sum_images(img1, img2,"promedio")

resta_truncar = rest_images(img1, img2,"truncar")
resta_ciclico = rest_images(img1, img2,"ciclico")
resta_promedio = rest_images(img1, img2,"promedio")

plt.figure(figsize=(10, 5))


plt.subplot(231)
plt.imshow(suma_truncar)
plt.title('truncar +')
plt.axis('off')

plt.subplot(232)
plt.imshow(suma_ciclico)
plt.title('ciclico +')
plt.axis('off')

plt.subplot(233)
plt.imshow(cv2.cvtColor(suma_promedio, cv2.COLOR_BGR2RGB))
plt.title('promedio +')
plt.axis('off')

plt.subplot(234)
plt.imshow(cv2.cvtColor(resta_truncar, cv2.COLOR_BGR2RGB))
plt.title('truncar -')
plt.axis('off')

plt.subplot(235)
plt.imshow(cv2.cvtColor(resta_ciclico, cv2.COLOR_BGR2RGB))
plt.title('ciclico -')
plt.axis('off')

plt.subplot(236)
plt.imshow(resta_promedio)
plt.title('promedio -')
plt.axis('off')

plt.show()