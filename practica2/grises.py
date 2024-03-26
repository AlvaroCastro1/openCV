import cv2
import matplotlib.pyplot as plt

def histograma_gris(imagen: str):

    alto, ancho = imagen.shape

    conteo_colores = {}

    # cada pixel añadir frecuencia
    for i in range(alto):
        for j in range(ancho):
            intensidad = imagen[i, j]
            if intensidad in conteo_colores:
                conteo_colores[intensidad] += 1
            else:
                conteo_colores[intensidad] = 1

    # añadir al diccionario todas las intensidades (0 a 255)
    for valor in range(256):
        if valor not in conteo_colores:
            conteo_colores[valor] = 0

    conteo_colores = dict(sorted(conteo_colores.items()))
    return conteo_colores


if __name__ == "__main__":
    image_path = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"
    conteo_colores = histograma_gris(image_path)
    # subplots
    plt.figure(figsize=(14, 6))

    # Subplot para el histograma
    plt.subplot(111)
    plt.bar(conteo_colores.keys(), conteo_colores.values(), color='gray')
    plt.title('Histograma en escala de grises')
    plt.xlabel('Valor de intensidad')
    plt.ylabel('Frecuencia')

    # Ajustar automáticamente el tamaño de la ventana
    plt.gcf().set_size_inches(12, 6)

    # Mostrar los subplots
    plt.tight_layout()
    plt.show()

    # # subplots
    # plt.figure(figsize=(14, 6))

    # # subplot para la imagen
    # plt.subplot(121)
    # plt.imshow(imagen, cmap='gray')
    # plt.title('Imagen en escala de grises')
    # plt.axis('off')

    # # Subplot para el histograma
    # plt.subplot(122)
    # plt.bar(conteo_colores.keys(), conteo_colores.values(), color='gray')
    # plt.title('Histograma en escala de grises')
    # plt.xlabel('Valor de intensidad')
    # plt.ylabel('Frecuencia')

    # # Ajustar automáticamente el tamaño de la ventana
    # plt.gcf().set_size_inches(12, 6)

    # # Mostrar los subplots
    # plt.tight_layout()
    # plt.show()