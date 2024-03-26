from PyQt6.QtWidgets import  QPushButton, QDialog, QLabel, QVBoxLayout, QComboBox

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
