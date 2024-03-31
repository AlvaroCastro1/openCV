import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import tkinter as tk
from tkinter import filedialog

class ImageManipulator:
    def espejo_horizontal(self, original_image):
        imagen_espejo = np.zeros_like(original_image)
        height, width, _ = original_image.shape
        for i in range(height):
            imagen_espejo[i, :] = original_image[height - 1 - i, :]
        return imagen_espejo

    def espejo_vertical(self, original_image):
        imagen_espejo = np.zeros_like(original_image)
        height, width, _ = original_image.shape
        for i in range(width):
            imagen_espejo[:, i] = original_image[:, width - 1 - i]
        return imagen_espejo

    def espejo_diagonal(self, original_image):
        imagen_espejo = np.zeros_like(original_image)
        height, width, _ = original_image.shape
        for i in range(height):
            for j in range(width):
                imagen_espejo[i, j] = original_image[height - 1 - i, width - 1 - j]
        return imagen_espejo

    def mostrar_imagenes(self, original, horizontal, vertical, diagonal):
        plt.figure(figsize=(10, 10))

        # Mostrar la imagen original
        plt.subplot(2, 2, 1)
        plt.imshow(original)
        plt.title('Imagen Original')
        plt.axis('off')
        # Mostrar el espejo vertical
        plt.subplot(2, 2, 2)
        plt.imshow(vertical)
        plt.title('Espejo 1')
        plt.axis('off')

        # Mostrar el espejo horizontlS
        plt.subplot(2, 2, 3)
        plt.imshow(horizontal)
        plt.title('Espejo 2')
        plt.axis('off')

        # Mostrar el espejo diagonal
        plt.subplot(2, 2, 4)
        plt.imshow(diagonal)
        plt.title('Espejo 3')
        plt.axis('off')

        plt.show()


    def save_images(self, vertical):
        key = cv2.waitKey(0)
        if key == ord('s'):
            root = tk.Tk()
            root.withdraw()
       
            ruta_guardado = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        
            if ruta_guardado:
                cv2.imwrite(ruta_guardado + '_espejo_vertical.jpg', vertical)
        
if __name__ == "__main__": 
   
    image_manipulator = ImageManipulator()

    original_image = cv2.imread('lorito.png')

    imagen_espejo_horizontal = image_manipulator.espejo_horizontal(original_image)
    imagen_espejo_vertical = image_manipulator.espejo_vertical(original_image)
    imagen_espejo_diagonal = image_manipulator.espejo_diagonal(original_image)

    image_manipulator.mostrar_imagenes(original_image, imagen_espejo_horizontal, imagen_espejo_vertical, imagen_espejo_diagonal)

    image_manipulator.save_images(original_image, imagen_espejo_horizontal, imagen_espejo_vertical, imagen_espejo_diagonal)
