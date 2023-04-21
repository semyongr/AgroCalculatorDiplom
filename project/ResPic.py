from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ResPic(object):
    def setupUi(self, ResPic):
        ResPic.setObjectName("ResPic")
        ResPic.resize(800, 750)
        ResPic.setStyleSheet("background-color: rgb(141, 196, 145);\n"
"")
        self.title_lbl = QtWidgets.QLabel(parent=ResPic)
        self.title_lbl.setGeometry(QtCore.QRect(130, 10, 541, 81))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(22)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")

        self.retranslateUi(ResPic)
        QtCore.QMetaObject.connectSlotsByName(ResPic)

    def retranslateUi(self, ResPic):
        _translate = QtCore.QCoreApplication.translate
        ResPic.setWindowTitle(_translate("ResPic", "Обработанное изображение"))
        self.title_lbl.setText(_translate("ResPic", "Обработанное изображение"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResPic = QtWidgets.QWidget()
    ui = Ui_ResPic()
    ui.setupUi(ResPic)
    ResPic.show()
    sys.exit(app.exec())
