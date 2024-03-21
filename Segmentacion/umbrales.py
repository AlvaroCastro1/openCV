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

def umbral_por2puntos(imagen, umbral_valor1, umbral_valor2):
    alto, ancho = imagen.shape
    salida = np.zeros_like(imagen)
    for i in range(alto):
        for j in range(ancho):
            if imagen[i, j] <= umbral_valor1 and imagen[i, j] >= umbral_valor2:
                salida[i, j] = 0
            else:
                salida[i, j] = imagen[i,j]
    return salida

def umbral_por2puntos_invertido(imagen, umbral_valor1, umbral_valor2):
    alto, ancho = imagen.shape
    salida = np.zeros_like(imagen)
    for i in range(alto):
        for j in range(ancho):
            if imagen[i, j] <= umbral_valor1 and imagen[i, j] >= umbral_valor2:
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
    um_2puntos_img = umbral_por2puntos(imagen, umbral_valor, umbral_valor+100)
    um_2puntos_inv_img = umbral_por2puntos_invertido(imagen, umbral_valor, umbral_valor+100)

    import matplotlib.pyplot as plt    
    plt.figure(figsize=(10, 5))

    plt.subplot(331)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.title('imagen')
    
    plt.subplot(332)
    plt.imshow(cv2.cvtColor(umb_img, cv2.COLOR_BGR2RGB))
    plt.title('imagen')
    
    plt.subplot(333)
    plt.imshow(cv2.cvtColor(umb_inv_img, cv2.COLOR_BGR2RGB))
    plt.title('imagen')
    
    plt.subplot(334)
    plt.imshow(cv2.cvtColor(um_nivel_img, cv2.COLOR_BGR2RGB))
    plt.title('imagen')
    
    plt.subplot(335)
    plt.imshow(cv2.cvtColor(um_nivel_inv_img, cv2.COLOR_BGR2RGB))
    plt.title('imagen')
    
    plt.subplot(336)
    plt.imshow(cv2.cvtColor(um_nivel_img, cv2.COLOR_BGR2RGB))
    plt.title('imagen')
    
    plt.subplot(337)
    plt.imshow(cv2.cvtColor(um_nivel_inv_img, cv2.COLOR_BGR2RGB))
    plt.title('imagen')

    plt.subplot(338)
    plt.imshow(cv2.cvtColor(um_2puntos_img, cv2.COLOR_BGR2RGB))
    plt.title('imagen')
    
    plt.subplot(339)
    plt.imshow(cv2.cvtColor(um_2puntos_inv_img, cv2.COLOR_BGR2RGB))
    plt.title('imagen')
    
    plt.show()