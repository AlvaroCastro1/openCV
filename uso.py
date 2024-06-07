import cv2
import numpy as np

# Ruta de la imagen original
ruta_imagen = "images/S.png"

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)

# Obtener dimensiones de la imagen original
alto, ancho = imagen.shape[:2]

# Redimensionar la imagen a la mitad
escala = 0.5
nueva_dim = (int(ancho * escala), int(alto * escala))
imagen_reducida = cv2.resize(imagen, nueva_dim, interpolation=cv2.INTER_AREA)

# Rotar la imagen 45 grados a la derecha
centro = (nueva_dim[0] // 2, nueva_dim[1] // 2)
matriz_rotacion = cv2.getRotationMatrix2D(centro, -45, 1.0)
imagen_rotada = cv2.warpAffine(imagen_reducida, matriz_rotacion, nueva_dim)

# Crear un fondo blanco del mismo tamaño que la imagen original
fondo = np.zeros((alto, ancho, 3), dtype=np.uint8)

# Calcular las coordenadas para centrar la imagen rotada en el fondo
x_offset = (ancho - nueva_dim[0]) // 2
y_offset = (alto - nueva_dim[1]) // 2

# Colocar la imagen rotada en el fondo
fondo[y_offset:y_offset + nueva_dim[1], x_offset:x_offset + nueva_dim[0]] = imagen_rotada

# Guardar la imagen resultante
ruta_imagen_resultante = "imagen_resultante.jpg"
cv2.imwrite(ruta_imagen_resultante, fondo)

print('Imagen resultante guardada como', ruta_imagen_resultante)
