import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from diseno1 import Ui_MainWindow

class miApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.mostrar_img1.clicked.connect(self.mostrar_imagen)
        
    def mostrar_imagen(self):
        imagen_ruta = "C:/Users/Hp245-User/Desktop/openCV/images/amarilla.png"
        pixmap = QPixmap(imagen_ruta)
        
        # Asignar la imagen al QLabel
        self.ui.mostrar_imagen1.setPixmap(pixmap)
        self.ui.mostrar_imagen1.setScaledContents(True)  # Escalar la imagen al tamaño del QLabel
        
        self.ui.mostrar_imagen2.setPixmap(pixmap)
        self.ui.mostrar_imagen2.setScaledContents(True)  # Escalar la imagen al tamaño del QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = miApp()
    ventana.show()
    sys.exit(app.exec())
