import cv2
import numpy as np

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
        for canal in range(resultado_promedio.shape[2]):
            max_valor = np.max(resultado_promedio[:, :, canal])
            min_valor = np.min(resultado_promedio[:, :, canal])
            print(f"Canal {canal + 1}: {min_valor} - {max_valor}")

            for i in range(resultado.shape[0]):
                for j in range(resultado.shape[1]):
                    resultado[i, j, canal] = ((resultado_promedio[i, j, canal] - min_valor) / (max_valor - min_valor)) * 255
                    # resultado[i, j, canal] = ((resultado_promedio[i, j, canal] - min_valor) / (max_valor)) * 255

    # cv2.imshow("division de Imagenes", resultado)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return resultado

if __name__ == "__main__":
    image_path = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"
    imagen = cv2.imread(image_path)

    r = division_imagen(imagen, 3,"truncar")
    cv2.imshow('Imagen Div', r)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
