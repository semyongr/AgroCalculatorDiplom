import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap, QDoubleValidator, QIntValidator


def info(self, title, text):
    QMessageBox.information(
        self,
        title,
        text)

# аутентификация
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("LoginWindow.ui", self)

        self.registration_window = RegistrationClass()
        self.registr_btn.clicked.connect(self.open_registration)
        self.login_btn.clicked.connect(self.connect)

    def connect(self):
        connected = False
        try:
            global connection
            connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="diplom")
            connected = True
        except pymysql.MySQLError as ex:
            error = ex
            # print(error)
        if connected == True:
            cursor = connection.cursor()
            if ((self.login_tb.text() == "") | (self.pass_tb.text() == "")):
                info(self, 'Ошибка!', 'Введите логин и пароль')
            else:
                login = self.login_tb.text()
                password = self.pass_tb.text()
                self.sql_login = "SELECT * FROM `users` WHERE login = %s"
                cursor.execute(self.sql_login, (login))
                value = cursor.fetchall()
                print(value)
                if value == ():
                    info(self, 'Ошибка!', 'Логин не зарегистрирован в системе')
                elif value[0][5] != password:
                    info(self, 'Ошибка!', 'Неверный пароль')
                else:
                    global user_id
                    user_id = value[0][0]
                    self.start_window = StartWindowClass()
                    self.start_window.show()
                    Login.close(self)
        else:
            info(self, 'Ошибка!', 'Не удается подключиться к серверу. Проверьте подключение к интернету')

    def open_registration(self):
        self.registration_window.show()

# регистрация
class RegistrationClass(QMainWindow):
    def __init__(self):
        super(RegistrationClass, self).__init__()
        loadUi("RegistrationWindow.ui", self)
        self.regist_btn.clicked.connect(self.registration)

    def registration(self):
        connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="diplom")
        cursor = connection.cursor()
        if ((self.surname_tb.text() == "") | (self.name_tb.text() == "") | (self.patr_tb.text() == "") | (self.login_tb.text() == "") | (self.pass_tb.text() == "")):
            info(self, 'Ошибка!', 'Заполните все поля!')
        else:
            login = self.login_tb.text()
            cursor.execute("SELECT * FROM `users` WHERE login = %s", login)
            value = cursor.fetchone()
            print(value)
            if value != None:
                info(self, 'Ошибка!', 'Даннный логин уже занят')
            else:
                surname = self.surname_tb.text()
                name = self.name_tb.text()
                patr = self.patr_tb.text()
                password = self.pass_tb.text()
                cursor.execute("INSERT INTO users (surname,name,patronymic,login,password) VALUES (%s,%s,%s,%s,%s)",
                               (surname, name, patr, login, password))
                connection.commit()
                cursor.execute("SELECT id_user FROM `users` WHERE login = %s", login)
                id_user = cursor.fetchone()
                cursor.execute("INSERT INTO storage(id_user,id_fertilizer,amount) VALUES (%s,1,0), (%s,2,0), (%s,3,0)",
                               (id_user, id_user, id_user))
                connection.commit()

# главное меню
class StartWindowClass(QMainWindow):
    def __init__(self):
        super(StartWindowClass, self).__init__()
        loadUi("StartWindow.ui", self)

        self.calc_window = CalcWindowClass()
        self.stock_window = StockWindowClass()

        self.main_btn.clicked.connect(self.open_calc)
        self.stock_btn.clicked.connect(self.open_stock)

    def open_calc(self):
        self.calc_window.show()

    def open_stock(self):
        cursor = connection.cursor()
        cursor.execute("SELECT amount FROM storage WHERE id_user = %s AND id_fertilizer = 1", user_id)
        sql_azote = cursor.fetchone()
        self.stock_window.azot_tb.setText(str(sql_azote[0]))

        cursor.execute("SELECT amount FROM storage WHERE id_user = %s AND id_fertilizer = 2", user_id)
        sql_phosph = cursor.fetchone()
        self.stock_window.phosphor_tb.setText(str(sql_phosph[0]))

        cursor.execute("SELECT amount FROM storage WHERE id_user = %s AND id_fertilizer = 3", user_id)
        sql_potas = cursor.fetchone()
        self.stock_window.potassium_tb.setText(str(sql_potas[0]))

        self.stock_window.show()

# калькулятор
class CalcWindowClass(QMainWindow):
    def __init__(self):
        super(CalcWindowClass, self).__init__()
        loadUi("MainWindow.ui", self)

        # валидация форм ввода
        self.square_tb.setValidator(QDoubleValidator())
        self.quantity_tb.setValidator(QIntValidator())
        self.number_tb.setValidator(QIntValidator())
        self.mass_tb.setValidator(QDoubleValidator())

        # подключение к БД
        cursor = connection.cursor()

        # подключение форм
        self.result_window = ResultWindowClass()
        # self.image_window = ImageWindowClass()

        # подключение функций кнопкам
        # self.load_img_btn.clicked.connect(self.open_img_window)
        self.calc_btn.clicked.connect(self.calc)
        self.clear_btn.clicked.connect(self.clear)

        # подгрузка с/х культур в checkbox
        def cultures(self):
            cursor.execute("SELECT name FROM cultures")
            sql = cursor.fetchall()
            cul_names = []
            for i in sql:
                cul_names.append(i[0])
            self.culture_cb.addItems(cul_names)
        cultures(self)

        # подгрузка фосфорных коэффициентов в checkbox
        def phosphor(self):
            cursor.execute("SELECT DISTINCT level FROM phoshor_coefficient ORDER BY level")
            sql = cursor.fetchall()
            phos_levels = []
            for i in sql:
                phos_levels.append(i[0])
            self.phosphor_cb.addItems(phos_levels)
        phosphor(self)

        # подгрузка калийных коэффициентов в checkbox
        def potassium(self):
            cursor.execute("SELECT DISTINCT level FROM potassium_coefficient ORDER BY level")
            sql = cursor.fetchall()
            pot_levels = []
            for i in sql:
                pot_levels.append(i[0])
            self.potassium_cb.addItems(pot_levels)
        potassium(self)

    def clear(self):
        self.square_tb.setText('')
        self.quantity_tb.setText('')
        self.number_tb.setText('')
        self.mass_tb.setText('')

    # калькулятор удобрений
    def calc(self):
        if ((self.square_tb.text() == "") | (self.quantity_tb.text() == "") | (self.number_tb.text() == "") | (self.mass_tb.text() == "")):
            info(self, 'Ошибка!', 'Заполните все поля!')
        elif (self.square_tb.text() == ',') | (self.mass_tb.text() == ','):
            info(self, 'Ошибка!', 'Введены некорректные данные!')
        else:
            square = float((self.square_tb.text()).replace(",", "."))
            quantity = int(self.quantity_tb.text())
            number = int(self.number_tb.text())
            mass = float(self.mass_tb.text().replace(",", "."))
            phosphor_level = str(self.phosphor_cb.currentText())
            potassium_level = str(self.potassium_cb.currentText())
            culture = str(self.culture_cb.currentText())
            cursor = connection.cursor()

            # азотистые удобрения
            cursor.execute(
                "SELECT ratio FROM data d JOIN cultures c ON d.id_culture = c.id_culture WHERE d.id_fertilizer = 1 AND c.name = '{}'".format(
                    culture))
            azote_sql = cursor.fetchone()
            azote = float(azote_sql[0])
            print(azote)

            # фосфорные удобрения
            cursor.execute(
                "SELECT d.ratio FROM data d JOIN cultures c ON d.id_culture = c.id_culture WHERE d.id_fertilizer = 2 AND c.name = '{}'".format(
                    culture))
            phosphor_sql = cursor.fetchone()
            phosphor = float(phosphor_sql[0])

            # калийные удобрения
            cursor.execute(
                "SELECT d.ratio FROM data d JOIN cultures c ON d.id_culture = c.id_culture WHERE d.id_fertilizer = 3 AND c.name = '{}'".format(
                    culture))
            potassium_sql = cursor.fetchone()
            potassium = float(potassium_sql[0])

            # коэффициент для фосфорных удобрений

            query = 'SELECT p.coefficient FROM phoshor_coefficient p JOIN cultures c ON p.id_culture = c.id_culture ' \
                    'WHERE p.level = "{}" AND c.name = "{}"'.format(phosphor_level, culture)
            cursor.execute(query)
            phos_coeff_sql = cursor.fetchone()
            phos_coeff = float(phos_coeff_sql[0])

            # коэффициент для калийных удобрений
            query = 'SELECT p.coefficient FROM potassium_coefficient p JOIN cultures c ON p.id_culture = c.id_culture ' \
                    'WHERE p.level = "{}" AND c.name = "{}"'.format(potassium_level, culture)
            cursor.execute(query)

            potas_coeff_sql = cursor.fetchone()
            potas_coeff = float(potas_coeff_sql[0])

            harvest = square * ((quantity * number * mass) / 10000)
            result_azote = round(harvest * azote)
            result_phosphor = round(harvest * phosphor * phos_coeff)
            result_potassium = round(harvest * potassium * potas_coeff)

            self.result_window.azot_tb.setText(str(result_azote))
            self.result_window.phosphor_tb.setText(str(result_phosphor))
            self.result_window.potassium_tb.setText(str(result_potassium))

            cursor.execute("SELECT amount FROM storage WHERE id_user = %s AND id_fertilizer = 1", user_id)
            sql_azote = cursor.fetchone()
            self.result_window.azot_storage.setText(str(sql_azote[0]))

            cursor.execute("SELECT amount FROM storage WHERE id_user = %s AND id_fertilizer = 2", user_id)
            sql_phosph = cursor.fetchone()
            self.result_window.phosphor_storage.setText(str(sql_phosph[0]))

            cursor.execute("SELECT amount FROM storage WHERE id_user = %s AND id_fertilizer = 3", user_id)
            sql_potas = cursor.fetchone()
            self.result_window.potassium_storage.setText(str(sql_potas[0]))

            global azote_res
            azote_res = sql_azote[0] - result_azote
            if azote_res < 0:
                azote_status = "Не хватает " + str(abs(azote_res)) + " кг"
            else:
                azote_status = "Достаточно"
            self.result_window.azot_status.setText(azote_status)

            global phosphor_res
            phosphor_res = sql_phosph[0] - result_phosphor
            if phosphor_res < 0:
                phosphor_status = "Не хватает " + str(abs(phosphor_res)) + " кг"
            else:
                phosphor_status = "Достаточно"
            self.result_window.phosphor_status.setText(phosphor_status)

            global potassium_res
            potassium_res = sql_potas[0] - result_potassium
            if potassium_res < 0:
                potassium_status = "Не хватает " + str(abs(potassium_res)) + " кг"
            else:
                potassium_status = "Достаточно"
            self.result_window.potassium_status.setText(potassium_status)

            self.result_window.show()

# окно результатов
class ResultWindowClass(QMainWindow):
    def __init__(self):
        super(ResultWindowClass, self).__init__()
        loadUi("ResultWindow.ui", self)

        cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor

        self.use_btn.clicked.connect(self.use)

    def use(self):
        if ((azote_res < 0) | (phosphor_res < 0) | (potassium_res < 0)):
            info(self, 'Ошибка!', 'Недосточно удобрений для выполнения данной операции')
        else:
            self.cursor.execute("UPDATE storage SET amount = %s WHERE id_user = %s AND id_fertilizer = 1"
                                , (azote_res, user_id))
            self.cursor.execute("UPDATE storage SET amount = %s WHERE id_user = %s AND id_fertilizer = 2"
                                , (phosphor_res, user_id))
            self.cursor.execute("UPDATE storage SET amount = %s WHERE id_user = %s AND id_fertilizer = 3"
                                , (potassium_res, user_id))
            self.connection.commit()
            info(self, 'Успешно!', 'Операция выполнена, изменения сохранены')

# учет
class StockWindowClass(QMainWindow):
    def __init__(self):
        super(StockWindowClass, self).__init__()
        loadUi("StockWindow.ui", self)

        self.azot_tb.setValidator(QIntValidator())
        self.phosphor_tb.setValidator(QIntValidator())
        self.potassium_tb.setValidator(QIntValidator())

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
            self.cursor.execute("UPDATE storage SET amount = %s WHERE id_user = %s AND id_fertilizer = 1",
                                (azote, user_id))
            self.cursor.execute("UPDATE storage SET amount = %s WHERE id_user = %s AND id_fertilizer = 2",
                                (phosphor, user_id))
            self.cursor.execute("UPDATE storage SET amount = %s WHERE id_user = %s AND id_fertilizer = 3",
                                (potassium, user_id))
            self.connection.commit()
            info(self, 'Успешно ', 'Данные сохранены')


app = QApplication(sys.argv)
window = Login()
window.show()
app.exec()



