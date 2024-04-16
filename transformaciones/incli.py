import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog

def obtener_angulo():
    root = tk.Tk()
    root.withdraw()  
    angulo = simpledialog.askfloat("Ángulo", "Ingrese el ángulo de inclinación (en grados):")
    return angulo

# Método para la inclinación vertical
def inclinar_vertical(image, angulo):
    theta_vertical = angulo * (np.pi / 180)  
    matrix_vertical = np.float32([[1, 0, 0],
                                  [np.tan(theta_vertical), 1, 0]])
    inclinada_vertical = cv2.warpAffine(image, matrix_vertical, (image.shape[1], image.shape[0]))
    return inclinada_vertical

# Método para la inclinación horizontal
def inclinar_horizontal(image, angulo):
    theta_horizontal = angulo * (np.pi / 180) 
    matrix_horizontal = np.float32([[1, np.tan(theta_horizontal), 0],
                                    [0, 1, 0]])
    inclinada_horizontal = cv2.warpAffine(image, matrix_horizontal, (image.shape[1], image.shape[0]))
    return inclinada_horizontal


if __name__ == "__main__":
    #------------------------------
    image = cv2.imread("lorito.png")

    angulo = obtener_angulo()

    inclinada_vertical = inclinar_vertical(image, angulo)
    inclinada_horizontal = inclinar_horizontal(image, angulo)

    cv2.imwrite("lorito_inclinada_vertical.png", inclinada_vertical)
    cv2.imwrite("lorito_inclinada_horizontal.png", inclinada_horizontal)

    #-----------Mostrar las imagenes
    cv2.imshow("Inclinada Verticalmente", inclinada_vertical)
    cv2.imshow("Inclinada Horizontalmente", inclinada_horizontal)
    cv2.waitKey(0)

    # Cerrar todas las ventanas
    cv2.destroyAllWindows()
