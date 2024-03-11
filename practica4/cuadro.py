import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

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

def multiplicar_imgEsquinaNegro(imagen_ruta: str):
    imagen = cv2.imread(imagen_ruta)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    esquina = crear_imgCuadradoEsquinaNegro(imagen_ruta)
    cv2.namedWindow("esquina", cv2.WINDOW_NORMAL)
    cv2.imshow("esquina", esquina)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return multiplicar(imagen, esquina)
    return cv2.multiply(imagen, esquina)

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

def multiplicar(imagen1, imagen2):
    # Crear una imagen vacía para el resultado
    resultado = np.zeros_like(imagen1)
    
    # Multiplicar las imágenes píxel a píxel y asegurarse de que estén en el rango de 0 a 255
    for i in range(imagen1.shape[0]):
        for j in range(imagen1.shape[1]):
            valor = imagen1[i, j] * imagen2[i, j]
            resultado[i, j] = valor
            
    return resultado

ruta_amarilla = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"

# Obtener resultados
resultado1 = multiplicar_imgEsquinaNegro(ruta_amarilla)
resultado2 = restar_imgCentroBlanco(ruta_amarilla)
resultado3 = sumar_centro130(ruta_amarilla)
resultado4 = restar_centroAleatorio_fondoNegro(ruta_amarilla)

# Mostrar los resultados en subplots
plt.figure(1)

plt.subplot(221)  # 4 filas, 1 columna, posición 1
plt.imshow(cv2.cvtColor(resultado1, cv2.COLOR_BGR2RGB))
plt.title("Imagen Esquina Negro")

plt.subplot(222)  # 4 filas, 1 columna, posición 2
plt.imshow(cv2.cvtColor(resultado2, cv2.COLOR_BGR2RGB))
plt.title("Imagen Centro Blanco")

plt.subplot(223)  # 4 filas, 1 columna, posición 3
plt.imshow(cv2.cvtColor(resultado3, cv2.COLOR_BGR2RGB))
plt.title("Centro 130 Fondo Aleatorio")

plt.subplot(224)  # 4 filas, 1 columna, posición 4
plt.imshow(cv2.cvtColor(resultado4, cv2.COLOR_BGR2RGB))
plt.title("Centro Aleatorio Fondo Negro")

plt.tight_layout()
plt.show()