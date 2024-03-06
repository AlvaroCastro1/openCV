import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def colorear_franjas(imagen):
    img = cv2.imread(imagen)
    alto, ancho, _ = img.shape
    nueva_img = np.zeros_like(img)
    
    for y in range(0, alto, 30):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for dy in range(min(10, alto - y)):
            nueva_img[y + dy:y + dy + 1, :] = color
        for dy in range(min(20, alto - (y + 10))):
            nueva_img[y + 10 + dy:y + 10 + dy + 1, :] = img[y + 10 + dy:y + 10 + dy + 1, :]
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # Creamos una figura con dos subtramas
    axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Mostramos la imagen original en la primera subtrama
    axes[0].set_title('Imagen original')
    axes[0].axis('off')  # Desactivamos los ejes
    axes[1].imshow(cv2.cvtColor(nueva_img, cv2.COLOR_BGR2RGB))  # Mostramos la imagen coloreada en la segunda subtrama
    axes[1].set_title('Imagen coloreada')
    axes[1].axis('off')  # Desactivamos los ejes
    plt.tight_layout()  # Ajustamos automáticamente el diseño de las subtramas
    plt.show()

if __name__ == "__main__":
    imagen = 'C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png'
    colorear_franjas(imagen)
