import sys
import cv2
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.uic import loadUi

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import  QFileDialog, QMessageBox

from utilidades import validar_2_imagenes, validar_1_imagen, mostrar_imagen, seleccionarYmostrar

from numerodialog import NumeroDialog
from mododialog import ModoDialog

from operaciones_basicas.suma import sum_images
from operaciones_basicas.resta import rest_images
from operaciones_basicas.multi import multiplicar_imagen
from operaciones_basicas.division import division_imagen
from operaciones_basicas.negativo import obtener_negativo

from operaciones_logicas.op_and import operacion_and
from operaciones_logicas.op_or import operacion_or
from operaciones_logicas.op_xor import operacion_xor
from operaciones_logicas.op_not import operacion_not

class miApp(QMainWindow):

    def __init__(self):
        super().__init__(flags=Qt.WindowType.Window)
        loadUi("./main.ui", self)  # Carga la interfaz de usuario desde el archivo
        self.imagen1=None
        self.imagen2=None

        # Conecta los botones al método con funciones lambda para pasar la etiqueta
        self.btn_mostrar_img1.clicked.connect(lambda: self.mostrar_imagen_y_actualizar(self.lb_imagen1, 'imagen1'))
        self.btn_mostrar_img2.clicked.connect(lambda: self.mostrar_imagen_y_actualizar(self.lb_imagen2, 'imagen2'))

        self.btn_suma.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.restar)
        self.btn_multiplicacion.clicked.connect(self.multiplicar)
        self.btn_division.clicked.connect(self.dividir)

        self.btn_negativo.clicked.connect(self.negativo)

        self.btn_and.clicked.connect(self.hacer_and)
        self.btn_or.clicked.connect(self.hacer_or)
        self.btn_xor.clicked.connect(self.hacer_xor)
        self.btn_not.clicked.connect(self.hacer_not)

    def mostrar_imagen_y_actualizar(self, etiqueta, imagen):
        if imagen == 'imagen1':
            self.imagen1 = seleccionarYmostrar(etiqueta, getattr(self, imagen))
        elif imagen == 'imagen2':
            self.imagen2 = seleccionarYmostrar(etiqueta, getattr(self, imagen))

    def sumar(self):
        if not validar_2_imagenes(self.imagen1, self.imagen2):
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
        if not validar_2_imagenes(self.imagen1, self.imagen2):
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
        if not validar_1_imagen(self.imagen1):
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
        if not validar_1_imagen(self.imagen1):
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

    def negativo(self):
        if not validar_1_imagen(self.imagen1):
            return

        if self.check_gris.isChecked():
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
        else:
            img1 = self.imagen1
        r = obtener_negativo(img1)
        cv2.namedWindow("negtativo", cv2.WINDOW_NORMAL)
        cv2.imshow("negtativo",r)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def hacer_and(self):
        if not validar_2_imagenes(self.imagen1, self.imagen2):
            return

        if self.check_gris.isChecked():
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY) if self.imagen1 is not None else None
            img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY) if self.imagen2 is not None else None
        else:
            img1 = self.imagen1
            img2 = self.imagen2
        r = operacion_and(img1, img2)
        cv2.namedWindow("AND", cv2.WINDOW_NORMAL)
        cv2.imshow("AND",r)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def hacer_or(self):
        if not validar_2_imagenes(self.imagen1, self.imagen2):
            return

        if self.check_gris.isChecked():
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY) if self.imagen1 is not None else None
            img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY) if self.imagen2 is not None else None
        else:
            img1 = self.imagen1
            img2 = self.imagen2
        r = operacion_or(img1, img2)
        cv2.namedWindow("OR", cv2.WINDOW_NORMAL)
        cv2.imshow("OR",r)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def hacer_xor(self):
        if not validar_2_imagenes(self.imagen1, self.imagen2):
            return

        if self.check_gris.isChecked():
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY) if self.imagen1 is not None else None
            img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY) if self.imagen2 is not None else None
        else:
            img1 = self.imagen1
            img2 = self.imagen2
        r = operacion_xor(img1, img2)
        cv2.namedWindow("XOR", cv2.WINDOW_NORMAL)
        cv2.imshow("XOR",r)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def hacer_not(self):
        if not validar_1_imagen(self.imagen1):
            return
        r = operacion_not(self.imagen1)
        cv2.namedWindow("NOT", cv2.WINDOW_NORMAL)
        cv2.imshow("NOT",r)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = miApp()
    ventana.show()
    sys.exit(app.exec())
