import cv2
import numpy as np

# Carga la imagen desde el archivo
image = cv2.imread("c:/Users/Hp245-User/Desktop/openCV/images/flowers.jpg")

# Divide la imagen en canales BGR
b, g, r = cv2.split(image)

# Concatena los canales en el orden BGR para visualización
image_BGR = cv2.hconcat([r, g, b])

# Define umbrales para cada canal
Sr = r > 150
Sg = g < 40
Sb = b < 40

# Concatena los resultados de los umbrales para visualización
image_S = np.concatenate((Sr, Sg, Sb), axis=1)

# Realiza una operación AND lógica entre los umbrales de los canales
S = np.logical_and(Sr, Sg, Sb)

# Elimina regiones pequeñas de la imagen binaria
(N, M) = S.shape
Q = S
for i in range(N):
    s = np.sum(S[i, :])
    if s < 20:
        Q[i, :] = 0

# Encuentra los límites del objeto segmentado
true_indices = np.argwhere(Q)  # Encuentra los índices de los valores verdaderos en Q
imin, jmin = true_indices.min(axis=0)  # Obtener el índice mínimo en ambas dimensiones
imax, jmax = true_indices.max(axis=0)  # Obtener el índice máximo en ambas dimensiones

# Crea una imagen de bordes del objeto segmentado
E = np.zeros_like(Q, dtype=np.uint8)
for i in range(N):
    for j in range(1, M):
        if Q[i, j] != Q[i, j - 1]:
            E[i, j] = 1
            E[i, j - 1] = 1

for i in range(1, N):
    for j in range(M):
        if Q[i - 1, j] != Q[i, j]:
            E[i, j] = 1
            E[i - 1, j] = 1

salida = image
for i in range(1, N):
    for j in range(M):
        if E[i, j] == 1:
            salida[i,j,:]=[255,0,0]

# Muestra las imágenes resultantes en ventanas
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("RGB Channels", cv2.WINDOW_NORMAL)
cv2.namedWindow("Thresholded RGB", cv2.WINDOW_NORMAL)
cv2.namedWindow("Segmented Object", cv2.WINDOW_NORMAL)
cv2.namedWindow("Segmented Edges", cv2.WINDOW_NORMAL)
cv2.namedWindow("Final", cv2.WINDOW_NORMAL)

cv2.imshow("Original", image)
cv2.imshow("RGB Channels", image_BGR)
cv2.imshow("Thresholded RGB", image_S.astype(np.uint8) * 255)
cv2.imshow("Segmented Object", Q.astype(np.uint8) * 255)
cv2.imshow("Segmented Edges", E.astype(np.uint8) * 255)
cv2.imshow("Final", salida)

cv2.waitKey(0)
cv2.destroyAllWindows()