import cv2
import numpy as np

def dilatar_imagen(img_binaria):
    kernel = np.ones((3, 3), np.uint8)
    alto, ancho = img_binaria.shape
    img_dilatada = np.zeros_like(img_binaria)

    # Aplicar dilatación
    for y in range(1, alto - 1):
        for x in range(1, ancho - 1):
            # Obtener la submatriz de la imagen binaria del tamaño del kernel
            submatriz = img_binaria[y-1:y+2, x-1:x+2]
            # Verificar si algún píxel en la vecindad es blanco (255)
            if np.max(submatriz * kernel) > 0:
                img_dilatada[y, x] = 255

    return img_dilatada

# Lógica principal directamente en el script
if __name__ == '__main__':
    img_binaria = cv2.imread('imagen.png', cv2.IMREAD_GRAYSCALE)
    if img_binaria is None:
        print("Error: No se pudo cargar la imagen.")
    else:
        img_dilatada = dilatar_imagen(img_binaria)

        cv2.imshow('Imagen Binaria Original', img_binaria)
        cv2.imshow('Imagen Binaria Dilatada', img_dilatada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

