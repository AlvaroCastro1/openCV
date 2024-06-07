import cv2
import numpy as np

# Función de manejo de eventos de ratón
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordenadas del punto de semilla: ({x}, {y})")
        flood_fill(image_gray, (x, y))

# Función para aplicar flood fill
def flood_fill(image, seed_point):
    filled_image = image.copy()
    h, w = filled_image.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(filled_image, mask, seed_point, 255)
    cv2.imshow('Imagen con Flood Fill', filled_image)

# Leer la imagen y convertirla a escala de grises
image = cv2.imread('images/ochos.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen original
cv2.imshow('Imagen Original', image_gray)

# Configurar la función de devolución de llamada del ratón
cv2.setMouseCallback('Imagen Original', mouse_callback)

# Esperar hasta que el usuario cierre la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
