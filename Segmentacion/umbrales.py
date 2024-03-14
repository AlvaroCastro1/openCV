import cv2
import numpy as np


def umbral(imagen, umbral_valor):
    alto, ancho = imagen.shape
    salida = np.zeros_like(imagen)
    for i in range(alto):
        for j in range(ancho):
            if imagen[i, j] >= umbral_valor:
                salida[i, j] = 255
            else:
                salida[i, j] = 0
    return salida

def umbral_invertido(imagen, umbral_valor):
    alto, ancho = imagen.shape
    salida = np.zeros_like(imagen)
    for i in range(alto):
        for j in range(ancho):
            if imagen[i, j] >= umbral_valor:
                salida[i, j] = 0
            else:
                salida[i, j] = 255
    return salida

def umbral_porNivel(imagen, umbral_valor):
    alto, ancho = imagen.shape
    salida = np.zeros_like(imagen)
    for i in range(alto):
        for j in range(ancho):
            if imagen[i, j] >= umbral_valor:
                salida[i, j] = 0
            else:
                salida[i, j] = imagen[i,j]
    return salida

def umbral_porNivel_invertido(imagen, umbral_valor):
    alto, ancho = imagen.shape
    salida = np.zeros_like(imagen)
    for i in range(alto):
        for j in range(ancho):
            if imagen[i, j] >= umbral_valor:
                salida[i, j] = imagen[i,j]
            else:
                salida[i, j] = 0
    return salida

if __name__ == "__main__":
    imagen = cv2.imread('c:/Users/Hp245-User/Desktop/openCV/images/amarilla.png')
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # umbral_valor = int(input("Ingrese un valor de umbral (0-255): "))
    umbral_valor = 100

    umb_img = umbral(imagen, umbral_valor)
    umb_inv_img = umbral_invertido(imagen, umbral_valor)
    um_nivel_img = umbral_porNivel(imagen, umbral_valor)
    um_nivel_inv_img = umbral_porNivel_invertido(imagen, umbral_valor)

    import matplotlib.pyplot as plt    
    plt.figure(figsize=(10, 5))

    plt.subplot(231)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('Umbral')

    plt.subplot(232)
    plt.imshow(cv2.cvtColor(umb_img, cv2.COLOR_BGR2RGB))
    plt.title('Umbral')
    
    plt.subplot(233)
    plt.imshow(cv2.cvtColor(umb_inv_img, cv2.COLOR_BGR2RGB))
    plt.title('Umbral inv')
    
    plt.subplot(234)
    plt.imshow(cv2.cvtColor(um_nivel_img, cv2.COLOR_BGR2RGB))
    plt.title('Umbral por nivel')
    
    plt.subplot(235)
    plt.imshow(cv2.cvtColor(um_nivel_inv_img, cv2.COLOR_BGR2RGB))
    plt.title('Umbral por nivel inv')

    plt.show()