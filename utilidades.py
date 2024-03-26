import cv2
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from PyQt6.QtGui import QPixmap

def validar_2_imagenes(imagen1, imagen2):
    if imagen1 is None or imagen2 is None:
        QMessageBox.warning(None, "Advertencia", "Por favor, seleccione ambas imágenes antes de realizar la operación.")
        return False
    return True

def validar_1_imagen(imagen1):
    if imagen1 is None:
        QMessageBox.warning(None, "Advertencia", "Por favor, seleccione la imagen 1 antes de realizar la operación.")
        return False
    return True

def mostrar_imagen(ruta_imagen, etiqueta_mostrar, imagen):
    imagen_cargada = cv2.imread(ruta_imagen)

    if imagen_cargada is None:
        QMessageBox.warning(None, "Error", "No se pudo cargar la imagen.")
    else:
        etiqueta_mostrar.setPixmap(QPixmap(ruta_imagen))
        etiqueta_mostrar.setScaledContents(True)
        imagen = imagen_cargada

def seleccionarYmostrar(etiqueta, imagen):
    file_dialog = QFileDialog(None)
    ruta_imagen, _ = file_dialog.getOpenFileName(None, "Seleccionar imagen", "", "Image Files (*.png *.jpg *.bmp *.gif)")

    if ruta_imagen:
        imagen_cargada = cv2.imread(ruta_imagen)
        if imagen_cargada is not None:
            etiqueta.setPixmap(QPixmap(ruta_imagen))
            etiqueta.setScaledContents(True)
            imagen = imagen_cargada
    return imagen
