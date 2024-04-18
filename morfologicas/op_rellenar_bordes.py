import cv2
import numpy as np

def rellenar_formas(ruta_imagen):
    # Cargar la imagen
    imagen = cv2.imread(ruta_imagen)

    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización para obtener una imagen binaria
    _, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

    # Encontrar contornos en la imagen binaria
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una máscara para dibujar los contornos rellenados
    mascara = np.zeros_like(gris)

    # Dibujar los contornos rellenados en la máscara
    cv2.drawContours(mascara, contornos, -1, (255, 255, 255), -1)

    return mascara

if __name__ == "__main__":
    # Llamar a la función con la ruta de la imagen y obtener la imagen procesada
    imagen_rellenada = rellenar_formas("/home/alvaro/Público/openCV/images/esqueleto.png")

    # Mostrar la imagen con las formas rellenadas
    cv2.imshow('Formas Rellenadas', imagen_rellenada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
