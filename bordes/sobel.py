import cv2
import numpy as np
import matplotlib.pyplot as plt

def convolucion_sobel(imagen, kernel):
       
    alto, ancho = imagen.shape
    kernel_tam = kernel.shape[0]

    pad_size = kernel_tam // 2

    imagen_padded = np.pad(imagen, ((pad_size, pad_size), (pad_size, pad_size)), mode='constant')

    convolucion_matriz = np.zeros_like(imagen)

    for i in range(alto):
        for j in range(ancho):
            region_interes = imagen_padded[i:i + kernel_tam, j:j + kernel_tam]
            convolucion_matriz[i, j] = np.sum(region_interes * kernel)
    return convolucion_matriz

def detectar_bordes_sobel(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, imagen_bn = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])
    gradiente_x = convolucion_sobel(imagen_bn, sobel_x)
    gradiente_y = convolucion_sobel(imagen_bn, sobel_y)

    magnitud_gradiente = abs(np.sqrt(gradiente_x**2 + gradiente_y**2))
    max_magnitud = np.max(magnitud_gradiente)
    magnitud_gradiente /= max_magnitud
    bordes = (magnitud_gradiente * 255).astype(np.uint8)

    return bordes


def plot_images(image1, image2, title1, title2):
    fig, axs = plt.subplots(1, 2, figsize=(12, 5), num="Sobel")
   
    if len(image1.shape) == 2:
        axs[0].imshow(image1, cmap='gray')
    else:
        axs[0].imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    axs[0].set_title(title1)
    axs[0].axis('off')

    if len(image2.shape) == 2:
        axs[1].imshow(image2, cmap='gray')
    else:
        axs[1].imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    axs[1].set_title(title2)
    axs[1].axis('off')

    plt.show()

if __name__ == "__main__": 
    imagen_original = cv2.imread("lapiz.png")
    bordes_sobel = detectar_bordes_sobel(imagen_original)
    imagen_en_gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)

    plot_images(imagen_en_gris, bordes_sobel, "Imagen en Gris", "Bordes detectados con Sobel")
