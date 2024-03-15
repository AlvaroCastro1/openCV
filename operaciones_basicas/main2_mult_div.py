import cv2
from suma import sum_images
from resta import rest_images
from multi import multiplicar_imagen
from division import division_imagen

img1 = "C:/Users/Hp245-User/Desktop/openCV/images/lc3.tiff"

imagen1 = cv2.imread(img1)

imagen1 = cv2.resize(imagen1, (300, 300))

import matplotlib.pyplot as plt

# Crear un subplot
plt.figure(figsize=(10, 5))

# Mostrar la primera imagen
plt.subplot(1, 1, 1)
plt.imshow(cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB))
plt.title('Imagen 1')

# Mostrar el subplot
plt.show()


"""
modos para poder hacer la operacion
truncar
ciclico
promedio
"""

multi_truncar = multiplicar_imagen(imagen1, 3,"truncar")
multi_ciclico = multiplicar_imagen(imagen1, 3,"ciclico")
multi_promedio = multiplicar_imagen(imagen1, 3,"promedio")

divi_truncar = division_imagen(imagen1, 3,"truncar")
divi_ciclico = division_imagen(imagen1, 3,"ciclico")
divi_promedio = division_imagen(imagen1, 3,"promedio")

plt.figure(figsize=(10, 5))


plt.subplot(231)
plt.imshow(cv2.cvtColor(multi_truncar, cv2.COLOR_BGR2RGB))
plt.title('truncar *')

plt.subplot(232)
plt.imshow(cv2.cvtColor(multi_ciclico, cv2.COLOR_BGR2RGB))
plt.title('ciclico *')

plt.subplot(233)
plt.imshow(cv2.cvtColor(multi_promedio, cv2.COLOR_BGR2RGB))
plt.title('promedio *')

plt.subplot(234)
plt.imshow(cv2.cvtColor(divi_truncar, cv2.COLOR_BGR2RGB))
plt.title('truncar /')

plt.subplot(235)
plt.imshow(cv2.cvtColor(divi_ciclico, cv2.COLOR_BGR2RGB))
plt.title('ciclico /')

plt.subplot(236)
plt.imshow(cv2.cvtColor(divi_promedio, cv2.COLOR_BGR2RGB))
plt.title('promedio /')

plt.show()