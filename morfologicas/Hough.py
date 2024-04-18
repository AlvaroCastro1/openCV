import cv2
import numpy as np

'''
    Usamos la fórmula p = x*cos(theta) + y*cos(theta) como representación de una línea de borde donde p es la longitud de la 
    línea perpendicular dibujada desde el origen (0,0) hasta la línea de borde y theta es el ángulo que la línea perpendicular forma 
    con el eje x en dirección contraria a las agujas del reloj.
    Transformamos cada punto de borde (x',y') en la imagen de borde a una curva coseno en el espacio de parámetros utilizando la fórmula anterior. 
    Como resultado, obtendremos muchas curvas coseno que se intersectan en varios puntos. Encontraremos los puntos (p, theta) a través de los 
    cuales pasan muchas curvas coseno que superan un umbral dado, y esos corresponderán a las líneas detectadas en el mapa de bordes.
'''
def transformadaHough(edgeMap, p_max):
    '''
    :param edgeMap: imagen que contiene solo bordes obtenidos mediante la detección de bordes de Canny
    :param p_max: longitud máxima posible de la perpendicular dibujada desde el origen hasta cualquier línea de borde en la imagen de borde
    :return: el arreglo np que contiene la transformada de Hough
    '''

    (alto, ancho) = edgeMap.shape[:2]
    # p_max representa la longitud máxima de una perpendicular dibujada desde el origen hasta una línea de borde en la imagen
    # p puede variar desde -p_max hasta p_max
    grados = 180
    # La imagen de Hough almacenará los datos de la transformada de Hough
    imagenHough = np.zeros((2*(p_max+1)+1, grados+1), dtype=np.uint8)

    for x in range(ancho):
        for y in range(alto):
            if edgeMap[y][x] != 0:
                # tenemos un punto de borde, encontramos todos los pares (p, theta) de líneas que pasan por estos puntos
                for theta in range(1,grados):
                    # p = x*cos(theta) + y*sin(theta)
                    # las funciones cos y sin de numpy toman el ángulo en radianes, así que convertimos grados a radianes
                    p = x*np.cos(theta*np.pi/180) + y*np.sin(theta*np.pi/180)
                    p = int(p + p_max)
                    if(imagenHough[p][theta] < 255):
                        imagenHough[p][theta] += 1

    return imagenHough


def encontrarPuntosParaLinea(p, theta, ancho, alto):
    # p = x*cos(theta) + y*sin(theta)
    x_0 = 0
    y_0 = 0
    try:
        y_0 = int(p/np.sin(theta*np.pi/180))
    except ZeroDivisionError:
        x_0 = p
        y_0 = 0

    x_1 = ancho - 1
    y_1 = 0
    try:
        y_1 = int((p - x_1 * np.cos(theta * np.pi / 180)) / np.sin(theta * np.pi / 180))
    except ZeroDivisionError:
        x_1 = p
        y_1 = 1

    y_2 = 0
    x_2 = 0
    try:
        x_2 = int(p/np.cos(theta*np.pi/180))
    except ZeroDivisionError:
        y_2 = p
        x_2 = 0

    y_3 = alto - 1
    x_3 = 0
    try:
        x_3 = int((p - y_3 * np.sin(theta*np.pi/180))/np.cos(theta * np.pi/180))
    except ZeroDivisionError:
        y_3 = p
        x_3 = 1

    # verifique qué dos de las cuatro parejas están dentro de los límites
    puntos = np.zeros((4,2), dtype=np.uint8)
    k = 0
    if y_0 >= 0 and y_0 < alto:
        puntos[k][0] = np.uint8(x_0)
        puntos[k][1] = np.uint8(y_0)
        k += 1

    if y_1 >= 0 and y_1 < alto:
        puntos[k][0] = np.uint8(x_1)
        puntos[k][1] = np.uint8(y_1)
        k += 1

    if x_2 >= 0 and x_2 < ancho:
        puntos[k][0] = np.uint8(x_2)
        puntos[k][1] = np.uint8(y_2)
        k += 1

    if x_3 >= 0 and x_3 < ancho:
        puntos[k][0] = np.uint8(x_3)
        puntos[k][1] = np.uint8(y_3)
        k += 1
    return puntos


def imagenHough(original, cannyThreshold1=100, cannyThreshold2=200, umbralHough=40):
    imagenBordesCanny = cv2.Canny(original, cannyThreshold1, cannyThreshold2)
    (alto, ancho) = imagenBordesCanny.shape[:2]
    p_max = int(np.sqrt(alto**2 + ancho**2))
    imagenHough = transformadaHough(imagenBordesCanny, p_max)
    dictLineas = {}
    (altoHough, anchoHough) = imagenHough.shape[:2]
    for p in range(altoHough):
        for t in range(anchoHough):
            if imagenHough[p][t] >= umbralHough:
                if p not in dictLineas:
                    dictLineas[p-p_max] = []
                dictLineas[p-p_max].append(t)

    for p in dictLineas:
        for theta in dictLineas[p]:
            puntos = encontrarPuntosParaLinea(p, theta, ancho, alto)
            cv2.line(original, (puntos[0][0], puntos[0][1]), (puntos[1][0], puntos[1][1]), (255,255), 1)
    return original


if __name__ == "__main__":
    # img = cv2.imread("./hough/hough2.png")
    # imagenBordesCanny = cv2.Canny(img,100,200)
    # (alto, ancho) = imagenBordesCanny.shape[:2]
    # #print(cannyEdgeImg)
    # p_max = int(np.sqrt(alto**2 + ancho**2))
    # imagenHough = transformadaHough(imagenBordesCanny, p_max)
    # umbral = 40
    # # ahora seleccionamos los pares (p,theta) tales que el número de curvas coseno que se intersectan es mayor que el umbral
    # dictLineas = {}
    # (altoHough, anchoHough) = imagenHough.shape[:2]
    # for p in range(altoHough):
    #     for t in range(anchoHough):
    #         if imagenHough[p][t] >= umbral:
    #             if p not in dictLineas:
    #                 dictLineas[p-p_max] = []
    #             dictLineas[p-p_max].append(t)

    # # ahora dibujamos líneas en la imagen original
    # # print(lineDict)
    # i = 0
    # for p in dictLineas:
    #     for theta in dictLineas[p]:
    #         #obtener dos puntos correspondientes a este par (p, theta)
    #         # p= x*cos(theta) + y*sin(theta)
    #         puntos = encontrarPuntosParaLinea(p, theta, ancho, alto)
    #         #print("{}, {}".format(points[0][0], points[0][1]) )
    #         #print("{}, {}".format(points[1][0], points[1][1]))
    #         cv2.line(img, (puntos[0][0], puntos[0][1]), (puntos[1][0], puntos[1][1]), (255,255), 1)
    # cv2.imshow("Mapa de bordes", imagenBordesCanny)
    # cv2.imshow("Mapa de Hough", imagenHough)
    # cv2.imshow("imagen con lineas", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    img = cv2.imread("/home/alvaro/Público/openCV/images/hough1.png")
    img_con_lineas = imagenHough(img)
    cv2.imshow("imagen con lineas", img_con_lineas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()