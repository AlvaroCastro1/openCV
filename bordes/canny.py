import numpy as np
import cv2
import matplotlib.pyplot as plt

def suavizar_imagen(imagen, kernel_size=5):
    return cv2.GaussianBlur(imagen, (kernel_size, kernel_size), 0)

def calcular_gradientes(imagen):
    sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    magnitud_gradiente = np.sqrt(sobelx**2 + sobely**2)
    direccion_gradiente = np.arctan2(sobely, sobelx)
    return magnitud_gradiente, direccion_gradiente

def suprimir_no_maximos(magnitud_gradiente, direccion_gradiente):
    altura, ancho = magnitud_gradiente.shape
    supresion = np.zeros((altura, ancho), dtype=np.float64)
    direccion_gradiente[direccion_gradiente < 0] += np.pi

    for y in range(1, altura - 1):
        for x in range(1, ancho - 1):
            angulo = direccion_gradiente[y, x]
            if (0 <= angulo < np.pi / 8) or (15*np.pi / 8 <= angulo < 2*np.pi):
                vecinos = (magnitud_gradiente[y, x-1], magnitud_gradiente[y, x+1])
            elif (np.pi / 8 <= angulo < 3*np.pi / 8) or (9*np.pi / 8 <= angulo < 11*np.pi / 8):
                vecinos = (magnitud_gradiente[y-1, x+1], magnitud_gradiente[y+1, x-1])
            elif (3*np.pi / 8 <= angulo < 5*np.pi / 8) or (11*np.pi / 8 <= angulo < 13*np.pi / 8):
                vecinos = (magnitud_gradiente[y-1, x], magnitud_gradiente[y+1, x])
            else:
                vecinos = (magnitud_gradiente[y-1, x-1], magnitud_gradiente[y+1, x+1])

            if magnitud_gradiente[y, x] >= max(vecinos):
                supresion[y, x] = magnitud_gradiente[y, x]

    return supresion

def umbralizar(imagen, umbral_bajo, umbral_alto):
    imagen_umbral = np.zeros_like(imagen)
    imagen_umbral[(imagen >= umbral_bajo) & (imagen <= umbral_alto)] = 255
    return imagen_umbral

if __name__ == "__main__": 
    imagen = cv2.imread('lapiz.png', cv2.IMREAD_GRAYSCALE)

    # Aplicar filtro de media para eliminar el ruido
    imagen_suavizada = cv2.blur(imagen, (3, 3)) 

    # Aplicar suavizado
    imagen_suavizada = suavizar_imagen(imagen)

    # Calcular gradientes
    magnitud_gradiente, direccion_gradiente = calcular_gradientes(imagen_suavizada)

    # Suprimir no máximos
    bordes_suprimidos = suprimir_no_maximos(magnitud_gradiente, direccion_gradiente)

    # Escala de grises o bl y ng
    bordes_suprimidos = np.uint8(bordes_suprimidos)

    # Umbralizar la imagen mas bajo y alto
    umbral_bajo = 30
    umbral_alto = 255
    bordes_umbralizados = umbralizar(bordes_suprimidos, umbral_bajo, umbral_alto)

    # Aplicar dilatación para que los bordes se vean más llenos
    kernel = np.ones((2,2), np.uint8)
    bordes_umbralizados_dilatados = cv2.dilate(bordes_umbralizados, kernel, iterations=1)

    cv2.imwrite('bordes_detectados_canny.png', bordes_umbralizados_dilatados)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].imshow(imagen, cmap='gray')
    axes[0].set_title('Imagen Original')
    axes[0].axis('off')

    axes[1].imshow(bordes_umbralizados_dilatados, cmap='gray')
    axes[1].set_title('Bordes Detectados')
    axes[1].axis('off')

    plt.show()
