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



def setYear():
    yearArr = misc.getYearArr('./bin/log/')
    for year in yearArr:
        ui.year_combo.addItem(year)

def setMonth():
    ui.month_combo.clear()
    monthArr = misc.getMonthArr('./bin/log/' + ui.year_combo.currentText() + '/')
    for month in monthArr:
        ui.month_combo.addItem(str(month).strip('.txt'))

def leftSlideMenu():
    if ui.left_menu_widget.width() == 0: newWidth = 184
    else: newWidth = 0

    ui.left_menu_widget.setMaximumWidth(newWidth)


def switchPages():
    ui.show_bud_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))
    ui.add_log_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))
    ui.show_inv_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(2))
    ui.add_inv_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(3))

def controls():
    ui.exit_button.clicked.connect(sys.exit)
    ui.minimize_button.clicked.connect(MainWindow.showMinimized)
    # ui.back_button.clicked.connect()

    ui.menu_button.clicked.connect(leftSlideMenu)
    ui.ab_save_button.clicked.connect(saveLog)
    ui.year_combo.currentTextChanged.connect(setMonth)

def saveLog():
    if ui.exp_radio.isChecked(): log_type = 'exp'
    elif ui.inc_radio.isChecked(): log_type = 'inc'
    
    log_place = ui.place_edit.text()
    log_title = ui.title_edit.text()
    log_amount = ui.amount_edit.text()

    filePath = './bin/log/' +  ui.year_combo.currentText() + '/' + ui.month_combo.currentText() + '.txt'
    misc.saveToFile([log_type, log_place, log_title, float(log_amount)], filePath)

if __name__ == "__main__":
    misc.createFiles()

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    controls()
    switchPages()
    setYear()
    
    sys.exit(app.exec_())