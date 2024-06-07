import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread('ejemplos/dilatacion.png', 0)

# Crear un kernel
kernel = np.ones((3, 3), np.uint8)

# imagen_dilatada = cv2.dilate(imagen, kernel, iterations=1)
# cv2.namedWindow("dilatada", cv2.WINDOW_NORMAL)
# cv2.imshow('dilatada', imagen_dilatada)

# imagen_erosionada = cv2.erode(imagen, kernel, iterations=1)
# cv2.namedWindow("erosionada", cv2.WINDOW_NORMAL)
# cv2.imshow('erosionada', imagen_erosionada)

# imagen_apertura = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)
# cv2.namedWindow("apertura", cv2.WINDOW_NORMAL)
# cv2.imshow('apertura', imagen_apertura)

# imagen_clausura = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)
# cv2.namedWindow("clausura", cv2.WINDOW_NORMAL)
# cv2.imshow('clausura', imagen_clausura)

# imagen = cv2.imread('images/hat_image.png', 0)
# imagen_top_hat = cv2.morphologyEx(imagen, cv2.MORPH_TOPHAT, kernel)
# cv2.namedWindow("top_hat", cv2.WINDOW_NORMAL)
# cv2.imshow('top_hat', imagen_top_hat)

# imagen = cv2.imread('images/black_hat.jpg', 0)
# imagen_black_hat = cv2.morphologyEx(imagen, cv2.MORPH_BLACKHAT, kernel)
# cv2.namedWindow("black_hat", cv2.WINDOW_NORMAL)
# cv2.imshow('black_hat', imagen_black_hat)

# from skimage.morphology import skeletonize
# imagen = cv2.imread('images/esqueleto.png', 0)
# _, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)
# esqueleto = skeletonize(imagen_binaria // 255) * 255
# cv2.imshow('Esqueletización', esqueleto.astype(np.uint8))

# imagen = cv2.imread('images/ochos.png', 0)
# _, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)
# imagen_relleno = imagen_binaria.copy()
# cv2.floodFill(imagen_relleno,None, (127, 70), 255)
# cv2.floodFill(imagen_relleno,None, (127, 127), 255)
# cv2.imshow('rellenada', imagen_relleno)

# imagen = cv2.imread('images/cameraman.png', 0)
# gradiente = cv2.morphologyEx(imagen, cv2.MORPH_GRADIENT, kernel)
# cv2.imshow('Gradiente Morfológico', gradiente)

# from skimage.transform import probabilistic_hough_line
# from skimage.feature import canny
# imagen = cv2.imread('images/hough2.png',0)
# lienas_bordes = canny(imagen, sigma=2)
# lines = probabilistic_hough_line(lienas_bordes, threshold=10, line_length=5, line_gap=3)
# image_with_lines = imagen.copy()
# for line in lines:
#     p0, p1 = line
#     cv2.line(image_with_lines, tuple(p0), tuple(p1), (0, 255, 0), 2)
# cv2.imshow('Hough Transform', image_with_lines)

momentos = cv2.moments(imagen)
hu_momentos = cv2.HuMoments(momentos).flatten()
print("Momentos de Hu:")
for i, momento in enumerate(hu_momentos):
    print(f"Hu[{i}] = {momento}")

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow('Original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()