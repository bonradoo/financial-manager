import sys
import os
from PyQt5 import QtWidgets
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QMainWindow, QApplication)
from PySide2.QtCharts import QtCharts
from functools import partial
from ui_interface import *
from Custom_Widgets import * #QT-PyQt-PySide-Custom-Widgets
from random import randrange

class UI(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())