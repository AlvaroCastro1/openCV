from PyQt6.QtWidgets import  QPushButton, QDialog, QLabel, QLineEdit, QVBoxLayout, QMessageBox

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

