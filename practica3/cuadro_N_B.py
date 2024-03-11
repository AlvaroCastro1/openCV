import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def crear_imgCentroNegro(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # alto, ancho = imagen.shape
    imagen_fondoBlanco_centroNegro = np.ones_like(imagen, dtype=np.uint8) * 255
    largo, ancho = imagen.shape

    for i in range(largo//4, 3 * largo//4 ,1):
        for j in range(ancho//4, 3 * ancho//4, 1):
            imagen_fondoBlanco_centroNegro[i,j] = 0
    return imagen_fondoBlanco_centroNegro

def crear_imgCentroBlanco(imagen_ruta: str):
    imagen = crear_imgCentroNegro(imagen_ruta)
    return 255 - imagen

def sumar_centroNegro(imagen_ruta: str):

    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Imagen a gris", imagen)
    imagen_fondoBlanco_centroNegro = crear_imgCentroNegro(imagen_ruta)

    return cv2.add(imagen, imagen_fondoBlanco_centroNegro)

def sumar_centroBlanco(imagen_ruta: str):

    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    imagen_fondoNegro_centroBlanco = crear_imgCentroBlanco(imagen_ruta)

    return cv2.add(imagen, imagen_fondoNegro_centroBlanco)

def restar_centroNegro(imagen_ruta: str):

    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Imagen a gris", imagen)
    imagen_fondoBlanco_centroNegro = crear_imgCentroNegro(imagen_ruta)

    return cv2.subtract(imagen, imagen_fondoBlanco_centroNegro)

def restar_centroBlanco(imagen_ruta: str):

    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    imagen_fondoNegro_centroBlanco = crear_imgCentroBlanco(imagen_ruta)

    return cv2.subtract(imagen, imagen_fondoNegro_centroBlanco)

def crear_centro130_fondoAleatorio(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    r = random.randint(0, 255)
    imagen_fondoBlanco_centroNegro = np.ones_like(imagen, dtype=np.uint8) * r
    largo, ancho = imagen.shape

    for i in range(largo//4, 3 * largo//4 ,1):
        for j in range(ancho//4, 3 * ancho//4, 1):
            imagen_fondoBlanco_centroNegro[i,j] = 130
    return imagen_fondoBlanco_centroNegro

def sumar130_fAleatorio(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)

    imagen_fondoAleatorio_centro130 = crear_centro130_fondoAleatorio(imagen_ruta)
    imagen_fondoAleatorio_centro130 = cv2.cvtColor(imagen_fondoAleatorio_centro130, cv2.COLOR_GRAY2BGR)
    return cv2.add(imagen, imagen_fondoAleatorio_centro130)

def crear_centroAleatorio_fondoNegro(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    imagen_fondoBlanco_centroNegro = np.zeros_like(imagen, dtype=np.uint8)
    largo, ancho = imagen.shape

    for i in range(largo//4, 3 * largo//4 ,1):
        for j in range(ancho//4, 3 * ancho//4, 1):
            imagen_fondoBlanco_centroNegro[i,j] = random.randint(0, 255)
    return imagen_fondoBlanco_centroNegro

def restar_CAleatorio(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)

    imagen_fondoNegro_centroAleatorio = crear_centroAleatorio_fondoNegro(imagen_ruta)
    imagen_fondoNegro_centroAleatorio = cv2.cvtColor(imagen_fondoNegro_centroAleatorio, cv2.COLOR_GRAY2BGR)

    return cv2.add(imagen, imagen_fondoNegro_centroAleatorio)


ruta_amarilla = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"

# Obtener resultados
resultado1 = sumar_centroNegro(ruta_amarilla)
resultado2 = sumar_centroBlanco(ruta_amarilla)
resultado3 = restar_centroNegro(ruta_amarilla)
resultado4 = restar_centroBlanco(ruta_amarilla)
resultado5 = sumar130_fAleatorio(ruta_amarilla)
resultado6 = restar_CAleatorio(ruta_amarilla)

# Mostrar los resultados en subplots
plt.figure(1)

plt.subplot(321)  # 3 filas, 2 columnas, posición 1
plt.imshow(cv2.cvtColor(resultado1, cv2.COLOR_BGR2RGB))
plt.title("Imagen+ Centro Negro")

plt.subplot(322)  # 3 filas, 2 columnas, posición 2
plt.imshow(cv2.cvtColor(resultado2, cv2.COLOR_BGR2RGB))
plt.title("Imagen+ Centro Blanco")

plt.subplot(323)  # 3 filas, 2 columnas, posición 3
plt.imshow(cv2.cvtColor(resultado3, cv2.COLOR_BGR2RGB))
plt.title("Imagen- Centro Negro")

plt.subplot(324)  # 3 filas, 2 columnas, posición 4
plt.imshow(cv2.cvtColor(resultado4, cv2.COLOR_BGR2RGB))
plt.title("Imagen- Centro Blanco")

plt.subplot(325)  # 3 filas, 2 columnas, posición 5
plt.imshow(cv2.cvtColor(resultado5, cv2.COLOR_BGR2RGB))
plt.title("Imagen+ Centro 130 Fondo Aleatorio")

plt.subplot(326)  # 3 filas, 2 columnas, posición 5
plt.imshow(cv2.cvtColor(resultado6, cv2.COLOR_BGR2RGB))
plt.title("Imagen- Centro Aleatorio")

print(resultado1.shape)
print(resultado2.shape)
print(resultado3.shape)
print(resultado4.shape)
print(resultado5.shape)
print(resultado6.shape)

plt.tight_layout()
plt.show()