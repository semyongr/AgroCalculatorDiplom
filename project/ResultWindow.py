from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(800, 489)
        ResultWindow.setStyleSheet("background-color: rgb(141, 196, 145);")
        self.centralwidget = QtWidgets.QWidget(parent=ResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 761, 441))
        self.frame.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.title_lbl = QtWidgets.QLabel(parent=self.frame)
        self.title_lbl.setGeometry(QtCore.QRect(140, 10, 531, 81))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(22)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("color: rgb(0, 0, 0);")
        self.title_lbl.setObjectName("title_lbl")
        self.result_lbl = QtWidgets.QLabel(parent=self.frame)
        self.result_lbl.setGeometry(QtCore.QRect(30, 100, 701, 311))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(16)
        self.result_lbl.setFont(font)
        self.result_lbl.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.result_lbl.setText("")
        self.result_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_lbl.setObjectName("result_lbl")
        ResultWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=ResultWindow)
        self.statusbar.setObjectName("statusbar")
        ResultWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "Результат"))
        self.title_lbl.setText(_translate("ResultWindow", "Годовые нормы удобрений"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultWindow()
    ui.setupUi(ResultWindow)
    ResultWindow.show()
    sys.exit(app.exec())
