import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QVBoxLayout, QComboBox
from PyQt6.QtWidgets import  QPushButton, QDialog, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi

import cv2
from operaciones_basicas.suma import sum_images
from operaciones_basicas.resta import rest_images
from operaciones_basicas.multi import multiplicar_imagen
from operaciones_basicas.division import division_imagen

class ModoDialog(QDialog):
    #clase para seleccionar modos
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setWindowTitle("Seleccionar Modo")
        self.setModal(True)

        self.label = QLabel("Seleccione el modo de suma:")
        layout.addWidget(self.label)

        self.combo_box = QComboBox()
        self.combo_box.addItem("truncar")
        self.combo_box.addItem("ciclico")
        self.combo_box.addItem("promedio")
        layout.addWidget(self.combo_box)

        self.btn_confirmar = QPushButton("Confirmar")
        self.btn_confirmar.clicked.connect(self.accept)
        layout.addWidget(self.btn_confirmar)

        self.setLayout(layout)

    def obtener_modo(self):
        return self.combo_box.currentText()

class NumeroDialog(QDialog):
    # Clase para ingresar un número flotante
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setWindowTitle("Ingresar Número")
        self.setModal(True)

        self.label = QLabel("Ingrese un número flotante:")
        layout.addWidget(self.label)

        self.float_edit = QLineEdit()
        self.float_edit.setPlaceholderText("Ej. 3.14")
        layout.addWidget(self.float_edit)

        self.btn_confirmar = QPushButton("Confirmar")
        self.btn_confirmar.clicked.connect(self.accept)
        layout.addWidget(self.btn_confirmar)

        self.setLayout(layout)

    def obtener_numero(self):
        try:
            return float(self.float_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un número flotante válido.")
            return None
class miApp(QMainWindow):

    def __init__(self):
        super().__init__(flags=Qt.WindowType.Window)
        loadUi("./main.ui", self)  # Carga la interfaz de usuario desde el archivo
        self.imagen1=None
        self.imagen2=None

        # Conecta los botones al método con funciones lambda para pasar la etiqueta
        self.btn_mostrar_img1.clicked.connect(lambda: self.seleccionarYmostrar(self.lb_imagen1))
        self.btn_mostrar_img2.clicked.connect(lambda: self.seleccionarYmostrar(self.lb_imagen2))
        self.btn_suma.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.restar)
        self.btn_multiplicacion.clicked.connect(self.multiplicar)
        self.btn_division.clicked.connect(self.dividir)

    def sumar(self):
        if not self.validar_2_imagenes():
            return

        modo_dialog = ModoDialog()
        if modo_dialog.exec() == QDialog.DialogCode.Accepted:
            modo = modo_dialog.obtener_modo()
            if self.check_gris.isChecked():
                img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY) if self.imagen1 is not None else None
                img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY) if self.imagen2 is not None else None
            else:
                img1 = self.imagen1
                img2 = self.imagen2
            r = sum_images(img1, img2, modo)
            cv2.namedWindow("suma", cv2.WINDOW_NORMAL)
            cv2.imshow("suma",r)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def restar(self):
        if not self.validar_2_imagenes():
            return

        modo_dialog = ModoDialog()
        if modo_dialog.exec() == QDialog.DialogCode.Accepted:
            modo = modo_dialog.obtener_modo()
            if self.check_gris.isChecked():
                img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
                img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY)
            else:
                img1 = self.imagen1
                img2 = self.imagen2
            r = rest_images(img1, img2, modo)
            cv2.namedWindow("resta", cv2.WINDOW_NORMAL)
            cv2.imshow("resta",r)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def multiplicar(self):
        if not self.validar_1_imagen():
            return

        modo_dialog = ModoDialog()
        if modo_dialog.exec() == QDialog.DialogCode.Accepted:
            modo = modo_dialog.obtener_modo()

            numero_dialog = NumeroDialog()
            if numero_dialog.exec() == QDialog.DialogCode.Accepted:
                numero = numero_dialog.obtener_numero()
                if numero is not None:
                    if self.check_gris.isChecked():
                        img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
                    else:
                        img1 = self.imagen1
                    r = multiplicar_imagen(img1, numero, modo)
                    cv2.namedWindow("multiplicacion", cv2.WINDOW_NORMAL)
                    cv2.imshow("multiplicacion",r)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

    def dividir(self):
        if not self.validar_1_imagen():
            return

        modo_dialog = ModoDialog()
        if modo_dialog.exec() == QDialog.DialogCode.Accepted:
            modo = modo_dialog.obtener_modo()

            numero_dialog = NumeroDialog()
            if numero_dialog.exec() == QDialog.DialogCode.Accepted:
                numero = numero_dialog.obtener_numero()
                if numero is not None:
                    if self.check_gris.isChecked():
                        img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
                    else:
                        img1 = self.imagen1
                    r = division_imagen(img1, numero, modo)
                    cv2.namedWindow("division", cv2.WINDOW_NORMAL)
                    cv2.imshow("division",r)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

    def validar_2_imagenes(self):
        if self.imagen1 is None or self.imagen2 is None:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione ambas imágenes antes de realizar la operación.")
            return False
        return True

    def validar_1_imagen(self):
        if self.imagen1 is None:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione la imagen 1 antes de realizar la operación.")
            return False
        return True

    def mostrar_imagen(self, ruta_imagen, etiqueta_mostrar):
        # Intenta cargar la imagen
        imagen = cv2.imread(ruta_imagen)

        if imagen is None:
            QMessageBox.warning(self, "Error", "No se pudo cargar la imagen.")
        else:
            # Si la imagen se carga correctamente, asigna la imagen al QLabel
            etiqueta_mostrar.setPixmap(QPixmap(ruta_imagen))
            etiqueta_mostrar.setScaledContents(True)

            # Asigna la imagen a la variable correspondiente (imagen1 o imagen2)
            if etiqueta_mostrar == self.lb_imagen1:
                self.imagen1 = imagen
            elif etiqueta_mostrar == self.lb_imagen2:
                self.imagen2 = imagen

    def seleccionarYmostrar(self, etiqueta):
        # Abre un cuadro de diálogo de archivo para seleccionar una imagen
        file_dialog = QFileDialog(self)
        ruta_imagen, _ = file_dialog.getOpenFileName(self, "Seleccionar imagen", "", "Image Files (*.png *.jpg *.bmp *.gif)")

        if ruta_imagen:  # Si el usuario seleccionó una imagen, muéstrala
            self.mostrar_imagen(ruta_imagen, etiqueta)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = miApp()
    ventana.show()
    sys.exit(app.exec())
