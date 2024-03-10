import cv2
from op_and import operacion_and
from op_or import operacion_or
from op_xor import operacion_xor
from op_not import operacion_not

img1 = "C:/Users/Hp245-User/Desktop/openCV/images/lc3.tiff"
img2 = "C:/Users/Hp245-User/Desktop/openCV/images/lenacolor.png"

imagen1 = cv2.imread(img1)
imagen2 = cv2.imread(img2)

imagen1 = cv2.resize(imagen1, (300, 300))
imagen2 = cv2.resize(imagen2, (300, 300))

# crear ventana
cv2.namedWindow("Imagen 1 y 2", cv2.WINDOW_NORMAL)

# concatenar horizontalmente
imagenes = cv2.hconcat([imagen1, imagen2])

cv2.imshow("Imagen 1 y 2", imagenes)

# resultado = operacion_and(img1, img2)
# cv = cv2.bitwise_and(imagen1, imagen2)
# cv2.imshow('Imagen And', resultado)
# cv2.imshow('Imagen And CV', cv)

# resultado = operacion_or(img1, img2)
# cv = cv2.bitwise_or(imagen1, imagen2)
# cv2.imshow('Imagen Or', resultado)
# cv2.imshow('Imagen Or CV', cv)

# resultado = operacion_xor(img1, img2)
# cv = cv2.bitwise_xor(imagen1, imagen2)
# cv2.imshow('Imagen XOr', resultado)
# cv2.imshow('Imagen XOr CV', cv)

resultado = operacion_not(img1)
cv = cv2.bitwise_not(imagen1)
cv2.imshow('Imagen NOT', resultado)
cv2.imshow('Imagen NOT CV', cv)

cv2.waitKey(0)
cv2.destroyAllWindows()