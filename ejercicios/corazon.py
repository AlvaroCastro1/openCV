import cv2
import numpy as np

# Cargar la foto
foto = cv2.imread("safeimagekit-400x400-image.png")

# crear un lienzo
img = np.zeros((400, 400, 3), dtype=np.uint8)

radio = 50

# elipse izq
cv2.ellipse(img, (151, 185), (radio, radio), 180, 0, 180, (0, 255, 0), -1)

# elipse der
cv2.ellipse(img, (249, 185), (radio, radio), 180, 0, 180, (0, 255, 0), -1)

# triangulo invertido
pts = np.array([[100, 185], [200, 340], [300, 185]], np.int32)

# rellenar el triangulo
cv2.fillPoly(img, [pts], color=(0, 255, 0))

# colocar los pixeles de la img a los pixeles color verde
img[img[:, :, 1] == 255] = foto[img[:, :, 1] == 255]


cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
