import cv2
import numpy as np
from operaciones_basicas.convert_8216 import transformar

def sum_images(image1, image2, modo: str):
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

    # Suma pixel a pixel

    result = np.zeros_like(img1, dtype=np.uint8)
    result_promedio = np.zeros_like(img1, dtype=np.uint16)

    if len(result.shape) == 3:  # If it's a color image
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                for k in range(result.shape[2]):
                    suma_entre_pixel= int(img1[i, j, k]) + int(img2[i, j, k])

                    if modo=="truncar":
                        #truncar
                        result[i, j, k] = min(int(suma_entre_pixel), 255)
                    if modo=="ciclico":
                        #ciclico
                        result[i, j, k] = suma_entre_pixel % 256 
                        
                    if modo=="promedio":
                        result_promedio[i, j, k] = suma_entre_pixel

        if modo == "promedio":
            result = transformar(result_promedio)

    elif len(result.shape) == 2:  # If it's a grayscale image
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                suma_entre_pixel= int(img1[i, j]) + int(img2[i, j])

                if modo=="truncar":
                    #truncar
                    result[i, j] = min(int(suma_entre_pixel), 255)
                if modo=="ciclico":
                    #ciclico
                    result[i, j] = suma_entre_pixel % 256 
                    
                if modo=="promedio":
                    result_promedio[i, j] = suma_entre_pixel

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
    r = sum_images(image1, image2,"promedio")
    cv2.namedWindow("suma", cv2.WINDOW_NORMAL)
    cv2.imshow("suma",r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
