import cv2
import numpy as np

def truncamiento(imagen, x, y):
    x_int = int(x)
    y_int = int(y)
    return imagen[y_int, x_int]

def vecino_cercano(imagen, x, y):
    x_int = int(round(x))
    y_int = int(round(y))
    return imagen[y_int, x_int]

def bilineal(imagen, x, y):
    x_int = int(x)
    y_int = int(y)
    x_frac = x - x_int
    y_frac = y - y_int


    # recorrer hasta el ultimo pixel
    if x_int < imagen.shape[1] - 1 and y_int < imagen.shape[0] - 1:
        # suma de area*intesidad 
        intensidad = (1 - x_frac) * (1 - y_frac) * imagen[y_int, x_int] + \
                             x_frac * (1 - y_frac) * imagen[y_int, x_int + 1] + \
                             (1 - x_frac) * y_frac * imagen[y_int + 1, x_int] + \
                             x_frac * y_frac * imagen[y_int + 1, x_int + 1]
        return intensidad
    # truncar al final
    else:
        return truncamiento(imagen, x, y)

def interpolacion_imagen(imagen, modo, escala_x, escala_y):
    if escala_x <= 0 or escala_y <= 0: 
        print("Error en las escalas")
        exit(0)


    if len(imagen.shape) == 3:
        canal1 = interpolacion_imagen(imagen[:,:,0], modo, escala_x, escala_y)
        canal2 = interpolacion_imagen(imagen[:,:,1], modo, escala_x, escala_y)
        canal3 = interpolacion_imagen(imagen[:,:,2], modo, escala_x, escala_y)
        img_escalada = cv2.merge((canal1, canal2, canal3))
        return img_escalada
    else:
        if modo == 'bilineal':
            metodo_interpolacion = bilineal
        elif modo == 'truncar':
            metodo_interpolacion = truncamiento
        elif modo == 'vecino':
            metodo_interpolacion = vecino_cercano
        else:
            raise ValueError("Modo de interpolación no válido.")
        # nuevo lienzo en negro
        nuevo_alto = int(imagen.shape[1] * escala_x)
        nuevo_ancho = int(imagen.shape[0] * escala_y)
        img_escalada = np.zeros((nuevo_ancho, nuevo_alto), dtype=np.uint8)

        for y in range(nuevo_ancho):
            for x in range(nuevo_alto):
                escala_nueva_x = x / escala_x
                escala_nueva_y = y / escala_y
                img_escalada[y, x] = metodo_interpolacion(imagen, escala_nueva_x, escala_nueva_y)

        return img_escalada

if __name__ == "__main__":
    
    imagen_path = "C:/Users/Hp245-User/Desktop/openCV/images/cameraman.png"
    imagen = cv2.imread(imagen_path, cv2.IMREAD_COLOR)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original", imagen)

    print(imagen.shape)

    img_escalada = interpolacion_imagen(imagen, 'bilineal', escala_x=3, escala_y=3)

    print(img_escalada.shape)
    
    cv2.imshow("imagen Escalada", img_escalada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()