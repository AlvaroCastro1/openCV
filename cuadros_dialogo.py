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
