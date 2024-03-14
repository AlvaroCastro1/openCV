import cv2
import numpy as np

def on_trackbar(value):
    global r_threshold, g_threshold, b_threshold
    
    # Actualiza los umbrales con los valores de los trackbars
    r_threshold = cv2.getTrackbarPos('Rojo', 'Threshold')
    g_threshold = cv2.getTrackbarPos('Verde', 'Threshold')
    b_threshold = cv2.getTrackbarPos('Azul', 'Threshold')
    
    # Realiza la segmentación basada en los umbrales
    Sr = r > r_threshold
    Sg = g < g_threshold
    Sb = b < b_threshold
    
    # Concatena los resultados de los umbrales para visualización
    result = np.concatenate((Sr, Sg, Sb), axis=1)
    
    # Realiza la operación AND lógica entre los umbrales de los canales
    S = np.logical_and(Sr, np.logical_and(Sg, Sb))
    
    # Aplica la máscara al canal original
    masked_image = np.zeros_like(image)
    masked_image[:,:,0][S] = b[S]
    masked_image[:,:,1][S] = g[S]
    masked_image[:,:,2][S] = r[S]
    
    # Muestra la imagen resultante
    cv2.imshow('Resultado', masked_image)

# Carga la imagen desde el archivo
image = cv2.imread("C:/Users/Hp245-User/Desktop/openCV/images/frutos_rojos.png")

# Divide la imagen en canales BGR
b, g, r = cv2.split(image)

# Crea la ventana y los trackbars
cv2.namedWindow('Threshold')
cv2.createTrackbar('Azul', 'Threshold', 0, 255, on_trackbar)
cv2.createTrackbar('Verde', 'Threshold', 0, 255, on_trackbar)
cv2.createTrackbar('Rojo', 'Threshold', 0, 255, on_trackbar)

# Llama a la función para mostrar la imagen inicial
on_trackbar(0)

# Espera a que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
