import cv2
import numpy as np

imagen = cv2.imread("C:/Users/Hp245-User/Desktop/openCV/images/frutos_rojos.png")

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", imagen)

b, g, r = cv2.split(imagen)

image_BGR = cv2.hconcat([r, g, b])
cv2.namedWindow("RGB canales", cv2.WINDOW_NORMAL)
cv2.imshow("RGB canales", image_BGR)


# Define umbrales para cada canal
Sr = r > 150
Sg = g < 120
Sb = b < 175

imagen_salida_humbrales = np.concatenate((Sr, Sg, Sb), axis=1)
cv2.namedWindow("Canales con humbral", cv2.WINDOW_NORMAL)
cv2.imshow("Canales con humbral", imagen_salida_humbrales.astype(np.uint8) * 255)

imagen_and = np.logical_and(Sr, Sg, Sb)

# Elimina regiones pequeñas de la imagen binaria
(N, M) = imagen_and.shape
frutos = imagen_and
for i in range(N):
    s = np.sum(imagen_and[i, :])
    if s < 20:
        frutos[i, :] = 0

cv2.namedWindow("Frutos Segmentados Bin", cv2.WINDOW_NORMAL)
cv2.imshow("Frutos Segmentados Bin", frutos.astype(np.uint8) * 255)

# Encuentra los límites del objeto segmentado
true_indices = np.argwhere(frutos)  # Encuentra los índices de los valores verdaderos en Q
imin, jmin = true_indices.min(axis=0)  # Obtener el índice mínimo en ambas dimensiones
imax, jmax = true_indices.max(axis=0)  # Obtener el índice máximo en ambas dimensiones

# Crea una imagen de bordes del objeto segmentado
bordes_frutos = np.zeros_like(frutos, dtype=np.uint8)
for i in range(N):
    for j in range(1, M):
        if frutos[i, j] != frutos[i, j - 1]:
            bordes_frutos[i, j] = 1
            bordes_frutos[i, j - 1] = 1

cv2.namedWindow("Borde de Frutos", cv2.WINDOW_NORMAL)
cv2.imshow("Borde de Frutos", bordes_frutos.astype(np.uint8) * 255)

for i in range(1, N):
    for j in range(M):
        if frutos[i - 1, j] != frutos[i, j]:
            bordes_frutos[i, j] = 1
            bordes_frutos[i - 1, j] = 1

imagen_original_bordes = imagen
for i in range(1, N):
    for j in range(M):
        if bordes_frutos[i, j] == 1:
            imagen_original_bordes[i,j,:]=[255,0,0]

cv2.namedWindow("Final", cv2.WINDOW_NORMAL)
cv2.imshow("Final", imagen_original_bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()