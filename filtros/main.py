import cv2

from media import filtro_media
from mediana import filtro_mediana

# carga la imagen usando OpenCV
imagen_original = cv2.imread('C:/Users/Hp245-User/Desktop/openCV/images/ruido1.jpg')
imagen_original = cv2.cvtColor(imagen_original, cv2.COLOR_RGB2GRAY)

tamano_kernel = 3
imagen_filtrada_personalizada_mediana = filtro_mediana(imagen_original, tamano_kernel)

# funcion de openCV
imagen_filtrada_opencv_mediana = cv2.medianBlur(imagen_original, tamano_kernel)


imagen_filtrada_personalizada_media = filtro_media(imagen_original, tamano_kernel)

# funcion de openCV
imagen_filtrada_opencv_media = cv2.blur(imagen_original, (tamano_kernel, tamano_kernel))

cv2.imshow('Imagen Original', imagen_original)
cv2.imshow('Pe media', imagen_filtrada_personalizada_media)
cv2.imshow('CV media', imagen_filtrada_opencv_media)
cv2.imshow('Pe mediana', imagen_filtrada_personalizada_mediana)
cv2.imshow('CV mediana', imagen_filtrada_opencv_mediana)
cv2.waitKey(0)
cv2.destroyAllWindows()