import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
#集成界面生成的wocai。py 要在同一个目录下
from wocai import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("hello")
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
