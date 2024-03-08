import numpy as np
import cv2

def filtro_media(imagen, tamano_kernel:int):
    if tamano_kernel % 2 == 0:
        tamano_kernel += 1

    altura, ancho = imagen.shape[:2]
    if len(imagen.shape) == 3:  # imagen es a color
        canales = imagen.shape[2]
        imagen_filtrada = np.zeros_like(imagen)
    else:
        canales = 1
        imagen_filtrada = np.zeros_like(imagen, dtype=np.uint8)

    # calcular margen para evitar bordes
    margen = tamano_kernel // 2

    # empieza desde el margen, no 0
    for y in range(margen, altura - margen):
        for x in range(margen, ancho - margen):
            # inclusivo inferior y exclusivo superior
            area = imagen[y - margen: y + margen + 1, x - margen:x + margen + 1]
            # print(area.shape)

            # calcular promedio para cada canal
            if canales > 1:
                for c in range(canales):
                    valor_medio = int(np.mean(area[:, :, c]))
                    imagen_filtrada[y, x, c] = valor_medio
            else:
                valor_medio = int(np.mean(area))
                imagen_filtrada[y, x] = valor_medio

    return imagen_filtrada

if __name__ == "__main__":
    # carga la imagen usando OpenCV
    imagen_original = cv2.imread('C:/Users/Hp245-User/Desktop/openCV/images/ruido1.jpg')
    # imagen_original = cv2.cvtColor(imagen_original, cv2.COLOR_RGB2GRAY)

    tamano_kernel = 3
    imagen_filtrada_personalizada = filtro_media(imagen_original, tamano_kernel)

    # funcion de openCV
    imagen_filtrada_opencv = cv2.blur(imagen_original, (tamano_kernel, tamano_kernel))

    cv2.imshow('Imagen Original', imagen_original)
    cv2.imshow('Imagen Filtrada (Personalizado)', imagen_filtrada_personalizada)
    cv2.imshow('Imagen Filtrada (OpenCV)', imagen_filtrada_opencv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()