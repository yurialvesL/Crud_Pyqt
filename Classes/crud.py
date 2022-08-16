from PyQt5.QtWidgets import QMainWindow,QMessageBox,QRadioButton,QTableWidget
from Template.tela import *
from Template.registration import *
from Classes.Person import *
from Classes.Connector import *


class Crud(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.list = personcollection()
        super().setupUi(self)
        self.insertperson()

    def insertperson(self):
        self.qtable_contacts.setRowCount(len(self.list))
        row=0
        for i in self.list:
            self.qtable_contacts.setItem(row,0,QtWidgets.QTableWidgetItem(str(i.id)))
            self.qtable_contacts.setItem(row, 1, QtWidgets.QTableWidgetItem(i.name))
            self.qtable_contacts.setItem(row, 2, QtWidgets.QTableWidgetItem(i.sex))
            self.qtable_contacts.setItem(row, 3, QtWidgets.QTableWidgetItem(i.job))
            self.qtable_contacts.setItem(row, 4, QtWidgets.QTableWidgetItem(i.email))
            self.qtable_contacts.setItem(row, 5, QtWidgets.QTableWidgetItem(i.cpf))
            self.qtable_contacts.setItem(row, 6, QtWidgets.QTableWidgetItem(i.typephone))
            self.qtable_contacts.setItem(row, 7, QtWidgets.QTableWidgetItem(i.phone_number))
            print(i.id,i.name,i.sex,i.job,i.email,i.cpf,i.typephone,i.phone_number)
            row+=1


class Registration(QMainWindow,Ui_Registration):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)




