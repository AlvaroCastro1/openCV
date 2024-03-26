import sys
import cv2
import matplotlib.pyplot as plt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.uic import loadUi

from cuadros_dialogo import DialogoDosNumeros, DialogoUnNumero, DialogoDosUmbrales, DialogoTamanoKernel, DialogoNumeroSegmentaciones

from utilidades import validar_2_imagenes, validar_1_imagen, seleccionarYmostrar

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

from transformaciones.escalado import interpolacion_imagen
from transformaciones.traslacion import traslacion

from practica2.grises import histograma_gris
from practica2.color import histograma_color

from Segmentacion.umbrales import umbral, umbral_invertido, umbral_porNivel, umbral_porNivel_invertido, umbral_por2puntos, umbral_por2puntos_invertido

from filtros.media import filtro_media
from filtros.mediana import filtro_mediana

from conversiones.color2gray import convertir_a_gris_promedio, convertir_a_gris_formula

from kmeans.kmeans import segmentar_con_kmeans

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

        self.btn_escalado.clicked.connect(self.hacer_escalado)
        self.btn_traslacion.clicked.connect(self.hacer_traslacion)

        self.btn_hist_color.clicked.connect(self.histograma_a_color)
        self.btn_hist_BN.clicked.connect(self.histograma_a_gris)

        self.btn_umbral.clicked.connect(self.hacer_umbral)
        self.btn_umbral_Invertido.clicked.connect(self.hacer_umbral_Invertido)
        self.btn_u_porNivel.clicked.connect(self.hacer_u_porNivel)
        self.btn_u_porNivel_Invertido.clicked.connect(self.hacer_u_porNivel_Invertido)
        self.btn_u_por2puntos.clicked.connect(self.hacer_u_por2puntos)
        self.btn_u_por2puntos_Invertido.clicked.connect(self.hacer_u_por2puntos_invertido)

        self.btn_filtro_media.clicked.connect(self.hacer_filtro_media)
        self.btn_filtro_mediana.clicked.connect(self.hacer_filtro_mediana)
        
        self.btn_conv_formula.clicked.connect(self.hacer_conv_formula)
        self.btn_conv_promedio.clicked.connect(self.hacer_conv_promedio)

        self.btn_kmeans.clicked.connect(self.hacer_segm_kmeans)

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
                img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
                img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY)
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
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY)
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
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY)
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
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            img2 = cv2.cvtColor(self.imagen2, cv2.COLOR_RGB2GRAY)
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

    def hacer_escalado(self):
        if not validar_1_imagen(self.imagen1):
            return

        dialogo = DialogoDosNumeros(self)
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            escala_x, escala_y = float(dialogo.textbox1.text()), float(dialogo.textbox2.text())

            if self.check_gris.isChecked():
                img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                img = self.imagen1

            r = interpolacion_imagen(img, 'bilineal', escala_x=escala_x, escala_y=escala_y)
            cv2.imshow("Escalado", r)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_traslacion(self):
        if not validar_1_imagen(self.imagen1):
            return

        dialogo = DialogoDosNumeros(self)
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            traslacion_x, traslacion_y = float(dialogo.textbox1.text()), float(dialogo.textbox2.text())

            if self.check_gris.isChecked():
                img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                img = self.imagen1

            r = traslacion(img, traslacion_x=traslacion_x, traslacion_y=traslacion_y)
            cv2.namedWindow("Traslacion", cv2.WINDOW_NORMAL)
            cv2.imshow("Traslacion", r)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def histograma_a_color(self):
        if not validar_1_imagen(self.imagen1):
            return
        # Convertir a color si la imagen es en escala de grises
        if len(self.imagen1.shape) == 2:
            imagen = cv2.cvtColor(self.imagen1, cv2.COLOR_GRAY2BGR)
        else:
            imagen = self.imagen1

        conteo_colores = histograma_color(imagen)

        # Crear una figura con dos subplots: uno para la imagen y otro para el histograma
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        ax1.imshow(cv2.cvtColor(self.imagen1, cv2.COLOR_BGR2RGB))
        ax1.set_title('Imagen')
        ax1.axis('off')

        # Trazar el histograma en el segundo subplot
        ax2.plot(list(conteo_colores['R'].keys()), list(conteo_colores['R'].values()), color='red', label="rojo")
        ax2.plot(list(conteo_colores['G'].keys()), list(conteo_colores['G'].values()), color='green', label="verde")
        ax2.plot(list(conteo_colores['B'].keys()), list(conteo_colores['B'].values()), color='blue', label="azul")
        ax2.set_title('Histograma de la imagen')
        ax2.set_xlabel('Valor de intensidad')
        ax2.set_ylabel('Frecuencia')
        ax2.legend()
        ax2.grid(True)

        plt.show()

    def histograma_a_gris(self):
        if not validar_1_imagen(self.imagen1):
            return

        # Convertir a escala de grises si la imagen es a color
        if len(self.imagen1.shape) == 3:
            imagen = cv2.cvtColor(self.imagen1, cv2.COLOR_BGR2GRAY)
        else:
            imagen = self.imagen1

        conteo_colores = histograma_gris(imagen)

        # Crear una figura con dos subplots: uno para la imagen y otro para el histograma
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Mostrar la imagen en el primer subplot
        ax1.imshow(imagen, cmap='gray')
        ax1.set_title('Imagen en escala de grises')
        ax1.axis('off')

        # Trazar el histograma en el segundo subplot
        ax2.bar(conteo_colores.keys(), conteo_colores.values(), color='gray')
        ax2.set_title('Histograma en escala de grises')
        ax2.set_xlabel('Valor de intensidad')
        ax2.set_ylabel('Frecuencia')

        # Ajustar automáticamente el tamaño de la ventana
        plt.gcf().set_size_inches(12, 6)

        # Mostrar los subplots
        plt.tight_layout()
        plt.show()

    def hacer_umbral(self):
        if not validar_1_imagen(self.imagen1):
            return

        dialogo = DialogoUnNumero()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            # Obtener el número ingresado del cuadro de diálogo
            numero = int(dialogo.textbox.text())
            if len(self.imagen1.shape) == 3:
                img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                img = self.imagen1
            umb_img = umbral(img, numero)
            cv2.namedWindow("umbral", cv2.WINDOW_NORMAL)
            cv2.imshow("umbral", umb_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_umbral_Invertido(self):
        if not validar_1_imagen(self.imagen1):
            return

        dialogo = DialogoUnNumero()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            # Obtener el número ingresado del cuadro de diálogo
            numero = int(dialogo.textbox.text())
            if len(self.imagen1.shape) == 3:
                img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                img = self.imagen1
            umb_img = umbral_invertido(img, numero)
            cv2.namedWindow("umbral Invertido", cv2.WINDOW_NORMAL)
            cv2.imshow("umbral Invertido", umb_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_u_porNivel(self):
        if not validar_1_imagen(self.imagen1):
            return

        dialogo = DialogoUnNumero()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            # Obtener el número ingresado del cuadro de diálogo
            numero = int(dialogo.textbox.text())
            if len(self.imagen1.shape) == 3:
                img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                img = self.imagen1
            umb_img = umbral_porNivel(img, numero)
            cv2.namedWindow("umbral por Nivel", cv2.WINDOW_NORMAL)
            cv2.imshow("umbral por Nivel", umb_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_u_porNivel_Invertido(self):
        if not validar_1_imagen(self.imagen1):
            return

        dialogo = DialogoUnNumero()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            # Obtener el número ingresado del cuadro de diálogo
            numero = int(dialogo.textbox.text())
            if len(self.imagen1.shape) == 3:
                img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                img = self.imagen1
            umb_img = umbral_porNivel_invertido(img, numero)
            cv2.namedWindow("umbral por Nivel", cv2.WINDOW_NORMAL)
            cv2.imshow("umbral por Nivel", umb_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_u_por2puntos(self):
        if not validar_1_imagen(self.imagen1):
            return

        dialogo = DialogoDosUmbrales()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            # Obtener el número ingresado del cuadro de diálogo
            umbral1 = int(dialogo.textbox1.text())
            umbral2 = int(dialogo.textbox2.text())
            if len(self.imagen1.shape) == 3:
                img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                img = self.imagen1
            umb_img = umbral_por2puntos(img, umbral1, umbral2)
            cv2.namedWindow("umbral por 2 puntos", cv2.WINDOW_NORMAL)
            cv2.imshow("umbral por 2 puntos", umb_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_u_por2puntos_invertido(self):
        if not validar_1_imagen(self.imagen1):
            return

        dialogo = DialogoDosUmbrales()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            # Obtener el número ingresado del cuadro de diálogo
            umbral1 = int(dialogo.textbox1.text())
            umbral2 = int(dialogo.textbox2.text())
            if len(self.imagen1.shape) == 3:
                img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                img = self.imagen1
            umb_img = umbral_por2puntos_invertido(img, umbral1, umbral2)
            cv2.namedWindow("umbral por 2 puntos invertido", cv2.WINDOW_NORMAL)
            cv2.imshow("umbral por 2 puntos invertido", umb_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_filtro_media(self):
        if not validar_1_imagen(self.imagen1):
            return
        if self.check_gris.isChecked():
            img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
        else:
            img = self.imagen1

        dialogo = DialogoTamanoKernel()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            tamano_kernel = int(dialogo.textbox.text())

            imagen_filtrada_personalizada = filtro_media(img, tamano_kernel)
            cv2.namedWindow('Imagen Filtrada media', cv2.WINDOW_NORMAL)
            cv2.imshow('Imagen Filtrada media', imagen_filtrada_personalizada)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_filtro_mediana(self):
        if not validar_1_imagen(self.imagen1):
            return
        if self.check_gris.isChecked():
            img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
        else:
            img = self.imagen1

        dialogo = DialogoTamanoKernel()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            tamano_kernel = int(dialogo.textbox.text())

            imagen_filtrada_personalizada = filtro_mediana(img, tamano_kernel)
            cv2.namedWindow('Imagen Filtrada mediana', cv2.WINDOW_NORMAL)
            cv2.imshow('Imagen Filtrada mediana', imagen_filtrada_personalizada)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hacer_conv_formula(self):
        if not validar_1_imagen(self.imagen1):
            return
        if (len(self.imagen1.shape)==3):
            img = self.imagen1
        else:
            img = cv2.cvtColor(self.imagen1, cv2.COLOR_GRAY2RGB)

        imagen_a_gris = convertir_a_gris_formula(img)
        cv2.namedWindow('Imagen en grises', cv2.WINDOW_NORMAL)
        cv2.imshow('Imagen en grises', imagen_a_gris)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def hacer_conv_promedio(self):
        if not validar_1_imagen(self.imagen1):
            return
        if (len(self.imagen1.shape)==3):
            img = self.imagen1
        else:
            img = cv2.cvtColor(self.imagen1, cv2.COLOR_GRAY2RGB)

        imagen_a_gris = convertir_a_gris_promedio(img)
        cv2.namedWindow('Imagen en grises', cv2.WINDOW_NORMAL)
        cv2.imshow('Imagen en grises', imagen_a_gris)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def hacer_segm_kmeans(self):
        if not validar_1_imagen(self.imagen1):
            return

        if self.check_gris.isChecked():
            img = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
        else:
            img = self.imagen1

        dialogo = DialogoNumeroSegmentaciones()
        
        if dialogo.exec() == QDialog.DialogCode.Accepted:
            num_seg = int(dialogo.textbox.text())
            imagen_segm = segmentar_con_kmeans(img, n_clusters=num_seg)
            cv2.namedWindow('Imagen segmentada con Kmeans', cv2.WINDOW_NORMAL)
            cv2.imshow('Imagen segmentada con Kmeans', imagen_segm)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = miApp()
    ventana.show()
    sys.exit(app.exec())
