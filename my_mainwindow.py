import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from my_UI import *


class MyMainwindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainwindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainwindow()
    myWin.show()
    sys.exit(app.exec_())