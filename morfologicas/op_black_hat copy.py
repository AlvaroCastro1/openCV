"""
resalta las regiones oscuras
se resta la imagen original de la imagen cerrada

cerrada 1ro dilatacion 2do erosion
"""
import cv2
import numpy as np

def dilation(image, kernel):
    """Dilatación de la imagen utilizando un kernel dado."""
    output = np.zeros_like(image)
    image_padded = np.pad(image, ((1,1),(1,1)), mode='constant', constant_values=0) # Padding con valores negros
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

def erosion(image, kernel):
    """Erosión de la imagen utilizando un kernel dado."""
    output = np.zeros_like(image)
    image_padded = np.pad(image, ((1,1),(1,1)), mode='constant', constant_values=255) # Padding con valores blancos
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

def closing(image, kernel_size):
    """Operación de cierre: dilatación seguida de erosión."""
    kernel = np.ones((kernel_size, kernel_size), np.uint8)  # Kernel de tamaño especificado
    return erosion(dilation(image, kernel), kernel)

def black_hat(image, kernel_size):
    """Operador Black Hat."""
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image = image

    closed_image = closing(image, kernel_size)
    return cv2.subtract(closed_image, image)

if __name__ == "__main__":
    # Carga la imagen
    imagen = cv2.imread("/home/alvaro/Público/openCV/images/black_hat.jpg")

    # Define el tamaño del kernel
    kernel_size = 3

    # Aplica el operador Black Hat
    black_hat_image = black_hat(imagen, kernel_size)

    # Muestra la imagen original y el resultado
    cv2.imshow('Original', imagen)
    cv2.imshow('Black Hat', black_hat_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
