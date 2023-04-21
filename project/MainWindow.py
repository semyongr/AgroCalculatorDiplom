from PyQt6 import QtCore, QtGui, QtWidgets
from ResultWindow import *
from connection import *
cursor = connection.cursor()

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Ui_ResultWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 626)
        MainWindow.setStyleSheet("background-color: rgb(141, 196, 145);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.potassium_cb = QtWidgets.QComboBox(parent=self.centralwidget)
        self.potassium_cb.setGeometry(QtCore.QRect(590, 350, 381, 41))
        self.potassium_cb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 14pt \"Book Antiqua\";")
        self.potassium_cb.setObjectName("potassium_cb")
        self.culture_cb = QtWidgets.QComboBox(parent=self.centralwidget)
        self.culture_cb.setGeometry(QtCore.QRect(590, 430, 381, 41))
        self.culture_cb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 14pt \"Book Antiqua\";")
        self.culture_cb.setObjectName("culture_cb")
        self.clear_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(590, 530, 161, 61))
        self.clear_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.clear_btn.setCheckable(False)
        self.clear_btn.setAutoRepeatDelay(300)
        self.clear_btn.setObjectName("clear_btn")
        self.quantity_tb = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.quantity_tb.setGeometry(QtCore.QRect(210, 160, 151, 41))
        self.quantity_tb.setStyleSheet("font: 14pt \"Book Antiqua\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.quantity_tb.setObjectName("quantity_tb")
        self.load_img_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.load_img_btn.setGeometry(QtCore.QRect(660, 60, 261, 61))
        self.load_img_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.load_img_btn.setCheckable(False)
        self.load_img_btn.setAutoRepeatDelay(300)
        self.load_img_btn.setObjectName("load_img_btn")
        self.phosphor_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.phosphor_lbl.setGeometry(QtCore.QRect(150, 250, 421, 71))
        self.phosphor_lbl.setSizeIncrement(QtCore.QSize(0, 0))
        self.phosphor_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.phosphor_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.phosphor_lbl.setWordWrap(True)
        self.phosphor_lbl.setObjectName("phosphor_lbl")
        self.phosphor_cb = QtWidgets.QComboBox(parent=self.centralwidget)
        self.phosphor_cb.setGeometry(QtCore.QRect(590, 270, 381, 41))
        self.phosphor_cb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 14pt \"Book Antiqua\";")
        self.phosphor_cb.setObjectName("phosphor_cb")
        self.square_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.square_lbl.setGeometry(QtCore.QRect(250, 60, 151, 51))
        self.square_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.square_lbl.setObjectName("square_lbl")
        self.potassium_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.potassium_lbl.setGeometry(QtCore.QRect(120, 330, 451, 71))
        self.potassium_lbl.setSizeIncrement(QtCore.QSize(0, 0))
        self.potassium_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.potassium_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.potassium_lbl.setWordWrap(True)
        self.potassium_lbl.setObjectName("potassium_lbl")
        self.square_tb = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.square_tb.setGeometry(QtCore.QRect(420, 70, 211, 41))
        self.square_tb.setStyleSheet("font: 14pt \"Book Antiqua\";\n"
"background-color: rgb(255, 255, 255);")
        self.square_tb.setObjectName("square_tb")
        self.MainWindow_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.MainWindow_2.setGeometry(QtCore.QRect(20, 19, 1061, 481))
        self.MainWindow_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.MainWindow_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.MainWindow_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.MainWindow_2.setObjectName("MainWindow_2")
        self.quantity_lbl_2 = QtWidgets.QLabel(parent=self.MainWindow_2)
        self.quantity_lbl_2.setGeometry(QtCore.QRect(30, 120, 151, 81))
        self.quantity_lbl_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.quantity_lbl_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.quantity_lbl_2.setStyleSheet("font: 14pt \"Book Antiqua\";\n"
"color: rgb(0, 0, 0);")
        self.quantity_lbl_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.quantity_lbl_2.setWordWrap(True)
        self.quantity_lbl_2.setObjectName("quantity_lbl_2")
        self.number_lbl_2 = QtWidgets.QLabel(parent=self.MainWindow_2)
        self.number_lbl_2.setGeometry(QtCore.QRect(380, 130, 151, 71))
        self.number_lbl_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.number_lbl_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.number_lbl_2.setStyleSheet("font: 14pt \"Book Antiqua\";\n"
"color: rgb(0, 0, 0);")
        self.number_lbl_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.number_lbl_2.setWordWrap(True)
        self.number_lbl_2.setObjectName("number_lbl_2")
        self.number_tb_2 = QtWidgets.QLineEdit(parent=self.MainWindow_2)
        self.number_tb_2.setGeometry(QtCore.QRect(550, 140, 151, 41))
        self.number_tb_2.setStyleSheet("font: 14pt \"Book Antiqua\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"
"")
        self.number_tb_2.setObjectName("number_tb_2")
        self.mass_lbl_2 = QtWidgets.QLabel(parent=self.MainWindow_2)
        self.mass_lbl_2.setGeometry(QtCore.QRect(740, 130, 141, 71))
        self.mass_lbl_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.mass_lbl_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.mass_lbl_2.setStyleSheet("font: 14pt \"Book Antiqua\";\n"
"color: rgb(0, 0, 0);")
        self.mass_lbl_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mass_lbl_2.setWordWrap(True)
        self.mass_lbl_2.setObjectName("mass_lbl_2")
        self.mass_tb_2 = QtWidgets.QLineEdit(parent=self.MainWindow_2)
        self.mass_tb_2.setGeometry(QtCore.QRect(890, 140, 151, 41))
        self.mass_tb_2.setStyleSheet("font: 14pt \"Book Antiqua\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"
"")
        self.mass_tb_2.setObjectName("mass_tb_2")
        self.culture_lbl = QtWidgets.QLabel(parent=self.centralwidget)
        self.culture_lbl.setGeometry(QtCore.QRect(140, 410, 431, 71))
        self.culture_lbl.setSizeIncrement(QtCore.QSize(0, 0))
        self.culture_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.culture_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.culture_lbl.setWordWrap(True)
        self.culture_lbl.setObjectName("culture_lbl")
        self.calc_btn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.calc_btn.setGeometry(QtCore.QRect(370, 530, 191, 61))
        self.calc_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.calc_btn.setCheckable(False)
        self.calc_btn.setAutoRepeatDelay(300)
        self.calc_btn.setObjectName("calc_btn")
        self.MainWindow_2.raise_()
        self.square_tb.raise_()
        self.clear_btn.raise_()
        self.potassium_lbl.raise_()
        self.culture_lbl.raise_()
        self.load_img_btn.raise_()
        self.phosphor_cb.raise_()
        self.phosphor_lbl.raise_()
        self.calc_btn.raise_()
        self.culture_cb.raise_()
        self.quantity_tb.raise_()
        self.square_lbl.raise_()
        self.potassium_cb.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        def cultures(self):
                self.connection = connection
                self.cursor = cursor
                self.cursor.execute("SELECT culture FROM fertilizers ")
                self.sql = cursor.fetchall()
        cultures(self)
        self.cul_names = []
        for i in self.sql:
                self.cul_names.append(i[0])
        self.culture_cb.addItems(self.cul_names)

        def potassium(self):
                self.connection = connection
                self.cursor = cursor
                self.cursor.execute("SELECT DISTINCT level FROM potassium_coeff ORDER BY level")
                self.sql = cursor.fetchall()
        potassium(self)
        self.pot_levels = []
        for i in self.sql:
                self.pot_levels.append(i[0])
        self.potassium_cb.addItems(self.pot_levels)

        def phosphor(self):
                self.connection = connection
                self.cursor = cursor
                self.cursor.execute("SELECT DISTINCT level FROM phoshor_coeff ORDER BY level")
                self.sql = cursor.fetchall()
        phosphor(self)
        self.phos_levels = []
        for i in self.sql:
                self.phos_levels.append(i[0])
        self.phosphor_cb.addItems(self.phos_levels)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчет количества норм удобрений"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))
        self.load_img_btn.setText(_translate("MainWindow", "Обработать изображение"))
        self.phosphor_lbl.setText(_translate("MainWindow", "Содержание в почве фосфорных соединений"))
        self.square_lbl.setText(_translate("MainWindow", "Площадь, га"))
        self.potassium_lbl.setText(_translate("MainWindow", "Содержание в почве калийных соединений"))
        self.quantity_lbl_2.setText(_translate("MainWindow", "Количество колосьев на 1 кв. м, шт."))
        self.number_lbl_2.setText(_translate("MainWindow", "Число зёрен в колосе, шт."))
        self.mass_lbl_2.setText(_translate("MainWindow", "Масса 1000 зёрен, г"))
        self.culture_lbl.setText(_translate("MainWindow", "Сельскохозяйственная культура"))
        self.calc_btn.setText(_translate("MainWindow", "Выполнить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
