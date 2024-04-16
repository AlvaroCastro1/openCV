"""
para resaltar regiones brillantes más pequeñas en una imagen
se resta la imagen original de la imagen abierta

abierta 1ro erosion 2do dilatacion
"""
import cv2
import numpy as np

def erosion(image, kernel):
    """Erosión de la imagen utilizando un kernel dado."""
    output = np.zeros_like(image)
    # Rellena la imagen con valores blancos para evitar efectos no deseados en los bordes
    image_padded = np.pad(image, ((1,1),(1,1)), mode='constant', constant_values=255)
    # Itera sobre cada píxel de la imagen
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            # Realiza la erosión en cada píxel
            min_val = 255
            for i in range(kernel.shape[0]):
                for j in range(kernel.shape[1]):
                    if kernel[i][j] == 1:
                        min_val = min(min_val, image_padded[y+i][x+j])
            output[y,x] = min_val
    return output

def dilation(image, kernel):
    """Dilatación de la imagen utilizando un kernel dado."""
    output = np.zeros_like(image)
    # Rellena la imagen con valores negros para evitar efectos no deseados en los bordes
    image_padded = np.pad(image, ((1,1),(1,1)), mode='constant', constant_values=0)
    # Itera sobre cada píxel de la imagen
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            # Realiza la dilatación en cada píxel
            max_val = 0
            for i in range(kernel.shape[0]):
                for j in range(kernel.shape[1]):
                    if kernel[i][j] == 1:
                        max_val = max(max_val, image_padded[y+i][x+j])
            output[y,x] = max_val
    return output

def opening(image, kernel_size):
    """Operación de apertura: erosión seguida de dilatación."""
    # Crea un kernel de tamaño especificado
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    # Aplica la erosión seguida de la dilatación
    return dilation(erosion(image, kernel), kernel)

def top_hat(image, kernel_size):
    """Operador Top Hat."""
    # Convierte la imagen a escala de grises si es a color
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image = image

    # Aplica la operación de apertura
    opened_image = opening(image, kernel_size)
    # Realiza la resta entre la imagen original y la imagen abierta
    return cv2.subtract(image, opened_image)

if __name__ == "__main__":
    # Carga la imagen
    imagen = cv2.imread("/home/alvaro/Público/openCV/images/hat_image.png")

    # Define el tamaño del kernel
    kernel_size = 3

    # Aplica el operador Top Hat
    top_hat_image = top_hat(imagen, kernel_size)

    # Muestra la imagen original y el resultado
    cv2.imshow('Original', imagen)
    cv2.imshow('Top Hat', top_hat_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
