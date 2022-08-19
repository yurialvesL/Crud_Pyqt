from PyQt5.QtWidgets import QMainWindow, QMessageBox, QRadioButton, QTableWidget
from PyQt5.QtGui import QIcon
from Template.tela import *
from Template.registration import *
from Classes.Person import *
from Classes.Connector import *


class Crud(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.table_person()
        self.list = []
        self.btn_insert.clicked.connect(self.insertperson)
        self.btn_update.clicked.connect(self.updata)
        self.btn_delete.clicked.connect(self.delete)
        self.rbd_darkmode.clicked.connect(self.dark_mode)

    def table_person(self):
        self.list = personcollection()
        self.qtable_contacts.setRowCount(len(self.list))
        row = 0
        for i in self.list:
            self.qtable_contacts.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i.id)))
            self.qtable_contacts.setItem(row, 1, QtWidgets.QTableWidgetItem(i.name))
            self.qtable_contacts.setItem(row, 2, QtWidgets.QTableWidgetItem(i.sex))
            self.qtable_contacts.setItem(row, 3, QtWidgets.QTableWidgetItem(i.job))
            self.qtable_contacts.setItem(row, 4, QtWidgets.QTableWidgetItem(i.email))
            self.qtable_contacts.setItem(row, 5, QtWidgets.QTableWidgetItem(i.cpf))
            self.qtable_contacts.setItem(row, 6, QtWidgets.QTableWidgetItem(i.typephone))
            self.qtable_contacts.setItem(row, 7, QtWidgets.QTableWidgetItem(i.phone_number))
            row += 1

    def insertperson(self):
        if self.rbd_darkmode.isChecked():
            self.regis = Registration()
            self.hide()
            self.regis.show()
            self.regis.rbd_darkmode.setChecked(True)
            self.regis.dark_mode()
        else:
            self.regis = Registration()
            self.hide()
            self.regis.show()

    def updata(self):
        rows = sorted(set(index.row() for index in
                          self.qtable_contacts.selectedIndexes()))
        id = self.qtable_contacts.item(rows[0], 0).text()
        name = self.qtable_contacts.item(rows[0], 1).text()
        sex = self.qtable_contacts.item(rows[0], 2).text()
        job = self.qtable_contacts.item(rows[0], 3).text()
        email = self.qtable_contacts.item(rows[0], 4).text()
        cpf = self.qtable_contacts.item(rows[0], 5).text()
        type_phone = self.qtable_contacts.item(rows[0], 6).text()
        phone_number = self.qtable_contacts.item(rows[0], 7).text()
        persona = Person(id, name, sex, job, email, cpf, type_phone, phone_number)
        print(persona.name)
        self.up = Update()
        self.hide()
        self.up.show()
        self.up.filldata(persona)

    def delete(self):
        rows = sorted(set(index.row() for index in
                          self.qtable_contacts.selectedIndexes()))
        id = self.qtable_contacts.item(rows[0], 0).text()
        if self.btn_delete.clicked:
            message = QMessageBox()
            message.setWindowIcon(QIcon('img/cross.png'))
            message.setWindowTitle('Exclusão de contato')
            message.setIcon(QMessageBox.Critical)
            message.setText(f'Tem certeza que deseja excluir o usuário de ID:{id} ?')
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            returnvalue = message.exec()
            if returnvalue == QMessageBox.Yes:
                delete_person(id)
                message = QMessageBox()
                message.setWindowIcon(QIcon('img/cross.png'))
                message.setWindowTitle('User information')
                message.setIcon(QMessageBox.Information)
                message.setText(f'User deleted with success')
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
                self.table_person()

    def dark_mode(self):
        if self.rbd_darkmode.isChecked():
            self.rbd_darkmode.setText('Dark mode on')

            self.btn_delete.setStyleSheet('QPushButton{'
                                          'background-color:transparent;color:white;border:none;}'
                                          'QPushButton:hover{font-weight:bold;border-bottom: 2px solid white;}')
            self.btn_insert.setStyleSheet('QPushButton{'
                                          'background-color:transparent;color:white;border:none;}'
                                          'QPushButton:hover{font-weight:bold;border-bottom: 2px solid white;}')
            self.btn_update.setStyleSheet('QPushButton{'
                                          'background-color:transparent;color:white;border:none;}'
                                          'QPushButton:hover{font-weight:bold;border-bottom: 2px solid white;}')
            self.btn_search_cpf.setStyleSheet('QPushButton{''background-color:transparent;color:white;border:none;}'
                                              'QPushButton:hover{font-weight:bold;border-bottom: 2px solid white;}')
            self.lbl_title.setStyleSheet('QLabel{color:white;}')
            self.label.setStyleSheet('QLabel{color:white;}')
            self.qtable_contacts.setStyleSheet('QTableWidget{color:white;background-color:#616060;selection'
                                               '-background-color: #353535; border-radius: 10px; '
                                               'margin-top:5px;} '
                                               'QHeaderView{color:white;}QHeaderView:section{'
                                               'background-color:#646464; border-radius:1px; border:1px solid white;}'
                                               'QTableWidget::item{border-radius:10px;} ')
            self.setStyleSheet('background-color:black;')
            self.txt_cpf_search.setStyleSheet('color:white;')
            self.qtable_contacts.verticalHeader().hide()
        elif not self.rbd_darkmode.isChecked():
            self.rbd_darkmode.setText('Dark mode off')
            self.setStyleSheet('background-color:white;')
            self.btn_delete.setStyleSheet('QPushButton{'
                                          'background-color:transparent;color:black;border:none;}'
                                          'QPushButton:hover{font-weight:bold;border-bottom: 2px solid black;}')
            self.btn_insert.setStyleSheet('QPushButton{'
                                          'background-color:transparent;color:black; border:none;}'
                                          'QPushButton:hover{font-weight:bold;border-bottom: 2px solid black;}')
            self.btn_update.setStyleSheet('QPushButton{'
                                          'background-color:transparent;color:black; border:none;}'
                                          'QPushButton:hover{font-weight:bold;border-bottom: 2px solid black;}')
            self.btn_search_cpf.setStyleSheet('QPushButton{''background-color:transparent;color:black;border:none;}'
                                              'QPushButton:hover{font-weight:bold;border-bottom: 2px solid black;}')
            self.lbl_title.setStyleSheet('QLabel{color:black;}')
            self.label.setStyleSheet('QLabel{color:black;}')
            self.qtable_contacts.setStyleSheet('QTableWidget{color:white;background-color:white;selection'
                                               '-background-color: #353535; border-radius: 10px; '
                                               'margin-top:5px;} '
                                               'QHeaderView{color:black;}QHeaderView:section{'
                                               'background-color:white; border-radius:1px; border:1px solid black;}'
                                               'QTableWidget::item{border-radius:10px; color:black;} ')
            self.qtable_contacts.verticalHeader().hide()


class Registration(QMainWindow, Ui_Registration):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.typephones()
        self.btn_register.clicked.connect(self.insert)
        self.rbd_darkmode.clicked.connect(self.dark_mode)
        self.btn_back.clicked.connect(self.back_to_principal)

    def typephones(self):
        list_type = ['CELL', 'COM', 'RES']
        self.comboBox.addItems(list_type)

    def insert(self):
        Person.name = self.txt_name.text()
        Person.job = self.txt_job.text()
        if self.rbd_men.isChecked():
            Person.sex = 'M'
        elif self.rbd_woman.isChecked():
            Person.sex = 'F'
        Person.email = self.txt_email.text()
        Person.cpf = self.txt_cpf.text()
        option = self.comboBox.currentText()
        if option == "CELL":
            Person.typephone = "CELL"
        elif option == "RES":
            Person.typephone = "RES"
        elif option == "COM":
            Person.typephone = "COM"
        Person.phone_number = self.txt_phonenumber.text()
        insert_person(Person)
        message = QMessageBox()
        message.setWindowIcon(QIcon('img/agenda.png'))
        message.setIcon(QMessageBox.Information)
        message.setMinimumSize(600, 1000)
        message.setText('User insert in Database with success!')
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
        if self.rbd_darkmode.isChecked():
            self.principal = Crud()
            self.hide()
            self.principal.show()
            self.principal.rbd_darkmode.setChecked(True)
            self.principal.dark_mode()

    def dark_mode(self):
        if self.rbd_darkmode.isChecked():
            self.setStyleSheet('background-color:black;')
            self.rbd_darkmode.setText('dark mode on')
            self.btn_register.setStyleSheet('QPushButton{border:1px solid white; color:white;}'
                                            'QPushButton:hover{font-weight:bold;color:white;}')
            self.btn_back.setStyleSheet('QPushButton{border:1px solid white; color:white;}'
                                        'QPushButton:hover{font-weight:bold; }')
            self.frame.setStyleSheet('background-color:#646464; border-radius:30px;')
            self.txt_name.setStyleSheet('QLineEdit{border:none; border-bottom:1px solid white;color:white; '
                                        'background-color:transparent;}')
            self.txt_cpf.setStyleSheet('QLineEdit{border-bottom:1px solid white;color:white; '
                                       'background-color:transparent;}')
            self.txt_job.setStyleSheet('QLineEdit{border-bottom:1px solid white;color:white; '
                                       'background-color:transparent;}')
            self.txt_email.setStyleSheet('QLineEdit{border-bottom:1px solid white;color:white; '
                                         'background-color:transparent;}')
            self.txt_phonenumber.setStyleSheet('QLineEdit{border-bottom:1px solid white;color:white; '
                                               'background-color:transparent;}')
            self.lbl_id.hide()
            self.label.setStyleSheet('QLabel{color:white;}')
            self.label_2.setStyleSheet('QLabel{color:white; }')
            self.label_3.setStyleSheet('QLabel{color:white;}')
            self.label_4.setStyleSheet('QLabel{color:white;}')
            self.label_5.setStyleSheet('QLabel{color:white;}')
            self.label_6.setStyleSheet('QLabel{color:white;}')
            self.label_7.setStyleSheet('QLabel{color:white;}')
            self.label_8.setStyleSheet('QLabel{color:white; font-weight:bold;}')
            self.label_9.hide()
            self.rbd_men.setStyleSheet('color:white;')
            self.rbd_woman.setStyleSheet('color:white;')
            self.comboBox.setStyleSheet('border:1px solid white; color:white;')

        elif not self.rbd_darkmode.isChecked():
            self.rbd_darkmode.setText('dark mode off')
            self.btn_register.setStyleSheet('QPushButton{border:1px solid black;, color:black;}'
                                            'QPushButton:hover{font-weight:bold;}')
            self.btn_back.setStyleSheet('QPushButton{border:1px solid black;, color:black;}'
                                        'QPushButton:hover{font-weight:bold;}')
            self.frame.setStyleSheet('background-color:white; border-radius:30px;')
            self.txt_name.setStyleSheet('QLineEdit{border:none;border-bottom:1px solid black; color:black;}')
            self.txt_cpf.setStyleSheet('QLineEdit{border-bottom:1px solid black;color:black}')
            self.txt_job.setStyleSheet('QLineEdit{border-bottom:1px solid black;color:black}')
            self.txt_email.setStyleSheet('QLineEdit{border-bottom:1px solid black;color:black}')
            self.txt_phonenumber.setStyleSheet('QLineEdit{border-bottom:1px solid black;color:black}')
            self.lbl_id.hide()
            self.label_2.setStyleSheet('QLabel{color:black;}')
            self.label_3.setStyleSheet('QLabel{color:black;}')
            self.label_4.setStyleSheet('QLabel{color:black;}')
            self.label_5.setStyleSheet('QLabel{color:black;}')
            self.label_6.setStyleSheet('QLabel{color:black;}')
            self.label_7.setStyleSheet('QLabel{color:black;}')
            self.label_8.setStyleSheet('QLabel{color:black; font-weight:bold;}')
            self.label_9.setStyleSheet('QLabel{color:black;}')
            self.rbd_men.setStyleSheet('color:black;')
            self.rbd_woman.setStyleSheet('color:black;')
            self.comboBox.setStyleSheet('border:1px solid white; color:black;')

    def back_to_principal(self):
        if self.rbd_darkmode.isChecked():
            self.principa = Crud()
            self.hide()
            self.principa.show()
            self.principa.rbd_darkmode.setChecked(True)
            self.principa.dark_mode()
        else:
            self.principa = Crud()
            self.hide()
            self.principa.show()


class Update(QMainWindow, Ui_Registration):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        list_type = ['CELL', 'COM', 'RES']
        self.comboBox.addItems(list_type)
        self.btn_register.clicked.connect(self.update_contact)

    def filldata(self, Person):
        self.txt_name.setText(Person.name)
        self.txt_job.setText(Person.job)
        self.txt_cpf.setText(Person.cpf)
        self.txt_email.setText(Person.email)
        self.txt_phonenumber.setText(Person.phone_number)
        self.lbl_id.setText(Person.id)
        if Person.typephone == "CELL":
            self.comboBox.setCurrentText("CELL")
        elif Person.typephone == "RES":
            self.comboBox.setCurrentText('RES')
        elif Person.typephone == "COM":
            self.comboBox.setCurrentText('COM')

        if Person.sex == "M":
            self.rbd_men.setChecked(True)
        elif Person.sex == "F":
            self.rbd_woman.setChecked(True)

    def update_contact(self):

        Person.id = self.lbl_id.text()
        Person.name = self.txt_name.text()
        Person.job = self.txt_job.text()
        Person.cpf = self.txt_cpf.text()
        Person.email = self.txt_email.text()
        Person.phone_number = self.txt_phonenumber.text()
        option = self.comboBox.currentText()
        if option == "CELL":
            Person.typephone = "CELL"
        elif option == "RES":
            Person.typephone = "RES"
        elif option == "COM":
            Person.typephone = "COM"
        if self.rbd_men.isChecked():
            Person.sex = "M"
        elif self.rbd_woman.isChecked():
            Person.sex = "F"
        print(Person.typephone)
        update_person(Person)
        message = QMessageBox()
        message.setWindowIcon(QIcon('img/agenda.png'))
        message.setIcon(QMessageBox.Information)
        message.setMinimumSize(600, 1000)
        message.setText('Update User Success!')
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
        self.principal = Crud()
        self.hide()
        self.principal.show()
