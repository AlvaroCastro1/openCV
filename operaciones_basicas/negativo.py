import cv2

def obtener_negativo(imagen):
    alto, ancho, _ = imagen.shape
    
    negativo = imagen.copy()
    
    for y in range(alto):
        for x in range(ancho):
            pixel = imagen[y, x]
            # nuevo pixel en negativo (225 - canal)
            negativo[y, x] = [255 - pixel[0], 255 - pixel[1], 255 - pixel[2]]
    
    return negativo

if __name__ == "__main__":
    image_path = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"
    imagen = cv2.imread(image_path)

    negativo = obtener_negativo(imagen)

    cv2.namedWindow('Imagen Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Negativo de la Imagen', cv2.WINDOW_NORMAL)

    # Mostrar la imagen original y su negativo
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Negativo de la Imagen', negativo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()