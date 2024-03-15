import cv2
import numpy as np
from convert_8216 import transformar

def multiplicar_imagen(image: str, constant: int, modo: str):

    if constant >= 255:
        constant = 255

    img1 = cv2.imread(image)


    if img1 is None:
        print("Error!/nNo se pudo cargar la imagen")
        return

    # enteros de 0 a 255
    resultado = np.zeros_like(img1, dtype=np.uint8)
    # 0 hasta 65535
    resultado_promedio = np.zeros_like(img1, dtype=np.uint16)

    for i in range(resultado.shape[0]):
        for j in range(resultado.shape[1]):
            for k in range(resultado.shape[2]):

                multi_entre_pixel= int(img1[i, j, k]) * constant

                if modo=="truncar":
                #truncar
                    resultado[i, j, k] = min(int(multi_entre_pixel), 255)
                if modo=="ciclico":
                    #ciclico
                    resultado[i, j, k] = multi_entre_pixel % 256 
                    
                if modo=="promedio":
                    resultado_promedio[i, j, k] = multi_entre_pixel

    if modo == "promedio":
        resultado = transformar(resultado_promedio)
        
    return resultado

if __name__ == "__main__":
    image_path = "C:/Users/Hp245-User/Desktop/openCV/images/patos.png"

    """
    truncar
    ciclico
    promedio
    """
    r = multiplicar_imagen(image_path, 30,"promedio")
    cv2.namedWindow("multi", cv2.WINDOW_NORMAL)
    cv2.imshow("multi",r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
