import cv2
from suma import sum_images
from resta import rest_images
from multi import multiplicar_imagen
from division import division_imagen

img1 = "C:/Users/Hp245-User/Desktop/openCV/images/LC1.jpeg"
img2 = "C:/Users/Hp245-User/Desktop/openCV/images/lenacolor.png"

imagen1 = cv2.imread(img1)
imagen2 = cv2.imread(img2)

imagen1 = cv2.resize(imagen1, (300, 300))
imagen2 = cv2.resize(imagen2, (300, 300))

# crear ventana
cv2.namedWindow("Imagen 1 y 2", cv2.WINDOW_NORMAL)

# concatenar horizontalmente
imagenes = cv2.hconcat([imagen1, imagen2])

cv2.imshow("Imagen 1 y 2", imagenes)

"""
modos para poder hacer la operacion
truncar
ciclico
promedio
"""

resultado = sum_images(img1, img2,"promedio")
cv2.imshow('Imagen Suma', resultado)

# resultado = rest_images(img2, img1,"promedio")
# cv2.imshow('Imagen Resta', resultado)

# resultado = multiplicar_imagen(img1, 100,"promedio")
# cv2.imshow('Imagen Multiplicacion', resultado)

resultado = division_imagen(img1, 1,"truncar")
cv2.imshow('Imagen division', resultado)


cv2.waitKey(0)
cv2.destroyAllWindows()