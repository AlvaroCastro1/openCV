from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class DialogoDosNumeros(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ingresar dos números")
        layout = QVBoxLayout()

        self.label1 = QLabel("Número 1:")
        self.textbox1 = QLineEdit()
        layout.addWidget(self.label1)
        layout.addWidget(self.textbox1)

        self.label2 = QLabel("Número 2:")
        self.textbox2 = QLineEdit()
        layout.addWidget(self.label2)
        layout.addWidget(self.textbox2)

        self.boton_aceptar = QPushButton("Aceptar")
        self.boton_aceptar.clicked.connect(self.aceptar)
        layout.addWidget(self.boton_aceptar)

        self.setLayout(layout)

    def aceptar(self):
        numero1 = self.textbox1.text()
        numero2 = self.textbox2.text()
        try:
            numero1 = float(numero1)
            numero2 = float(numero2)
            self.accept()  # Cerrar el diálogo con código de aceptación
        except ValueError:
            pass  # No hacer nada si no se pueden convertir a números flotantes

class DialogoUnNumero(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ingresar un número entre 0 y 255")
        layout = QVBoxLayout()

        self.label = QLabel("Número entre 0 y 255:")
        self.textbox = QLineEdit()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)

        self.boton_aceptar = QPushButton("Aceptar")
        self.boton_aceptar.clicked.connect(self.aceptar)
        layout.addWidget(self.boton_aceptar)

        self.setLayout(layout)

    def aceptar(self):
        numero = self.textbox.text()
        if numero.isdigit():
            numero_entero = int(numero)
            if 0 <= numero_entero <= 255:
                print("Número ingresado:", numero_entero)
                self.accept()  # Cerrar el diálogo con código de aceptación
                return
        print("Error: Por favor, ingrese un número entero entre 0 y 255.")

class DialogoDosUmbrales(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ingresar dos umbrales entre 0 y 255")
        layout = QVBoxLayout()

        self.label1 = QLabel("Umbral 1:")
        self.textbox1 = QLineEdit()
        layout.addWidget(self.label1)
        layout.addWidget(self.textbox1)

        self.label2 = QLabel("Umbral 2:")
        self.textbox2 = QLineEdit()
        layout.addWidget(self.label2)
        layout.addWidget(self.textbox2)

        self.boton_aceptar = QPushButton("Aceptar")
        self.boton_aceptar.clicked.connect(self.aceptar)
        layout.addWidget(self.boton_aceptar)

        self.setLayout(layout)

    def aceptar(self):
        umbral1 = self.textbox1.text()
        umbral2 = self.textbox2.text()
        try:
            umbral1 = int(umbral1)
            umbral2 = int(umbral2)
            if 0 <= umbral1 <= 255 and 0 <= umbral2 <= 255:
                self.accept()  # Cerrar el diálogo con código de aceptación
            else:
                print("Error: Los umbrales deben estar entre 0 y 255.")
        except ValueError:
            print("Error: Por favor, ingrese números enteros.")
