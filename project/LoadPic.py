from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoadPic(object):
    def setupUi(self, LoadPic):
        LoadPic.setObjectName("LoadPic")
        LoadPic.resize(800, 750)
        LoadPic.setStyleSheet("background-color: rgb(141, 196, 145);")
        self.title_lbl = QtWidgets.QLabel(parent=LoadPic)
        self.title_lbl.setGeometry(QtCore.QRect(180, 10, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(22)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")

        self.retranslateUi(LoadPic)
        QtCore.QMetaObject.connectSlotsByName(LoadPic)

    def retranslateUi(self, LoadPic):
        _translate = QtCore.QCoreApplication.translate
        LoadPic.setWindowTitle(_translate("LoadPic", "Исходное изображение"))
        self.title_lbl.setText(_translate("LoadPic", "Исходное изображение"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadPic = QtWidgets.QWidget()
    ui = Ui_LoadPic()
    ui.setupUi(LoadPic)
    LoadPic.show()
    sys.exit(app.exec())
