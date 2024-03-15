import cv2
import numpy as np

import cv2
import numpy as np

def traslacion(imagen, traslacion_x, traslacion_y):
    if imagen is None:
        print("No se pudo cargar la imagen")
        return None
    else:
        # Verificar si la imagen es a color o en escala de grises
        if len(imagen.shape) == 3:  # Imagen a color
            # Definir la matriz de traslación
            matriz_traslacion = np.float32([[1, 0, traslacion_x], [0, 1, traslacion_y]])

            # Aplicar la traslación a la imagen utilizando la función cv2.warpAffine()
            imagen_trasladada = cv2.warpAffine(imagen, matriz_traslacion, (imagen.shape[1], imagen.shape[0]))
        else:  # Imagen en escala de grises
            # Definir la matriz de traslación
            matriz_traslacion = np.float32([[1, 0, traslacion_x], [0, 1, traslacion_y]])

            # Aplicar la traslación a la imagen utilizando la función cv2.warpAffine()
            imagen_trasladada = cv2.warpAffine(imagen, matriz_traslacion, (imagen.shape[1], imagen.shape[0]), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=255)
        return imagen_trasladada



if __name__ == "__main__": 
    # Ruta de la imagen a cargar
    ruta_imagen = 'c:/Users/Hp245-User/Desktop/openCV/images/amarilla.png'
    imagen_color = cv2.imread(ruta_imagen)
    imagen_gris = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

    # Traslación de la imagen a color
    imagen_trasladada_color = traslacion(imagen_color, 50, 50)

    # Traslación de la imagen en escala de grises
    imagen_trasladada_gris = traslacion(imagen_gris, 50, 50)

    # Mostrar las imágenes trasladadas
    cv2.imshow('Imagen Trasladada (Color)', imagen_trasladada_color)
    cv2.imshow('Imagen Trasladada (Escala de Grises)', imagen_trasladada_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
