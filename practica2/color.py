import cv2
import matplotlib.pyplot as plt

def histograma_color(imagen):

    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
        return

    canales = cv2.split(imagen) #BGR
    canales = [canales[2], canales[1], canales[0]] # R G B
    nombres_canales = ['Canal Rojo', 'Canal Verde', 'Canal Azul']

    alto, ancho, _ = imagen.shape

    conteo_colores = {
        'R': {},
        'G': {},
        'B': {}
    }

    # a cada pixel añadir frecuencia
    for i in range(alto):
        for j in range(ancho):
            intensidades = imagen[i, j]
            for canal, intensidad in enumerate(intensidades):
                if intensidad in conteo_colores[('R', 'G', 'B')[canal]]:
                    conteo_colores[('R', 'G', 'B')[canal]][intensidad] += 1
                else:
                    conteo_colores[('R', 'G', 'B')[canal]][intensidad] = 1

    # añadir todos(0 a 255)
    for canal in conteo_colores:
        for valor in range(256):
            if valor not in conteo_colores[canal]:
                conteo_colores[canal][valor] = 0

    # ordenar el diccionario por valor de intensidad
    for canal in conteo_colores:
        conteo_colores[canal] = dict(sorted(conteo_colores[canal].items()))
    return conteo_colores


# Ejemplo de uso
# imagen = cv2.imread('C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png')
# nombres_canales = ['Canal Rojo', 'Canal Verde', 'Canal Azul']
# canales = cv2.split(imagen) #BGR
# conteo_colores = visualizar_histograma_y_canales('C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png')

# # subplots
# plt.figure(figsize=(14, 6))

# # Subplots para los histogramas
# for i, canal in enumerate(conteo_colores):
#     plt.subplot(2, 3, i+1)
#     plt.bar(conteo_colores[canal].keys(), conteo_colores[canal].values(), color=canal.lower())
#     plt.title(f'Histograma {nombres_canales[i]}')
#     plt.xlabel('Valor de intensidad')
#     plt.ylabel('Frecuencia')

# # Mostrar cada canal en un subplot
# for i, canal in enumerate(canales):
#     plt.subplot(2, 3, i+4)
#     plt.imshow(canal, cmap='gray')
#     plt.title(nombres_canales[i])

# # Ajustar automáticamente el tamaño de la ventana
# plt.gcf().set_size_inches(12, 6)

# # Mostrar los subplots
# plt.tight_layout()
# plt.show()
if __name__ == "__main__":
    image_path = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"

    conteo_colores = histograma_color(image_path)
    nombres_canales = ['Canal Rojo', 'Canal Verde', 'Canal Azul']
    plt.figure(figsize=(8, 6))

    plt.plot(list(conteo_colores['R'].keys()), list(conteo_colores['R'].values()), color='red', label="rojo")
    plt.plot(list(conteo_colores['G'].keys()), list(conteo_colores['G'].values()), color='green', label="verde")
    plt.plot(list(conteo_colores['B'].keys()), list(conteo_colores['B'].values()), color='blue', label="azul")

    plt.title('Histograma de la imagen')
    plt.xlabel('Valor de intensidad')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(True)

    plt.show()