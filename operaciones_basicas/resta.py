import cv2
import numpy as np
from operaciones_basicas.convert_8216 import transformar

def rest_images(image1, image2, modo: str):
    # Cargando las imágenes
    img1 = image1
    img2 = image2
    # print(f"{img1.shape} {img2.shape}")

    # Verificando que las imágenes se cargaron correctamente
    if img1 is None or img2 is None:
        print("Error!/nNo se pudo cargar alguna de las imagenes")
        return

    # ajustar el tamaño de las img que sean iguales
    if img1.shape != img2.shape:
        # redimensionar imagen2 al tamaño de imagen1
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # resta pixel a pixel

    result = np.zeros_like(img1, dtype=np.uint8)
    # int16 para + y -
    result_promedio = np.zeros_like(img1, dtype=np.int16)

    if len(result.shape) == 3:  # If it's a color image
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                for k in range(result.shape[2]):
                    resta_entre_pixel= int(img1[i, j, k]) - int(img2[i, j, k])

                    if modo=="truncar":
                        #truncar
                        result[i, j, k] = max(int(resta_entre_pixel), 0)
                    if modo=="ciclico":
                        #ciclico
                        result[i, j, k] = resta_entre_pixel % 256 
                        
                    if modo=="promedio":
                        result_promedio[i, j, k] = resta_entre_pixel

        if modo == "promedio":
            result = transformar(result_promedio)

    elif len(result.shape) == 2:  # If it's a grayscale image
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                resta_entre_pixel= int(img1[i, j]) - int(img2[i, j])

                if modo=="truncar":
                    #truncar
                    result[i, j] = max(int(resta_entre_pixel), 0)
                if modo=="ciclico":
                    #ciclico
                    result[i, j] = resta_entre_pixel % 256 
                    
                if modo=="promedio":
                    result_promedio[i, j] = resta_entre_pixel

        if modo == "promedio":
            result = transformar(result_promedio)

    return result

if __name__ == "__main__":
    image2 = cv2.imread("C:/Users/Hp245-User/Desktop/openCV/images/patos.png",0)
    image1 = cv2.imread("C:/Users/Hp245-User/Desktop/openCV/images/lenacolor.png",0)

    """
    truncar
    ciclico
    promedio
    """
    img = rest_images(image1, image2,"promedio")

    # image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    # img = cv2.subtract(image1, image2)

    cv2.namedWindow("resta", cv2.WINDOW_NORMAL)
    cv2.imshow("resta",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
