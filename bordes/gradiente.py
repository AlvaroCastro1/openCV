import cv2
import numpy as np

def detectar_bordes(imagen_gris, umbral=5):
    # Definir las máscaras de Sobel
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])

    # Aplicar las máscaras de Sobel para calcular las derivadas en las direcciones x e y
    gradiente_x = cv2.filter2D(imagen_gris, -1, sobel_x)
    gradiente_y = cv2.filter2D(imagen_gris, -1, sobel_y)

    # Calcular la magnitud del gradiente no poner **2 mantiene la imagen en negro y no se veeeee
    magnitud_gradiente = np.sqrt(gradiente_x + gradiente_y)

    # Crear una imagen para almacenar los bordes detectados
    bordes_detectados = np.zeros_like(imagen_gris)

    # Iterar sobre los píxeles y aplicar el umbral para detectar los bordes
    for i in range(imagen_gris.shape[0]):
        for j in range(imagen_gris.shape[1]):
            if magnitud_gradiente[i, j] > umbral:
                bordes_detectados[i, j] = 255

    return gradiente_x, gradiente_y, bordes_detectados

if __name__ == "__main__":
    # Leer la imagen en escala de grises
    imagen_gris = cv2.imread('hoja.jpg', cv2.IMREAD_GRAYSCALE)

    gradiente_x, gradiente_y, bordes_detectados = detectar_bordes(imagen_gris)

    # Mostrar los resultados
    cv2.imshow('Gradiente X', gradiente_x)
    cv2.imshow('Gradiente Y', gradiente_y)
    cv2.imshow('Bordes Detectados', bordes_detectados)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


   
