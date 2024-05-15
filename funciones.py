import os
import sys
import cv2
import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.uic import loadUi
import tkinter as tk
from tkinter import simpledialog
from tkinter import Scale, Button
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

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
from transformaciones.contraste import contraste_operacion, ope_contraste_bw
from transformaciones.incli import obtener_angulo, inclinar_vertical, inclinar_horizontal
from transformaciones.rotacion import Rotacion_imagenes
from transformaciones.espejo import ImageManipulator
from transformaciones.espejonegro import Espejo_transformar

from bordes.canny import suavizar_imagen, calcular_gradientes, suprimir_no_maximos,umbralizar
from bordes.sobel import convolucion_sobel, detectar_bordes_sobel, plot_images
from bordes.prewitt import convolucion
from bordes.gradiente import detectar_bordes

from practica2.grises import histograma_gris
from practica2.color import histograma_color

from Segmentacion.umbrales import umbral, umbral_invertido, umbral_porNivel, umbral_porNivel_invertido, umbral_por2puntos, umbral_por2puntos_invertido

from filtros.media import filtro_media
from filtros.mediana import filtro_mediana

from conversiones.color2gray import convertir_a_gris_promedio, convertir_a_gris_formula

from kmeans.kmeans import segmentar_con_kmeans

from guardar import guardar_imagen_ruta

from morfologicas.op_top_hat import top_hat
from morfologicas.op_black_hat import black_hat
from morfologicas.op_esqueleto import esqueletonizar
from morfologicas.op_rellenar_bordes import rellenar_formas

from conversiones_rgb.conver import rgb2bgr, rgb2cmyk, rgb2hsv

from morfologicas.Hough import imagenHough

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

        self.btn_contraste.clicked.connect(self.aplicar_contraste)
        self.btn_inclinacion_vertical.clicked.connect(self.aplicar_inclinacion_vertical)
        self.btn_inclinacion_hori.clicked.connect(self.aplicar_inclinacion)
        self.btn_rotacion.clicked.connect(self.aplicar_rotacion)
        self.btn_espejo.clicked.connect(self.aplicar_espejo)

        self.btn_borde_canny.clicked.connect(self.aplicar_canny)
        self.btn_borde_sobel.clicked.connect(self.aplicar_sobel)
        self.btn_borde_prewitt.clicked.connect(self.aplicar_prewitt)
        self.btn_borde_gradiente.clicked.connect(self.aplicar_gradiente)

        self.btn_top.clicked.connect(self.aplicar_top_hat)
        self.btn_black.clicked.connect(self.aplicar_black_hat)
        self.btn_esqueleto.clicked.connect(self.aplicar_esqueleto)
        self.btn_rellenar.clicked.connect(self.aplicar_relleno)

        self.btn_rgb.clicked.connect(self.convertir_rgb)
        self.btn_bgr.clicked.connect(self.convertir_bgr)
        self.btn_cmyk.clicked.connect(self.convertir_cmyk)
        self.btn_hsv.clicked.connect(self.convertir_hsv)

        self.btn_transformada.clicked.connect(self.aplicar_transformada)
#-------------------------------------FUNCIONES DE LAS DIFERENTES OPERACIONES-------------------------------------------------------------
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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            
            if key == ord('s'):
                guardar_imagen_ruta(r)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            
            if key == ord('s'):
                guardar_imagen_ruta(r)

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
                    key = cv2.waitKey(0)  
                    cv2.destroyAllWindows()
                    
                    if key == ord('s'):
                        guardar_imagen_ruta(r)

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
                    key = cv2.waitKey(0)  
                    cv2.destroyAllWindows()
                    
                    if key == ord('s'):
                        guardar_imagen_ruta(r)

    def negativo(self):
        if not validar_1_imagen(self.imagen1):
            return
        if self.check_gris.isChecked():
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
          
        else:
            img1 = self.imagen1
        r = obtener_negativo(img1)
        cv2.namedWindow("Negativo", cv2.WINDOW_NORMAL)
        cv2.imshow("Negativo",r)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        if key == ord('s'):
            guardar_imagen_ruta(r)
    
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
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        if key == ord('s'):
            guardar_imagen_ruta(r)

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
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        if key == ord('s'):
            guardar_imagen_ruta(r)

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
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        if key == ord('s'):
            guardar_imagen_ruta(r)

    def hacer_not(self):
        if not validar_1_imagen(self.imagen1):
            return
        r = operacion_not(self.imagen1)
        cv2.namedWindow("NOT", cv2.WINDOW_NORMAL)
        cv2.imshow("NOT",r)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        if key == ord('s'):
            guardar_imagen_ruta(r)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(r)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(r)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(umb_img)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(umb_img)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(umb_img)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(umb_img)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(umb_img)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(umb_img)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(imagen_filtrada_personalizada)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(imagen_filtrada_personalizada)

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
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        if key == ord('s'):
            guardar_imagen_ruta(imagen_a_gris)

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
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        if key == ord('s'):
            guardar_imagen_ruta(imagen_a_gris)

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
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(imagen_segm)
#------------------------------------------------------------
    def aplicar_contraste(self):
        if self.check_gris.isChecked():
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            factor_contraste = simpledialog.askfloat("Contraste", "Ingresa el valor del factor de contraste entre -100 y 100:")
            imagen_con_contraste = ope_contraste_bw(img1, factor_contraste)
            plt.figure(figsize=(10,5))
            plt.subplot(1, 2, 1)
            plt.title('Original a Grises')
            plt.imshow(img1, cmap='gray')
            plt.axis('off')
            plt.subplot(1, 2, 2)
            plt.title('Contraste aplicado')
            plt.imshow(imagen_con_contraste, cmap='gray') 
            plt.axis('off')
            plt.show()

        else:
            img1 = self.imagen1
            factor_contraste = simpledialog.askfloat("Contraste", "Ingresa el valor del factor de contraste entre -100 y 100:")
            imagen_con_contraste = contraste_operacion(img1, factor_contraste)
            plt.figure(figsize=(10,5))
            plt.subplot(1, 2, 1)
            plt.title('Original')
            plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  
            plt.axis('off')
            plt.subplot(1, 2, 2)
            plt.title('Contraste aplicado')
            plt.imshow(cv2.cvtColor(imagen_con_contraste, cv2.COLOR_BGR2RGB)) 
            plt.axis('off')
            plt.show()
            
    def aplicar_inclinacion(self):
        if self.check_gris.isChecked():
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            angulo = obtener_angulo()
            inclinada_horizontal = inclinar_horizontal(img1, angulo)
            
            cv2.imshow("Inclinada Horizontalmente", inclinada_horizontal)
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(inclinada_horizontal)
           
        else:
            img1 = self.imagen1
            angulo = obtener_angulo()
            inclinada_horizontal = inclinar_horizontal(img1, angulo)
            
            cv2.imshow("Inclinada Horizontalmente", inclinada_horizontal)
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(inclinada_horizontal)
            
    def aplicar_inclinacion_vertical(self):
        if self.check_gris.isChecked():
            img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            angulo = obtener_angulo()

            inclinada_vertical = inclinar_vertical(img1, angulo)
            cv2.imshow("Inclinada Verticalmente", inclinada_vertical)
            
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(inclinada_vertical) 
               
        else:
            img1 = self.imagen1
            angulo = obtener_angulo()

            inclinada_vertical = inclinar_vertical(img1, angulo)
            cv2.imshow("Inclinada Verticalmente", inclinada_vertical)
            
            key = cv2.waitKey(0)  
            cv2.destroyAllWindows()
            if key == ord('s'):
                guardar_imagen_ruta(inclinada_vertical) 
                

    def aplicar_rotacion(self):
        if self.check_gris.isChecked():
            rotacion_instancia = Rotacion_imagenes()
            rotacion_instancia.original_image = cv2.cvtColor(self.imagen1,cv2.COLOR_BGR2GRAY)

            root = tk.Tk()
            root.title("Rotación de Imagen")

            rotacion_instancia.angulo_scale = Scale(root, from_=0, to=360, orient="horizontal", label="Ángulo de Rotación", length=300)
            rotacion_instancia.angulo_scale.pack()

            rotacion_instancia.angulo_scale.bind("<ButtonRelease-1>", rotacion_instancia.actualizar_rotacion)

            rotacion_instancia.rotacion_resultado = tk.Label(root)
            rotacion_instancia.rotacion_resultado.pack()
            guardar_button = tk.Button(root, text="Guardar Imagen", command=rotacion_instancia.guardar_imagen)
            guardar_button.pack()

            original_photo = ImageTk.PhotoImage(Image.fromarray(rotacion_instancia.original_image))
            original_label = tk.Label(root, image=original_photo)
            original_label.pack()
            root.mainloop()

        else:
            rotacion_instancia = Rotacion_imagenes()
            rotacion_instancia.original_image = cv2.cvtColor(self.imagen1, cv2.COLOR_BGR2RGB)
            
            root = tk.Tk()
            root.title("Rotación de Imagen")

            rotacion_instancia.angulo_scale = Scale(root, from_=0, to=360, orient="horizontal", label="Ángulo de Rotación", length=300)
            rotacion_instancia.angulo_scale.pack()
            rotacion_instancia.angulo_scale.bind("<ButtonRelease-1>", rotacion_instancia.actualizar_rotacion)

            rotacion_instancia.rotacion_resultado = tk.Label(root)
            rotacion_instancia.rotacion_resultado.pack()
            guardar_button = tk.Button(root, text="Guardar Imagen", command=rotacion_instancia.guardar_imagen)
            guardar_button.pack()

            original_photo = ImageTk.PhotoImage(Image.fromarray(rotacion_instancia.original_image))
            original_label = tk.Label(root, image=original_photo)
            original_label.pack()

            root.mainloop()

    def aplicar_espejo (self):
        if self.check_gris.isChecked():
            espejo_transformar = Espejo_transformar()
            original_image = self.imagen1
            original_grayscale = espejo_transformar.convertir_a_grises(original_image)

            horizontal_image = espejo_transformar.espejo_horizontal(original_grayscale)
            vertical_image = espejo_transformar.espejo_vertical(original_grayscale)
            diagonal_image = espejo_transformar.espejo_diagonal(original_grayscale)

            espejo_transformar.mostrar_imagenes(original_grayscale, horizontal_image, vertical_image, diagonal_image)
            espejo_transformar.save_images(original_grayscale, horizontal_image, vertical_image, diagonal_image)

        else:
            image_manipulator = ImageManipulator()
            original_image =  cv2.cvtColor(self.imagen1, cv2.COLOR_BGR2RGB)
            
            imagen_espejo_horizontal = image_manipulator.espejo_horizontal(original_image)
            imagen_espejo_vertical = image_manipulator.espejo_vertical(original_image)
            imagen_espejo_diagonal = image_manipulator.espejo_diagonal(original_image)

            image_manipulator.mostrar_imagenes(original_image, imagen_espejo_horizontal, imagen_espejo_vertical, imagen_espejo_diagonal)
            image_manipulator.save_images(original_image, imagen_espejo_horizontal, imagen_espejo_vertical, imagen_espejo_diagonal)
            
#-----------------------------BORDES------------------------------------------------------------------------------------------
    def aplicar_canny(self):
        imagen = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)

        imagen_suavizada = cv2.blur(imagen, (3, 3))  

        imagen_suavizada = suavizar_imagen(imagen)

        magnitud_gradiente, direccion_gradiente = calcular_gradientes(imagen_suavizada)

        bordes_suprimidos = suprimir_no_maximos(magnitud_gradiente, direccion_gradiente)

        bordes_suprimidos = np.uint8(bordes_suprimidos)

        umbral_bajo = 50
        umbral_alto = 255
        bordes_umbralizados = umbralizar(bordes_suprimidos, umbral_bajo, umbral_alto)

        kernel = np.ones((2,2), np.uint8)
        bordes_umbralizados_dilatados = cv2.dilate(bordes_umbralizados, kernel, iterations=1)

        cv2.imwrite('bordes_detectados_canny.png', bordes_umbralizados_dilatados)

        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        axes[0].imshow(imagen, cmap='gray')
        axes[0].set_title('Imagen Original a Blanco y Negro')
        axes[0].axis('off')

        axes[1].imshow(bordes_umbralizados_dilatados, cmap='gray')
        axes[1].set_title('Bordes Detectados')
        axes[1].axis('off')

        plt.show()

    def aplicar_sobel(self):
        imagen_original = self.imagen1
        bordes_sobel = detectar_bordes_sobel(imagen_original)
        imagen_en_gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)
        plot_images(imagen_en_gris, bordes_sobel, "Imagen en Gris", "Bordes detectados con Sobel")
        

    def aplicar_prewitt(self):
        imagen = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
    
        kernel_prewitt_x = np.array([[-1, 0, 1],
                                    [-1, 0, 1],
                                    [-1, 0, 1]])

        kernel_prewitt_y = np.array([[-1, -1, -1],
                                    [0, 0, 0],
                                    [1, 1, 1]])

        edges_x = convolucion(imagen.astype(np.float32), kernel_prewitt_x)
        edges_y = convolucion(imagen.astype(np.float32), kernel_prewitt_y)
        edges = np.sqrt(np.square(edges_x) + np.square(edges_y))

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.imshow(imagen, cmap='gray')
        plt.title('Imagen Original')
        plt.subplot(1, 2, 2)
        plt.imshow(edges, cmap='gray')
        plt.title('Bordes detectados (Prewitt)')
        plt.show()

    def aplicar_gradiente(self):

        imagen_gris =cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)

        gradiente_x, gradiente_y, bordes_detectados = detectar_bordes(imagen_gris)

        cv2.imshow('Gradiente X', gradiente_x)
        cv2.imshow('Gradiente Y', gradiente_y)
        cv2.imshow('Bordes Detectados', bordes_detectados)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        if key == ord('s'):
            guardar_imagen_ruta(bordes_detectados)
    
    def aplicar_top_hat(self):
        tam_kernel = 3
        if not validar_1_imagen(self.imagen1):
            return
        else:
            img1 = self.imagen1

        top_hat_image = top_hat(img1, tam_kernel)

        cv2.namedWindow('Top Hat',cv2.WINDOW_NORMAL)
        cv2.imshow('Top Hat', top_hat_image)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(top_hat_image)

    def aplicar_black_hat(self):
        tam_kernel = 3
        if not validar_1_imagen(self.imagen1):
            return
        else:
            img1 = self.imagen1

        top_hat_image = black_hat(img1, tam_kernel)

        cv2.namedWindow('Black Hat',cv2.WINDOW_NORMAL)
        cv2.imshow('Black Hat', top_hat_image)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(top_hat_image)

    def aplicar_esqueleto(self):
        if not validar_1_imagen(self.imagen1):
            return
        else:
            if (len(self.imagen1.shape)==3):
                # Si la imagen tiene 3 canales, es una imagen a color y se convierte a grises
                img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_RGB2GRAY)
            else:
                # en escala de grises
                img1 = self.imagen1


        # Binariza la imagen
        _, binaria = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

        # Esqueletoniza la imagen binaria
        esqueleto = esqueletonizar(binaria)


        cv2.namedWindow('Esqueleto',cv2.WINDOW_NORMAL)
        cv2.imshow('Esqueleto', esqueleto)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(esqueleto)

    def aplicar_relleno(self):
        if not validar_1_imagen(self.imagen1):
            return
        else:
            img1 = self.imagen1

        rellenada = rellenar_formas(img1)

        cv2.namedWindow('Rellenada',cv2.WINDOW_NORMAL)
        cv2.imshow('Rellenada', rellenada)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(rellenada)

    def convertir_rgb(self):
        if not validar_1_imagen(self.imagen1):
            return
        else:
            if len(self.imagen1.shape) == 2:
                RGB = cv2.cvtColor(self.imagen1, cv2.COLOR_GRAY2BGR)
            else:
                RGB = self.imagen1

        cv2.namedWindow('RGB',cv2.WINDOW_NORMAL)
        cv2.imshow('RGB', RGB)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(RGB)

    def convertir_bgr(self):
        if not validar_1_imagen(self.imagen1):
            return
        else:
            if len(self.imagen1.shape) == 2:
                img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_GRAY2BGR)
            else:
                img1 = self.imagen1

        BGR = rgb2bgr(img1)
        cv2.namedWindow('BGR',cv2.WINDOW_NORMAL)
        cv2.imshow('BGR', BGR)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(BGR)

    def convertir_cmyk(self):
        if not validar_1_imagen(self.imagen1):
            return
        else:
            if len(self.imagen1.shape) == 2:
                img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_GRAY2BGR)
            else:
                img1 = self.imagen1

        cmyk = rgb2cmyk(img1)
        cv2.namedWindow('cmyk',cv2.WINDOW_NORMAL)
        cv2.imshow('cmyk', cmyk)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(cmyk)

    def convertir_hsv(self):
        if not validar_1_imagen(self.imagen1):
            return
        else:
            if len(self.imagen1.shape) == 2:
                img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_GRAY2BGR)
            else:
                img1 = self.imagen1

        hsv = rgb2hsv(img1)
        cv2.namedWindow('hsv',cv2.WINDOW_NORMAL)
        cv2.imshow('hsv', hsv)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(hsv)

    def aplicar_transformada(self):
        if not validar_1_imagen(self.imagen1):
            return
        else:
            if len(self.imagen1.shape) == 2:
                img1 = cv2.cvtColor(self.imagen1, cv2.COLOR_GRAY2BGR)
            else:
                img1 = self.imagen1

        img_con_lineas = imagenHough(img1)
        cv2.namedWindow("imagen con lineas", cv2.WINDOW_NORMAL)
        cv2.imshow("imagen con lineas", img_con_lineas)
        key = cv2.waitKey(0)  
        cv2.destroyAllWindows()
        
        if key == ord('s'):
            guardar_imagen_ruta(img_con_lineas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = miApp()
    ventana.show()
    sys.exit(app.exec())
