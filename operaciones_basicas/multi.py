import cv2
import numpy as np
from operaciones_basicas.convert_8216 import transformar

def multiplicar_imagen(image, constant, modo):
    if constant >= 255:
        constant = 255

    if image is None:
        print("Error!\nNo se pudo cargar la imagen")
        return

    resultado = np.zeros_like(image, dtype=np.uint8)

    if len(image.shape) == 2:  # imagen gris
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                multi_entre_pixel = int(image[i, j]) * constant

                if modo == "truncar":
                    resultado[i, j] = min(int(multi_entre_pixel), 255)
                elif modo == "ciclico":
                    resultado[i, j] = multi_entre_pixel % 256

    elif len(image.shape) == 3:  # imagen color
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(image.shape[2]):
                    multi_entre_pixel = int(image[i, j, k]) * constant

                    if modo == "truncar":
                        resultado[i, j, k] = min(int(multi_entre_pixel), 255)
                    elif modo == "ciclico":
                        resultado[i, j, k] = multi_entre_pixel % 256

    if modo == "promedio":
        resultado_promedio = np.zeros_like(image, dtype=np.uint16)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(image.shape[2]):
                    multi_entre_pixel = int(image[i, j, k]) * constant
                    resultado_promedio[i, j, k] = multi_entre_pixel
        resultado = transformar(resultado_promedio)

    return resultado

if __name__ == "__main__":
    image = cv2.imread("C:/Users/Hp245-User/Desktop/openCV/images/patos.png",0)

    """
    truncar
    ciclico
    promedio
    """
    r = multiplicar_imagen(image, 5, "truncar")
    cv2.namedWindow("multi", cv2.WINDOW_NORMAL)
    cv2.imshow("multi", r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
