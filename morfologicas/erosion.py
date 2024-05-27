import cv2
import numpy as np

if __name__ == '__main__':
    img_binaria = cv2.imread('imagen.png', cv2.IMREAD_GRAYSCALE)
    # Mostrar la imagen original
    cv2.imshow('Imagen Binaria Original', img_binaria)
    
    # Define el kernel de erosión (tamaño y forma del área de vecindad)
    kernel = np.ones((3,3), np.uint8)  # Kernel cuadrado de 3x3

    # Dimensiones de la imagen
    alto, ancho = img_binaria.shape

    # Inicializar una nueva matriz para la imagen erosionada
    img_erosionada = np.zeros_like(img_binaria)

    # Aplicar erosión
    for y in range(1, alto - 1):
        for x in range(1, ancho - 1):
            # Obtener la submatriz de la imagen binaria del tamaño del kernel
            submatriz = img_binaria[y-1:y+2, x-1:x+2]
            # Verificar si todos los píxeles en la vecindad son blancos (255)
            if np.min(submatriz * kernel) == 255:
                img_erosionada[y, x] = 255

    # Mostrar la imagen erosionada
    cv2.imshow('Imagen Binaria Erosionada', img_erosionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

