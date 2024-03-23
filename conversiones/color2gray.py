import cv2

def convertir_a_gris_promedio(imagen):
    # Obtiene las dimensiones de la imagen
    alto, ancho, _ = imagen.shape
    
    # Crea una matriz vacía para la imagen en escala de grises
    img_gris = imagen.copy()
    
    # Itera sobre cada píxel de la imagen
    for y in range(alto):
        for x in range(ancho):
            # Obtiene los valores de los canales de color BGR en el píxel actual
            blue = imagen[y, x, 0]
            green = imagen[y, x, 1]
            red = imagen[y, x, 2]
            
            gray = 1/3 * red + 1/3 * green + 1/3 * blue
            
            # Asigna el valor de intensidad calculado a la matriz de la imagen en escala de grises
            img_gris[y, x] = gray
    
    return img_gris

def convertir_a_gris_formula(imagen):
    
    # Verifica si la imagen se ha leído correctamente
    if imagen is None:
        print("No se pudo leer la imagen.")
        return None
    
    # Obtiene las dimensiones de la imagen
    alto, ancho, _ = imagen.shape
    
    # Crea una matriz vacía para la imagen en escala de grises
    img_gris = imagen.copy()
    
    # Itera sobre cada píxel de la imagen
    for y in range(alto):
        for x in range(ancho):
            # Obtiene los valores de los canales de color BGR en el píxel actual
            blue = imagen[y, x, 0]
            green = imagen[y, x, 1]
            red = imagen[y, x, 2]
            
            # Calcula el valor de intensidad en escala de grises utilizando la fórmula Y = 0.299R + 0.587G + 0.114B
            gray = 0.299 * red + 0.587 * green + 0.114 * blue
            
            # Asigna el valor de intensidad calculado a la matriz de la imagen en escala de grises
            img_gris[y, x] = gray
    
    return img_gris

if __name__ == "__main__":
    image = cv2.imread("c:/Users/Hp245-User/Desktop/openCV/images/amarilla.png")
    cv2.namedWindow("original", cv2.WINDOW_NORMAL)
    cv2.imshow("original", image)
    
    r1 = convertir_a_gris_promedio(image)
    cv2.namedWindow("promedio", cv2.WINDOW_NORMAL)
    cv2.imshow("promedio", r1)
    
    r2 = convertir_a_gris_formula(image)
    cv2.namedWindow("formula", cv2.WINDOW_NORMAL)
    cv2.imshow("formula", r2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()