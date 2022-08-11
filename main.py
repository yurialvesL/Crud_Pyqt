from Classes.crud import *
from PyQt5.QtWidgets import  QApplication
import sys

qt = QApplication(sys.argv)
tela = Crud()
tela.show()
sys.exit(qt.exec())
