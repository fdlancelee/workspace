# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyqtLearn1.py'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import *
if __name__ == '__main__':
    app = QApplication(sys.argv)
    '''
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
    '''
    gameshow = QWidget()
    gameshow.resize(900,500)
    gameshow.setWindowTitle('石头剪刀布')
    gameshow.setWindowIcon(QIcon("D:\头像2.jpg"))
    gameshow.show()
    sys.exit(app.exec_())


