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

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("Financial Tracker")

        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.back_button.clicked.connect(lambda: self.restore_or_maximize_window())

    def slideLeftMenu(self):
        width = self.ui.left_menu_widget.width()
        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
        # If maximized
        else:
            newWidth = 0
        # Animate the transition
        self.animation = QtCore.QPropertyAnimation(self.ui.left_menu_widget, b"maximumWidth") #Animate minimumWidht
        self.animation.setDuration(550)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.animation.start()

    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())