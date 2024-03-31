import numpy as np
import cv2
import matplotlib.pyplot as plt

# Función de convolución
def convolucion(imagen, kernel):
    altura, ancho = imagen.shape
    kh, kw = kernel.shape
    kh2, kw2 = kh // 2, kw // 2
    resultado = np.zeros_like(imagen)

    for y in range(altura):
        for x in range(ancho):
            suma = 0
            for ky in range(kh):
                for kx in range(kw):
                    i = y + ky - kh2
                    j = x + kx - kw2
                    if i >= 0 and i < altura and j >= 0 and j < ancho:
                        suma += imagen[i, j] * kernel[ky, kx]
            resultado[y, x] = suma
    return resultado


if __name__ == "__main__": 
    imagen = cv2.imread('lapiz.png', cv2.IMREAD_GRAYSCALE)
        # Kernel de Prewitt para detección de bordes en dirección X
    kernel_prewitt_x = np.array([[-1, 0, 1],
                                [-1, 0, 1],
                                [-1, 0, 1]])

    # Kernel de Prewitt para detección de bordes en dirección Y
    kernel_prewitt_y = np.array([[-1, -1, -1],
                                [0, 0, 0],
                                [1, 1, 1]])

    # Aplicar convolución con los kernels de Prewitt
    edges_x = convolucion(imagen.astype(np.float32), kernel_prewitt_x)
    edges_y = convolucion(imagen.astype(np.float32), kernel_prewitt_y)

    # Combinar los bordes detectados en ambas direcciones
    edges = np.sqrt(np.square(edges_x) + np.square(edges_y))

    # Mostrar la imagen original y los bordes detectados
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(imagen, cmap='gray')
    plt.title('Imagen Original')
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Bordes detectados (Prewitt)')
    plt.show()
