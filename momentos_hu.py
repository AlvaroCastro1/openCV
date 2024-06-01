import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def momentosHU(image):
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    _, resultado = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    moments = cv2.moments(resultado)

    momentos_ = cv2.HuMoments(moments).flatten()

    return momentos_

def crear_tabla(cabecera, data):
    # DataFrame de pandas con los datos
    df = pd.DataFrame(data, columns=cabecera)
    
    # matplotlib
    fig, ax = plt.subplots()
    ax.axis('off')
    # usar la tabla
    tabla = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)
    tabla.scale(1.2, 1.2)

    plt.title('Momentos de Hu')
    plt.show()

def main(image1, image2):
    # Calcular los momentos de Hu para ambas imágenes
    momentos_1 = momentosHU(image1)
    momentos_2 = momentosHU(image2)

    # Preparar los datos para la tabla
    cabecera = ["Momentos", "Imagen 1", "Imagen 2"]
    datos = []

    for i in range(len(momentos_1)):
        row = [f"# {i + 1}", f"{momentos_1[i]:.2e}", f"{momentos_2[i]:.2e}"]
        datos.append(row)


    crear_tabla(cabecera, datos)

if __name__ == "__main__":
    image1 = cv2.imread('images/S.png')
    image2 = cv2.imread('imagen_resultante.jpg')
    main(image1, image2)
