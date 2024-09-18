from PyQt5 import QtWidgets, QtGui  # Importa QtWidgets y QtGui
from PyQt5.QtCore import Qt  # Importa Qt desde PyQt5.QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QLineEdit, QPushButton, QWidget, QHBoxLayout, QMessageBox  # Importa varios widgets desde PyQt5.QtWidgets
import sys  # Importa el módulo sys


# Función para buscar la puja mayor
def buscar_mayor_puja(pujas):
    puja_previa = 0
    for i in pujas:
        puja_comprobada = int(pujas[i])
        if puja_comprobada > puja_previa:
            puja_previa = puja_comprobada
    return puja_previa


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Sistema de Subastas'
        self.left = 100
        self.top = 100
        self.width = 1300
        self.height = 400
        #_self.setStyleSheet("background-color: gray;")


        # Diccionario de pujas
        self.pujas = {'precio_inicial': '100'}

        # Inicializa la interfaz
        self.initUI()

    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Layout principal horizontal
        main_layout = QHBoxLayout()

        # Layout para la imagen
        image_layout = QVBoxLayout()
        self.image_label = QLabel(self)
        pixmap = QtGui.QPixmap("art.png")
        pixmap = pixmap.scaled(800, 800, Qt.KeepAspectRatio)  # Ajusta el tamaño de la imagen aquí
        self.image_label.setPixmap(pixmap)
        image_layout.addWidget(self.image_label)

        # Añadir el layout de imagen al layout principal
        main_layout.addLayout(image_layout)

        # Layout para los controles (botones y entradas)
        control_layout = QVBoxLayout()

        # Input para el nombre del pujador
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Introduzca nombre de pujador')
        self.nombre_input.setStyleSheet("font-size: 18px;")  # Aumenta el tamaño de la fuente
        control_layout.addWidget(self.nombre_input)

        # Input para el valor de la puja
        self.valor_input = QLineEdit(self)
        self.valor_input.setPlaceholderText('Introduzca la cantidad a pujar')
        self.valor_input.setStyleSheet("font-size: 18px;")  # Aumenta el tamaño de la fuente
        control_layout.addWidget(self.valor_input)


        # Botón para añadir puja
        add_button = QPushButton('Añadir Puja', self)
        add_button.setStyleSheet("font-size: 25px;")  # Aumenta el tamaño de la fuente
        add_button.clicked.connect(self.anadir_puja)
        control_layout.addWidget(add_button)

        # Botón para encontrar la mayor puja
        check_button = QPushButton('Buscar Mayor Puja', self)
        check_button.setStyleSheet("font-size: 25px;")  # Aumenta el tamaño de la fuente
        check_button.clicked.connect(self.mostrar_mayor_puja)
        control_layout.addWidget(check_button)  

        # Label para mostrar pujas
        self.pujas_label = QLabel('Las pujas van así:', self)
        self.pujas_label.setStyleSheet("font-size: 18px;")  # Aumenta el tamaño de la fuente para "Las pujas van así"
        control_layout.addWidget(self.pujas_label)

        # Añadir el layout de controles al layout principal
        main_layout.addLayout(control_layout)

        # Layout de botones de control
        self.setLayout(main_layout)

    def anadir_puja(self):
        nombre_pujador = self.nombre_input.text()
        valor_nueva_puja = self.valor_input.text()

        if nombre_pujador and valor_nueva_puja.isdigit():
            self.pujas[nombre_pujador] = valor_nueva_puja
            self.actualizar_pujas()
            self.nombre_input.clear()
            self.valor_input.clear()
        else:
            QMessageBox.warning(self, 'Error', 'Introduzca un nombre válido y un valor de puja numérico.')

    def mostrar_mayor_puja(self):
        mayor_puja = buscar_mayor_puja(self.pujas)
        QMessageBox.information(self, 'Mayor Puja', f'La mayor puja encontrada es: {mayor_puja}')

    def actualizar_pujas(self):
        pujas_texto = '\n'.join([f'    {clave}: {valor}' for clave, valor in self.pujas.items()])
        self.pujas_label.setText(f'Las pujas van así:\n{pujas_texto}')






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
