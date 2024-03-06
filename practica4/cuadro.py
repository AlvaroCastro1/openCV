import cv2
import numpy as np
import random

def crear_imgCuadradoEsquinaNegro(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Dimensiones de la imagen
    alto, ancho = imagen.shape
    tamano = random.randint(10, ancho-10)
    esquinas = [(0, 0), (ancho - tamano, 0), (0, alto - tamano), (ancho - tamano, alto - tamano)]

    esquina_aleatoria = random.choice(esquinas)

    # Color aleatorio del cuadrado (en formato BGR)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Dibujar el cuadrado en la imagen
    cv2.rectangle(imagen, esquina_aleatoria, (esquina_aleatoria[0] + tamano, esquina_aleatoria[1] + tamano), color, -1)
    return imagen

def crear_imgCentroBlanco(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagen_centroBlanco = np.zeros_like(imagen, dtype=np.uint8)
    
    alto, ancho = imagen.shape
    
    x_cuadrado = ancho // 4
    y_cuadrado = alto // 4

    # Color del cuadrado (en formato BGR)
    cv2.rectangle(imagen_centroBlanco, (x_cuadrado, y_cuadrado), (3*x_cuadrado, 3*y_cuadrado), (255, 255, 255), -1)
    return imagen_centroBlanco

def restar_imgCentroBlanco(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    centro = crear_imgCentroBlanco(imagen_ruta)
    return cv2.subtract(imagen, centro)

def crear_centro130_fondoAleatorio(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    r = random.randint(0, 255)
    imagen_fondoBlanco_centroNegro = np.ones_like(imagen, dtype=np.uint8) * r
    largo, ancho = imagen.shape

    for i in range(largo//4, 3 * largo//4 ,1):
        for j in range(ancho//4, 3 * ancho//4, 1):
            imagen_fondoBlanco_centroNegro[i,j] = 130
    imagen_fondoBlanco_centroNegro = cv2.cvtColor(imagen_fondoBlanco_centroNegro, cv2.COLOR_GRAY2BGR)
    return imagen_fondoBlanco_centroNegro

def sumar_centro130(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)

    imagen_fondoAleatorio_centro130 = crear_centro130_fondoAleatorio(imagen_ruta)

    return cv2.add(imagen, imagen_fondoAleatorio_centro130)

def crear_centroAleatorio_fondoNegro(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    imagen_fondoBlanco_centroNegro = np.zeros_like(imagen, dtype=np.uint8)
    largo, ancho = imagen.shape

    for i in range(largo//4, 3 * largo//4 ,1):
        for j in range(ancho//4, 3 * ancho//4, 1):
            imagen_fondoBlanco_centroNegro[i,j] = random.randint(0, 255)
    imagen_fondoBlanco_centroNegro = cv2.cvtColor(imagen_fondoBlanco_centroNegro, cv2.COLOR_GRAY2BGR)
    return imagen_fondoBlanco_centroNegro

def restar_centroAleatorio_fondoNegro(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)

    imagen_centroAleatorio_fondoNegro = crear_centroAleatorio_fondoNegro(imagen_ruta)

    return cv2.subtract(imagen, imagen_centroAleatorio_fondoNegro)

resultado = restar_centroAleatorio_fondoNegro("C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png")
print(resultado.shape)
cv2.namedWindow('Imagen resulatado', cv2.WINDOW_NORMAL)
cv2.imshow("Imagen resulatado", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()