import cv2
import numpy as np
from operaciones_basicas.convert_8216 import transformar

def division_imagen(image1, constant: int, modo: str):

    if constant >= 255:
            constant = 255

    img1 = image1


    if img1 is None:
        print("Error!/nNo se pudo cargar la imagen")
        return

    # division pixel a pixel

    resultado = np.zeros_like(img1, dtype=np.uint8)
    resultado_promedio = np.zeros_like(img1, dtype=np.uint16)

    if len(img1.shape) == 2:  # Grayscale image
        for i in range(resultado.shape[0]):
            for j in range(resultado.shape[1]):
                division_entre_pixel = int(img1[i, j]) / constant

                if modo=="truncar":
                #truncar
                    resultado[i, j] = min(int(division_entre_pixel), 255)
                if modo=="ciclico":
                    #ciclico
                    resultado[i, j] = division_entre_pixel % 256 
                    
                if modo=="promedio":
                    resultado_promedio[i, j] = division_entre_pixel

    elif len(img1.shape) == 3:  # Color image
        for i in range(resultado.shape[0]):
            for j in range(resultado.shape[1]):
                for k in range(resultado.shape[2]):
                    division_entre_pixel = int(img1[i, j, k]) / constant

                    if modo=="truncar":
                    #truncar
                        resultado[i, j, k] = min(int(division_entre_pixel), 255)
                    if modo=="ciclico":
                        #ciclico
                        resultado[i, j, k] = division_entre_pixel % 256 
                        
                    if modo=="promedio":
                        resultado_promedio[i, j, k] = division_entre_pixel

    if modo == "promedio":
        resultado = transformar(resultado_promedio)

    return resultado

if __name__ == "__main__":
    image = cv2.imread("C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png")

    """
    truncar
    ciclico
    promedio
    """
    r = division_imagen(image, 3,"promedio")
    cv2.namedWindow("divi", cv2.WINDOW_NORMAL)
    cv2.imshow("divi",r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
