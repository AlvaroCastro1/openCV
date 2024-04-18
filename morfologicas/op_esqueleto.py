"""
Funciona iterativamente eliminando píxeles de los bordes de la imagen hasta que solo queda el esqueleto

1. sacar imagen binaria
2. iniciar matriz vacía.
3. Repetir hasta que no haya cambio:
   a. En cada píxel en la imagen:
      i.  Se hace erosión despues dilatación en forma de cruz.
      ii. Hace restala imagen dilatada y la imagen erosionada.
      iii. Seleccionar los píxeles que son 1 en la imagen de diferencia y agregarlos al esqueleto.
   b. Actualizar la imagen binaria con el resultado de la erosión.
   c. Verificar si se ha alcanzado la convergencia:
      i.  Si no se han eliminado píxeles en la última iteración, terminar el bucle.
      ii. De lo contrario, continuar con la siguiente iteración.
4. Devolver el esqueleto resultante.
"""
import cv2
import numpy as np

# Funciones personalizadas de erosión y dilatación
def erosión_personalizada(img, elemento_estructurante):
    # Realiza la erosión personalizada
    kernel_h, kernel_v = elemento_estructurante
    alto, ancho = img.shape
    img_erosionada = np.zeros((alto, ancho), dtype=np.uint8)

    for y in range(alto):
        for x in range(ancho):
            if img[y, x] == 255:
                # Comprueba la vecindad en forma de cruz
                if (y - kernel_v >= 0 and img[y - kernel_v, x] == 255) and \
                   (y + kernel_v < alto and img[y + kernel_v, x] == 255) and \
                   (x - kernel_h >= 0 and img[y, x - kernel_h] == 255) and \
                   (x + kernel_h < ancho and img[y, x + kernel_h] == 255):
                    img_erosionada[y, x] = 255

    return img_erosionada

def dilatación_personalizada(img, elemento_estructurante):
    # Realiza la dilatación personalizada
    kernel_h, kernel_v = elemento_estructurante
    alto, ancho = img.shape
    img_dilatada = np.zeros((alto, ancho), dtype=np.uint8)

    for y in range(alto):
        for x in range(ancho):
            if img[y, x] == 255:
                # Dilatación en forma de cruz
                for dy in range(-kernel_v, kernel_v + 1):
                    for dx in range(-kernel_h, kernel_h + 1):
                        if (y + dy >= 0 and y + dy < alto) and \
                           (x + dx >= 0 and x + dx < ancho):
                            img_dilatada[y + dy, x + dx] = 255

    return img_dilatada

def esqueletonizar(imagen):
    tamaño = np.size(imagen)
    esqueleto = np.zeros(imagen.shape, np.uint8)

    # Umbralización de la imagen
    _, img_binaria = cv2.threshold(imagen, 127, 255, 0)

    # Elemento estructurante para la forma de cruz
    elemento_estructurante = (1, 1)

    hecho = False
    while not hecho:
        # Erosión seguida de dilatación
        erosionada = erosión_personalizada(img_binaria, elemento_estructurante)
        temp = dilatación_personalizada(erosionada, elemento_estructurante)
        temp = cv2.subtract(img_binaria, temp)
        esqueleto = cv2.bitwise_or(esqueleto, temp)
        img_binaria = erosionada.copy()

        # Verifica la convergencia
        ceros = tamaño - cv2.countNonZero(img_binaria)
        if ceros == tamaño:
            hecho = True

    return esqueleto

if __name__ == "__main__":
    # Carga la imagen
    imagen = cv2.imread("/home/alvaro/Público/openCV/images/esqueleto.png", 0)

    # Binariza la imagen
    _, binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

    # Esqueletoniza la imagen binaria
    esqueleto = esqueletonizar(binaria)

    # Muestra la imagen esqueletonizada
    cv2.imshow("Esqueleto de la imagen", esqueleto)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
