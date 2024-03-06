import cv2

imagen = cv2.imread("lenacolor.png")
cv2.imshow("Prueba de imagen", imagen)
cv2.waitKey(0)
cv2.imwrite("lena2.png", imagen)
cv2.destroyAllWindows()
