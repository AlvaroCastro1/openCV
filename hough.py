import cv2
import numpy as np
from skimage import data, color
from skimage.transform import probabilistic_hough_line
from skimage.feature import canny

# Cargar la imagen
image = cv2.imread('images/hough2.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de Canny para detectar bordes
edges = canny(image_gray, sigma=2)

# Aplicar la transformada de Hough probabilística
lines = probabilistic_hough_line(edges, threshold=10, line_length=5, line_gap=3)

# Crear una copia de la imagen para dibujar las líneas
image_with_lines = image.copy()
for line in lines:
    p0, p1 = line
    cv2.line(image_with_lines, tuple(p0), tuple(p1), (0, 255, 0), 2)

# Mostrar la imagen con OpenCV
cv2.imshow('Hough Transform', image_with_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
