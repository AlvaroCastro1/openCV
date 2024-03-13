import cv2

# Función de callback para el trackbar
def nothing(x):
    pass

# Cargar la imagen
image = cv2.imread("c:/Users/Hp245-User/Desktop/openCV/images/frutos_rojos.png")

# Dividir la imagen en los canales de color
b, g, r = cv2.split(image)

# Crear ventanas para cada canal de color
cv2.namedWindow("Rojo", cv2.WINDOW_NORMAL)
cv2.namedWindow("Verde", cv2.WINDOW_NORMAL)
cv2.namedWindow("Azul", cv2.WINDOW_NORMAL)

# Crear trackbars para los umbrales de color
cv2.createTrackbar('Threshold', 'Rojo', 0, 255, nothing)
cv2.createTrackbar('Threshold', 'Verde', 0, 255, nothing)
cv2.createTrackbar('Threshold', 'Azul', 0, 255, nothing)

while True:
    # Obtener los valores actuales de los trackbars
    r_threshold = cv2.getTrackbarPos('Threshold', 'Rojo')
    g_threshold = cv2.getTrackbarPos('Threshold', 'Verde')
    b_threshold = cv2.getTrackbarPos('Threshold', 'Azul')

    # Aplicar los umbrales a cada canal de color
    r_filtered = cv2.threshold(r, r_threshold, 255, cv2.THRESH_BINARY)[1]
    g_filtered = cv2.threshold(g, g_threshold, 255, cv2.THRESH_BINARY)[1]
    b_filtered = cv2.threshold(b, b_threshold, 255, cv2.THRESH_BINARY)[1]

    # Mostrar las imágenes filtradas en las ventanas correspondientes
    cv2.imshow("Rojo", r_filtered)
    cv2.imshow("Verde", g_filtered)
    cv2.imshow("Azul", b_filtered)

    # Esperar a que se presione una tecla
    key = cv2.waitKey(1) & 0xFF

    # Salir del bucle si se presiona la tecla 'q'
    if key == ord("q"):
        break

# Cerrar todas las ventanas
cv2.destroyAllWindows()

