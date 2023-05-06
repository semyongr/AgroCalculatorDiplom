import sys
from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QMainWindow, QMessageBox, QFileDialog, QWidget, QLabel
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap, QDoubleValidator, QIntValidator
from PIL import Image
# from connection import *

import pymysql

def info(self, title, text):
    QMessageBox.information(
        self,
        title,
        text)

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("LoginWindow.ui", self)

        self.login_btn.clicked.connect(self.conn)

    def conn(self):
        connected = False
        try:
            connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="agrohelperdb")
            connected = True
        except pymysql.MySQLError as ex:
            error = ex
            # print(error)
        if connected == True:
            cursor = connection.cursor()
            if ((self.login_tb.text() == "") | (self.pass_tb.text() == "")):
                info(self, 'Ошибка!', 'Заполните все поля!')
            else:
                login = self.login_tb.text()
                password = self.pass_tb.text()
                self.sql_login = "SELECT * FROM `users` WHERE login = %s"
                cursor.execute(self.sql_login, (login))
                value = cursor.fetchall()
                if value == ():
                    info(self, 'Ошибка!', 'Не удается войти: пользователь с данным логином не зарегистрирован')
                elif value[0][1] != password:
                    info(self, 'Ошибка!', 'Не удается войти: неверный пароль')
                else:
                    self.start_window = StartWindowClass()
                    self.start_window.show()
                    Login.close(self)
        else:
            info(self, 'Ошибка!', 'Не удается подключиться к серверу. Проверьте подключение к интернету')

class StartWindowClass(QMainWindow):
    def __init__(self):
        super(StartWindowClass, self).__init__()
        loadUi("StartWindow.ui", self)

        self.main_window = MainWindowClass()
        self.stock_window = StockWindowClass()

        self.main_btn.clicked.connect(self.open_main)
        self.stock_btn.clicked.connect(self.open_stock)

    def open_main(self):
        self.main_window.show()

    def open_stock(self):
        connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="agrohelperdb")
        cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor

        self.cursor.execute("SELECT count FROM stock WHERE type = 'Азотные'")
        self.sql = self.cursor.fetchone()
        self.stock_window.azot_tb.setText(str(self.sql[0]))
        self.cursor.execute("SELECT count FROM stock WHERE type = 'Калийные'")
        self.sql = self.cursor.fetchone()
        self.stock_window.potassium_tb.setText(str(self.sql[0]))
        self.cursor.execute("SELECT count FROM stock WHERE type = 'Фосфорные'")
        self.sql = self.cursor.fetchone()
        self.stock_window.phosphor_tb.setText(str(self.sql[0]))
        self.stock_window.show()

class MainWindowClass(QMainWindow):
    def __init__(self):
        super(MainWindowClass, self).__init__()
        loadUi("MainWindow.ui", self)

        # валидация форм ввода
        self.square_tb.setValidator(QDoubleValidator())
        self.quantity_tb.setValidator(QIntValidator())
        self.number_tb.setValidator(QIntValidator())
        self.mass_tb.setValidator(QDoubleValidator())


        # подключение к БД
        connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="agrohelperdb")
        cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor

        # подгрузка с/х культур в checkbox
        def cultures(self):
            self.cursor.execute("SELECT culture FROM fertilizers ")
            self.sql = cursor.fetchall()
            self.cul_names = []
            for i in self.sql:
                self.cul_names.append(i[0])
            self.culture_cb.addItems(self.cul_names)
        cultures(self)

        # подгрузка фосфорных коэффициентов в checkbox
        def phosphor(self):
            self.cursor.execute("SELECT DISTINCT level FROM phoshor_coeff ORDER BY level")
            self.sql = cursor.fetchall()
            self.phos_levels = []
            for i in self.sql:
                self.phos_levels.append(i[0])
            self.phosphor_cb.addItems(self.phos_levels)
        phosphor(self)

        # подгрузка калийных коэффициентов в checkbox
        def potassium(self):
            self.cursor.execute("SELECT DISTINCT level FROM potassium_coeff ORDER BY level")
            self.sql = cursor.fetchall()
            self.pot_levels = []
            for i in self.sql:
                self.pot_levels.append(i[0])
            self.potassium_cb.addItems(self.pot_levels)
        potassium(self)


        # подключение форм
        self.result_window = ResultWindowClass()
        self.image_window = ImageWindowClass()

        # подключение функций кнопкам
        self.load_img_btn.clicked.connect(self.open_img_window)
        self.calc_btn.clicked.connect(self.calc)
        self.clear_btn.clicked.connect(self.clear)

    def clear(self):
        self.square_tb.setText('')
        self.quantity_tb.setText('')
        self.number_tb.setText('')
        self.mass_tb.setText('')

    def open_img_window(self):
        self.image_window.show()

    # калькулятор удобрений
    def calc(self):
        if ((self.square_tb.text() == "") | (self.quantity_tb.text() == "") | (self.number_tb.text() == "") | (self.mass_tb.text() == "")):
            info(self, 'Ошибка!', 'Заполните все поля!')
        elif (self.square_tb.text() == ',') | (self.mass_tb.text() == ','):
            info(self, 'Ошибка!', 'Введены некорректные данные!')
        else:
            square = float((self.square_tb.text()).replace(",","."))
            quantity = int(self.quantity_tb.text())
            number = int(self.number_tb.text())
            mass = float(self.mass_tb.text().replace(",","."))
            posphor_level = str(self.phosphor_cb.currentText())
            potassium_level = str(self.potassium_cb.currentText())
            culture = str(self.culture_cb.currentText())
            print(mass)

            # азотистые удобрения
            self.sql_azote = "SELECT `azote` FROM `fertilizers` WHERE culture = %s"
            self.cursor.execute(self.sql_azote, (culture))
            self.azote = self.cursor.fetchone()
            self.azote = float(self.azote[0])

            # фосфорные удобрения
            self.sql_phosphor = "SELECT `phosphor` FROM `fertilizers` WHERE culture = %s"
            self.cursor.execute(self.sql_phosphor, (culture))
            self.phosphor = self.cursor.fetchone()
            self.phosphor = float(self.phosphor[0])

            # калийные удобрения
            self.sql_potassium = "SELECT `potassium` FROM `fertilizers` WHERE culture = %s"
            self.cursor.execute(self.sql_potassium, (culture))
            self.potassium = self.cursor.fetchone()
            self.potassium = float(self.potassium[0])

            # коэффициент для фосфорных удобрений
            self.sql_phos_coeff = "SELECT `coeff` FROM `phoshor_coeff` WHERE culture = %s AND level = %s"
            self.cursor.execute(self.sql_phos_coeff, (culture, posphor_level))
            self.phos_coeff = self.cursor.fetchone()
            self.phos_coeff = float(self.phos_coeff[0])

            # коэффициент для калийных удобрений
            self.sql_potas_coeff = "SELECT `coeff` FROM `potassium_coeff` WHERE culture = %s AND level = %s"
            self.cursor.execute(self.sql_potas_coeff, (culture, potassium_level))
            self.potas_coeff = self.cursor.fetchone()
            self.potas_coeff = float(self.potas_coeff[0])

            harvest = square * ((quantity * number * mass) / 10000)
            result_azote = round(harvest * self.azote)
            result_phosphor = round(harvest * self.phosphor * self.phos_coeff)
            result_potassium = round(harvest * self.potassium * self.potas_coeff)

            # result = f'Доза азотных удобрений: {result_azote}' + '\n' + \
            #          f'Доза фосфорных удобрений: {result_phosphor}' + '\n' + \
            #          f'Доза калийных удобрений: {result_potassium}'

            self.result_window.azot_tb.setText(str(result_azote))
            self.result_window.phosphor_tb.setText(str(result_phosphor))
            self.result_window.potassium_tb.setText(str(result_potassium))
            self.result_window.show()

class ImageWindowClass(QMainWindow):
    def __init__(self):
        super(ImageWindowClass, self).__init__()
        loadUi("ImageWindow.ui", self)

        self.field_square_tb.setValidator(QDoubleValidator())

        self.loadpic_window = LoadPicClass()
        self.select_img_btn.clicked.connect(self.load_img)


    # загрузка исходного изображения
    def load_img(self):
        field_square = (self.field_square_tb.text()).replace(",", ".")
        if ((self.field_square_tb.text() == "")):
            info(self, 'Ошибка!', 'Внесите данные о площади поля!')
        else:
            fname = QFileDialog.getOpenFileName(self, "OpenFile", "C:\\",
                                                    "PNG Files (*.png);;JPG Files (*.jpg)")
            if fname[0] == "":
                info(self, 'Ошибка!', 'Изображение не выбрано!')
            else:
                pixmap = QPixmap(fname[0])
                self.loadpic_window.loadpic_lbl.setPixmap(pixmap)
                self.loadpic_window.show()

                im = Image.open(fname[0])
                width, height = im.size
                # print(width)
                red_pixels = 0
                for pixel in im.getdata():
                    if pixel == (204, 0, 1):
                        red_pixels += 1
                # self.square_tb.setText(str(black))


                print(red_pixels)

                zone_square = (float(field_square) * red_pixels) / (width * height)
                print(zone_square)

class ResultWindowClass(QMainWindow):
    def __init__(self):
        super(ResultWindowClass, self).__init__()
        loadUi("ResultWindow.ui", self)

        self.azot_tb.setValidator(QIntValidator())
        self.phosphor_tb.setValidator(QIntValidator())
        self.potassium_tb.setValidator(QIntValidator())

        connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="agrohelperdb")
        cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor

        self.use_btn_azote.clicked.connect(self.use_azote)
        self.use_btn_phosphor.clicked.connect(self.use_phosphor)
        self.use_btn_potassium.clicked.connect(self.use_potassium)

    def use_azote(self):
        azote = int(self.azot_tb.text())
        self.cursor.execute("SELECT count FROM stock WHERE type = 'Азотные'")
        self.sql = self.cursor.fetchone()
        result = int(self.sql[0]) - azote
        if result >= 0:
            info(self, 'Успешно', 'Изменения сохранены')
            self.sql_azote = "UPDATE stock SET count = %s WHERE type = 'Азотные'"
            self.cursor.execute(self.sql_azote, (result))
            self.connection.commit()
        else:
            info(self, 'Ошибка!', 'В хранилище недосточно удобрений для выполнения данной операции')

    def use_phosphor(self):
        phosphor = int(self.phosphor_tb.text())
        self.cursor.execute("SELECT count FROM stock WHERE type = 'Фосфорные'")
        self.sql = self.cursor.fetchone()
        result = int(self.sql[0]) - phosphor
        if result >= 0:
            info(self, 'Успешно', 'Изменения сохранены')
            self.sql_phosphor = "UPDATE stock SET count = %s WHERE type = 'Фосфорные'"
            self.cursor.execute(self.sql_phosphor, (result))
            self.connection.commit()
        else:
            info(self, 'Ошибка!', 'В хранилище недосточно удобрений для выполнения данной операции')

    def use_potassium(self):
        potassium = int(self.potassium_tb.text())
        self.cursor.execute("SELECT count FROM stock WHERE type = 'Калийные'")
        self.sql = self.cursor.fetchone()
        result = int(self.sql[0]) - potassium
        if result >= 0:
            info(self, 'Успешно', 'Изменения сохранены')
            self.sql_potassium = "UPDATE stock SET count = %s WHERE type = 'Калийные'"
            self.cursor.execute(self.sql_potassium, (result))
            self.connection.commit()
        else:
            info(self, 'Ошибка!', 'В хранилище недосточно удобрений для выполнения данной операции')

class StockWindowClass(QMainWindow):
    def __init__(self):
        super(StockWindowClass, self).__init__()
        loadUi("StockWindow.ui", self)

        self.azot_tb.setValidator(QIntValidator())
        self.phosphor_tb.setValidator(QIntValidator())
        self.potassium_tb.setValidator(QIntValidator())

        connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="agrohelperdb")
        cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor
        self.save_btn.clicked.connect(self.save)

    def save(self):
        if ((self.azot_tb.text() == "") | (self.potassium_tb.text() == "") | (self.phosphor_tb.text() == "")):
            info(self, 'Ошибка!', 'Заполните все поля!')
        else:
            azote = int(self.azot_tb.text())
            potassium = int(self.potassium_tb.text())
            phosphor = int(self.phosphor_tb.text())

            self.sql_azote = "UPDATE stock SET count = CASE " \
                             "WHEN type = 'Азотные' THEN %s " \
                             "WHEN type = 'Калийные' THEN %s " \
                             "WHEN type = 'Фосфорные' THEN %s " \
                             "END"
            self.cursor.execute(self.sql_azote, (azote, potassium, phosphor))
            self.connection.commit()
            info(self, 'Успешно ', 'Изменения сохранены')

class LoadPicClass(QMainWindow):
    def __init__(self):
        super(LoadPicClass, self).__init__()
        loadUi("LoadPic.ui", self)

app = QApplication(sys.argv)
window = Login()
window.show()
app.exec()


