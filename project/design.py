from PyQt6 import QtCore, QtGui, QtWidgets
from connection import *
cursor = connection.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1110, 602)
        # Dialog.setFixedSize(1110, 802)
        Dialog.setStyleSheet("background-color: rgb(141, 196, 145);\n"
"")
        self.load_img_btn = QtWidgets.QPushButton(parent=Dialog)
        self.load_img_btn.setGeometry(QtCore.QRect(700, 60, 261, 61))
        self.load_img_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.load_img_btn.setCheckable(False)
        self.load_img_btn.setAutoRepeatDelay(300)
        self.load_img_btn.setObjectName("load_img_btn")
        self.square_tb = QtWidgets.QLineEdit(parent=Dialog)
        self.square_tb.setGeometry(QtCore.QRect(460, 70, 211, 41))
        self.square_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.square_tb.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.square_tb.setObjectName("square_tb")
        self.square_lbl = QtWidgets.QLabel(parent=Dialog)
        self.square_lbl.setGeometry(QtCore.QRect(290, 60, 151, 51))
        self.square_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.square_lbl.setObjectName("square_lbl")
        self.harvest_lbl = QtWidgets.QLabel(parent=Dialog)
        self.harvest_lbl.setGeometry(QtCore.QRect(180, 140, 341, 51))
        self.harvest_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.harvest_lbl.setObjectName("harvest_lbl")
        self.calc_harvest_btn = QtWidgets.QPushButton(parent=Dialog)
        self.calc_harvest_btn.setGeometry(QtCore.QRect(700, 140, 261, 61))
        self.calc_harvest_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.calc_harvest_btn.setCheckable(False)
        self.calc_harvest_btn.setAutoRepeatDelay(300)
        self.calc_harvest_btn.setObjectName("calc_harvest_btn")
        self.harvest_tb = QtWidgets.QLineEdit(parent=Dialog)
        self.harvest_tb.setGeometry(QtCore.QRect(460, 150, 211, 41))
        self.harvest_tb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.harvest_tb.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.harvest_tb.setObjectName("harvest_tb")
        self.phosphor_cb = QtWidgets.QComboBox(parent=Dialog)
        self.phosphor_cb.setGeometry(QtCore.QRect(460, 250, 501, 41))
        self.phosphor_cb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.phosphor_cb.setObjectName("phosphor_cb")
        self.phosphor_lbl = QtWidgets.QLabel(parent=Dialog)
        self.phosphor_lbl.setGeometry(QtCore.QRect(140, 230, 301, 71))
        self.phosphor_lbl.setSizeIncrement(QtCore.QSize(0, 0))
        self.phosphor_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.phosphor_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.phosphor_lbl.setWordWrap(True)
        self.phosphor_lbl.setObjectName("phosphor_lbl")
        self.potassium_cb = QtWidgets.QComboBox(parent=Dialog)
        self.potassium_cb.setGeometry(QtCore.QRect(460, 330, 501, 41))
        self.potassium_cb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.potassium_cb.setObjectName("potassium_cb")
        self.potassium_lbl = QtWidgets.QLabel(parent=Dialog)
        self.potassium_lbl.setGeometry(QtCore.QRect(140, 310, 301, 71))
        self.potassium_lbl.setSizeIncrement(QtCore.QSize(0, 0))
        self.potassium_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.potassium_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.potassium_lbl.setWordWrap(True)
        self.potassium_lbl.setObjectName("potassium_lbl")
        self.culture_cb = QtWidgets.QComboBox(parent=Dialog)
        self.culture_cb.setGeometry(QtCore.QRect(460, 410, 501, 41))
        self.culture_cb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.culture_cb.setObjectName("culture_cb")
        self.culture_lbl = QtWidgets.QLabel(parent=Dialog)
        self.culture_lbl.setGeometry(QtCore.QRect(140, 390, 301, 71))
        self.culture_lbl.setSizeIncrement(QtCore.QSize(0, 0))
        self.culture_lbl.setStyleSheet("font: 14pt \"Book Antiqua\";")
        self.culture_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.culture_lbl.setWordWrap(True)
        self.culture_lbl.setObjectName("culture_lbl")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 19, 1071, 481))
        self.frame.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.result_lbl = QtWidgets.QLabel(parent=Dialog)
        self.result_lbl.setGeometry(QtCore.QRect(20, 520, 1071, 141))
        self.result_lbl.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.result_lbl.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Book Antiqua\";")
        self.result_lbl.setText("")
        self.result_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_lbl.setObjectName("result_lbl")
        self.calc_btn = QtWidgets.QPushButton(parent=Dialog)
        self.calc_btn.setGeometry(QtCore.QRect(350, 700, 191, 61))
        self.calc_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.calc_btn.setCheckable(False)
        self.calc_btn.setAutoRepeatDelay(300)
        self.calc_btn.setObjectName("calc_btn")
        self.clear_btn = QtWidgets.QPushButton(parent=Dialog)
        self.clear_btn.setGeometry(QtCore.QRect(580, 700, 161, 61))
        self.clear_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 11pt \"Book Antiqua\";")
        self.clear_btn.setCheckable(False)
        self.clear_btn.setAutoRepeatDelay(300)
        self.clear_btn.setObjectName("clear_btn")
        self.frame.raise_()
        self.load_img_btn.raise_()
        self.square_tb.raise_()
        self.square_lbl.raise_()
        self.harvest_lbl.raise_()
        self.calc_harvest_btn.raise_()
        self.harvest_tb.raise_()
        self.phosphor_cb.raise_()
        self.phosphor_lbl.raise_()
        self.potassium_cb.raise_()
        self.potassium_lbl.raise_()
        self.culture_cb.raise_()
        self.culture_lbl.raise_()
        self.result_lbl.raise_()
        self.calc_btn.raise_()
        self.clear_btn.raise_()

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


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.load_img_btn.setText(_translate("Dialog", "Загрузить изображение"))
        self.square_lbl.setText(_translate("Dialog", "Площадь, га"))
        self.harvest_lbl.setText(_translate("Dialog", "Планируемый урожай, ц/га"))
        self.calc_harvest_btn.setText(_translate("Dialog", "Посчитать урожай"))
        self.phosphor_lbl.setText(_translate("Dialog", "Содержание в почве фосфорных соединений"))
        self.potassium_lbl.setText(_translate("Dialog", "Содержание в почве калийных соединений"))
        self.culture_lbl.setText(_translate("Dialog", "Сельскохозяйственная культура"))
        self.calc_btn.setText(_translate("Dialog", "Выполнить"))
        self.clear_btn.setText(_translate("Dialog", "Очистить"))

