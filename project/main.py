import sys
from PyQt6 import QtWidgets
import MainWindow
import connection

class ExampleApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()