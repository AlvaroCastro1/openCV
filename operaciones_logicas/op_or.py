import numpy as np
import cv2

def operacion_or(imagen1, imagen2):
    # Cargando las imágenes
    img1 = imagen1
    img2 = imagen2
    print(f"{img1.shape} {img2.shape}")

    # Verificando que las imágenes se cargaron correctamente
    if img1 is None or img2 is None:
        print("Error!/nNo se pudo cargar alguna de las imagenes")
        return
    
    # ajustar el tamaño de las img que sean iguales
    if img1.shape != img2.shape:
        # redimensionar imagen2 al tamaño de imagen1
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    altura, ancho = img1.shape[:2]
    if len(img1.shape) == 3:  # imagen a color
        canales = img1.shape[2]
        imagen_resultado = np.zeros_like(img1, dtype=np.uint8)
    else:
        canales = 1
        imagen_resultado = np.zeros_like(img1, dtype=np.uint8)

    # empieza desde el margen, no 0
    for y in range(altura):
        for x in range(ancho):
            if canales > 1:
                for c in range(canales):
                    imagen_resultado[y, x, c] = img1[y, x, c] | img2[y, x, c]
            else:
                imagen_resultado[y, x] = img1[y, x] | img2[y, x]


    # resultado_cv2 = cv2.bitwise_and(img2, img1)
    # return imagen_resultado, resultado_cv2
    return imagen_resultado

if __name__ == "__main__":

    image2_path = "C:/Users/Hp245-User/Desktop/openCV/images/patos.png"
    image1_path = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"
    
    imagen2 = cv2.imread(image2_path)
    imagen1 = cv2.imread(image1_path)

    resultado = operacion_or(imagen2, imagen1)

    # Mostrar las imágenes originales y el resultado
    cv2.imshow('Imagen 1', imagen1)
    cv2.imshow('Imagen 2', imagen2)
    cv2.imshow('Resultado', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
