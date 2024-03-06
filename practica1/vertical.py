import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def colorear_franjas(imagen):
    img = cv2.imread(imagen)
    height, width, _ = img.shape
    imagen_franjas = img.copy()

    n = 3
    inicio = 0
    fin = 2**n + 2**n

    while fin <= width:
        color_franja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        print(f"2^{n}={2**n}")
        imagen_franjas[:, inicio:inicio+2**n] = color_franja
        print(f"incian desde {inicio} hasta {inicio+2**n}")
        n +=1
        inicio=fin
        fin = inicio + 2**n + 2**n



    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Imagen original')
    axes[0].axis('off')
    axes[1].imshow(cv2.cvtColor(imagen_franjas, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Imagen coloreada')
    axes[1].axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    imagen = 'C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png'
    print(cv2.imread(imagen).shape)
    colorear_franjas(imagen)
