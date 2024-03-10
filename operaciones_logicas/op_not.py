import numpy as np
import cv2

def operacion_not(imagen1):
    # Cargando las imágenes
    img1 = imagen1
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    print(f"{img1.shape}")
    # Verificando que las imágenes se cargaron correctamente
    if img1 is None:
        print("Error!/nNo se pudo cargar alguna de las imagenes")
        return

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
                    imagen_resultado[y, x, c] = ~img1[y, x, c]
            else:
                imagen_resultado[y, x] = ~img1[y, x]


    # resultado_cv2 = cv2.bitwise_and(img2, img1)
    # return imagen_resultado, resultado_cv2
    return imagen_resultado

if __name__ == "__main__":

    image1_path = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"
    
    imagen1 = cv2.imread(image1_path)

    resultado= operacion_not(imagen1)
    
    print(np.max(resultado))
    # Mostrar las imágenes originales y el resultado
    cv2.imshow('Imagen 1', imagen1)
    cv2.imshow('Resultado', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
