import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import cv2

class Espejo_transformar:
    def espejo_horizontal(self, original_image):
        height, width = original_image.shape[:2]
        imagen_espejo = np.zeros_like(original_image)
        for i in range(height):
            imagen_espejo[i, :] = original_image[height - 1 - i, :]
        return imagen_espejo

    def espejo_vertical(self, original_image):
        height, width = original_image.shape[:2]
        imagen_espejo = np.zeros_like(original_image)
        for i in range(width):
            imagen_espejo[:, i] = original_image[:, width - 1 - i]
        return imagen_espejo

    def espejo_diagonal(self, original_image):
        height, width = original_image.shape[:2]
        imagen_espejo = np.zeros_like(original_image)
        for i in range(height):
            for j in range(width):
                imagen_espejo[i, j] = original_image[height - 1 - i, width - 1 - j]
        return imagen_espejo

    def convertir_a_grises(self, image):
        # Convertir a escala de grises
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def mostrar_imagenes(self, original, horizontal, vertical, diagonal):
        plt.figure(figsize=(10, 10))

        # Mostrar la imagen original
        plt.subplot(2, 2, 1)
        plt.imshow(original, cmap='gray')
        plt.title('Imagen Original')
        plt.axis('off')

        # Mostrar el espejo vertical
        plt.subplot(2, 2, 2)
        plt.imshow(vertical, cmap='gray')
        plt.title('Espejo Horizontal')
        plt.axis('off')

        # Mostrar el espejo horizonatl
        plt.subplot(2, 2, 3)
        plt.imshow(horizontal, cmap='gray')
        plt.title('Espejo Vertical')
        plt.axis('off')

        # Mostrar el espejo diagonal
        plt.subplot(2, 2, 4)
        plt.imshow(diagonal, cmap='gray')
        plt.title('Espejo Diagonal')
        plt.axis('off')

        plt.show()

    def save_images(self, original, horizontal, vertical, diagonal):
        mpimg.imsave('imagen_original.jpg', original, cmap='gray')
        mpimg.imsave('espejo_horizontal.jpg', horizontal, cmap='gray')
        mpimg.imsave('espejo_vertical.jpg', vertical, cmap='gray')
        mpimg.imsave('espejo_diagonal.jpg', diagonal, cmap='gray')

if __name__ == "__main__": 
    espejo_transformar = Espejo_transformar()
    original_image = cv2.imread('lorito.png')

    # Convertir a escala de grises
    original_grayscale = espejo_transformar.convertir_a_grises(original_image)

    horizontal_image = espejo_transformar.espejo_horizontal(original_grayscale)
    vertical_image = espejo_transformar.espejo_vertical(original_grayscale)
    diagonal_image = espejo_transformar.espejo_diagonal(original_grayscale)

    espejo_transformar.mostrar_imagenes(original_grayscale, horizontal_image, vertical_image, diagonal_image)
    espejo_transformar.save_images(original_grayscale, horizontal_image, vertical_image, diagonal_image)
