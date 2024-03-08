import cv2
import numpy as np

def sum_images(image1, image2, modo: str):
    # Cargando las imágenes
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    print(f"{img1.shape} {img2.shape}")

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

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            for k in range(result.shape[2]):

                suma_entre_pixel= int(img1[i, j, k]) + int(img2[i, j, k])

                if modo=="truncar":
                #truncar
                    result[i, j, k] = min(int(suma_entre_pixel), 255)
                if modo=="ciclico":
                    #ciclico
                    """
                    se trabaja con el modulo
                    255 + 1 = 256 -> 256 % 256 = 0
                    255 + 3 = 258 -> 258 % 256 = 2
                    """
                    result[i, j, k] = suma_entre_pixel % 256 
                    
                if modo=="promedio":
                    result_promedio[i, j, k] = suma_entre_pixel

    if modo == "promedio":
        for canal in range(result_promedio.shape[2]):
            max_valor = np.max(result_promedio[:, :, canal])
            min_valor = np.min(result_promedio[:, :, canal])
            print(f"Canal {canal + 1}: {min_valor} - {max_valor}")

            for i in range(result.shape[0]):
                for j in range(result.shape[1]):
                    #result[i, j, canal] = ((result_promedio[i, j, canal] - min_valor) / (max_valor - min_valor)) * 255
                    result[i, j, canal] = ((result_promedio[i, j, canal] - min_valor) / (max_valor)) * 255


    # print(f"{img1.shape} {img2.shape}")
    # cv2.imshow("Suma de Imagenes", result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return result

if __name__ == "__main__":
    image2_path = "C:/Users/Hp245-User/Desktop/openCV/images/patos.png"
    image1_path = "C:/Users/Hp245-User/Desktop/openCV/images/lenacolor.png"

    """
    truncar
    ciclico
    promedio
    """
    sum_images(image1_path, image2_path,"promedio")
