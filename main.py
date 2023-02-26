import sys
import os
import PyQt5
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
from functools import partial
import ui_interface
from Custom_Widgets import *#QT-PyQt-PySide-Custom-Widgets

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = ui_interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(800, 600)
        self.show()
        

if __name__ == '__main__':
    