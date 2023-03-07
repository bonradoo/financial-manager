import sys
import os
from PyQt5 import QtWidgets
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt
from functools import partial
from ui_interface import *
from Custom_Widgets import * #QT-PyQt-PySide-Custom-Widgets
import misc



# class UI(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__()
#         self.initUi(self)

#     def initUi(self):


# class UI(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: Qt.WindowFlags = ...) -> None:
#         super().__init__(parent, flags)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

def leftSlideMenu():
    width = ui.left_menu_widget.width()

    if width==0: newWidth=184
    else: newWidth=0

    ui.left_menu_widget.setMaximumWidth(newWidth)
    
    # animation = QtCore.QPropertyAnimation(ui.left_menu_widget, b'size')
    # animation.setStartValue(QtCore.QSize(width, ui.left_menu_widget.height()))
    # animation.setEndValue(QtCore.QSize(newWidth, ui.left_menu_widget.height()))
    # animation.setDuration(550)
    # animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
    # animation.start()

def switchPages():
    ui.show_bud_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))
    ui.add_log_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))
    ui.show_inv_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(2))
    ui.add_inv_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(3))

def controls():
    ui.exit_button.clicked.connect(sys.exit)
    ui.minimize_button.clicked.connect(MainWindow.showMinimized)
    # ui.back_button.clicked.connect(print(1))

    ui.menu_button.clicked.connect(leftSlideMenu)
    ui.ab_save_button.clicked.connect(saveLog)

def saveLog():
    if ui.exp_radio.isChecked(): log_type = 'exp'
    elif ui.inc_radio.isChecked(): log_type = 'inc'
    
    log_place = ui.place_edit.text()
    log_title = ui.title_edit.text()
    log_amount = ui.amount_edit.text()

    YM_input = ui.year_combo.currentText() + '/' + ui.month_combo.currentText()

    misc.saveToFile([log_type, log_place, log_title, float(log_amount)], YM_input)

if __name__ == "__main__":
    misc.createFiles()

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    controls()
    switchPages()
    
    sys.exit(app.exec_())