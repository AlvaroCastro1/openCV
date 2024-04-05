import cv2
import numpy as np

# Funcion que se ejecutara cada vez que cambie el valor de los trackbars
def actualizar_umbral(x):
    # Obtener los valores actuales de los trackbars
    umbral_min_rojo = cv2.getTrackbarPos('Umbral Minimo Rojo', 'Configuracion de Umbral')
    umbral_max_rojo = cv2.getTrackbarPos('Umbral Maximo Rojo', 'Configuracion de Umbral')
    umbral_min_verde = cv2.getTrackbarPos('Umbral Minimo Verde', 'Configuracion de Umbral')
    umbral_max_verde = cv2.getTrackbarPos('Umbral Maximo Verde', 'Configuracion de Umbral')
    umbral_min_azul = cv2.getTrackbarPos('Umbral Minimo Azul', 'Configuracion de Umbral')
    umbral_max_azul = cv2.getTrackbarPos('Umbral Maximo Azul', 'Configuracion de Umbral')

    # Aplicar los umbrales a los canales RGB
    umbralizado_rojo = cv2.inRange(canal_rojo, umbral_min_rojo, umbral_max_rojo)
    umbralizado_verde = cv2.inRange(canal_verde, umbral_min_verde, umbral_max_verde)
    umbralizado_azul = cv2.inRange(canal_azul, umbral_min_azul, umbral_max_azul)

    # Realizar la operacion AND bit a bit entre las imagenes umbralizadas en rojo, verde y azul
    resultado_and = cv2.bitwise_and(umbralizado_rojo, cv2.bitwise_and(umbralizado_verde, umbralizado_azul))

    # Concatenar las imagenes umbralizadas y el resultado de la operacion AND
    imagenes_concatenadas = np.hstack([umbralizado_rojo, umbralizado_verde, umbralizado_azul, resultado_and])

    # Mostrar las imagenes umbralizadas y el resultado de la operacion AND
    cv2.imshow('Configuracion de Umbral', imagenes_concatenadas)


if __name__ == "__main__":

    # Leer una imagen
    imagen = cv2.imread('/home/alvaro/Público/openCV/images/flowers.jpg')

    # Separar los canales de la imagen
    global canal_rojo, canal_verde, canal_azul
    canal_rojo = imagen[:, :, 2]
    canal_verde = imagen[:, :, 1]
    canal_azul = imagen[:, :, 0]

    # Crear una ventana para la configuracion del umbral
    cv2.namedWindow('Configuracion de Umbral', cv2.WINDOW_NORMAL)

    # Crear los trackbars para el canal rojo
    cv2.createTrackbar('Umbral Minimo Rojo', 'Configuracion de Umbral', 0, 255, actualizar_umbral)
    cv2.createTrackbar('Umbral Maximo Rojo', 'Configuracion de Umbral', 0, 255, actualizar_umbral)

    # Crear los trackbars para el canal verde
    cv2.createTrackbar('Umbral Minimo Verde', 'Configuracion de Umbral', 0, 255, actualizar_umbral)
    cv2.createTrackbar('Umbral Maximo Verde', 'Configuracion de Umbral', 0, 255, actualizar_umbral)

    # Crear los trackbars para el canal azul
    cv2.createTrackbar('Umbral Minimo Azul', 'Configuracion de Umbral', 0, 255, actualizar_umbral)
    cv2.createTrackbar('Umbral Maximo Azul', 'Configuracion de Umbral', 0, 255, actualizar_umbral)

    # Inicializar los valores iniciales de los trackbars
    cv2.setTrackbarPos('Umbral Maximo Rojo', 'Configuracion de Umbral', 255)
    cv2.setTrackbarPos('Umbral Maximo Verde', 'Configuracion de Umbral', 255)
    cv2.setTrackbarPos('Umbral Maximo Azul', 'Configuracion de Umbral', 255)

    # Llamar a la funcion actualizar_umbral para aplicar el umbral inicial
    actualizar_umbral(0)

    # Esperar a que se presione la tecla 'q' para salir
    while cv2.waitKey(1) & 0xFF != ord('q'):
        pass

    # Cerrar todas las ventanas
    cv2.destroyAllWindows()