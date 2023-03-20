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

# saving links for future me
# https://doc.qt.io/qtforpython/tutorials/expenses/expenses.html
# https://www.youtube.com/watch?v=MHn3ZTWcyXk
# https://stackoverflow.com/questions/48362864/how-to-insert-qchartview-in-form-with-qt-designer
# https://www.youtube.com/watch?v=a9Mynu6pC4U

def setTotals():
    filePath = './bin/log/' + ui.year_combo.currentText() + '/' + ui.month_combo.currentText() + '.txt'
    totals = misc.returnTotals(filePath)
    
    ui.ab_expval_label.setText(totals[0])
    ui.ab_incval_label.setText(totals[1])
    ui.ab_balval_label.setText(totals[2])

    ui.ab_expval_label_2.setText(totals[0])
    ui.ab_incval_label_2.setText(totals[1])
    ui.ab_balval_label_2.setText(totals[2])

def setYear():
    yearArr = misc.getYearArr('./bin/log/')
    ui.year_combo.addItems(yearArr)
    ui.year_combo.setCurrentIndex(len(yearArr)-1)


def setMonth():
    ui.month_combo.clear()
    monthArr = misc.getMonthArr('./bin/log/' + ui.year_combo.currentText() + '/')
    ui.month_combo.addItems(str(month).strip('.txt') for month in monthArr)
    ui.month_combo.setCurrentIndex(len(monthArr)-1)
    setTotals()


def leftSlideMenu():
    if ui.left_menu_widget.width() == 0: newWidth = 184
    else: newWidth = 0

    # print(ui.left_menu_widget.width())
    # animation = QtCore.QPropertyAnimation(ui.left_menu_widget, b'maximumWidth')
    # animation.setStartValue(curWidth)
    # animation.setEndValue(newWidth)
    # animation.setDuration(500)
    # animation.start()
    # print(ui.left_menu_widget.height())

    ui.left_menu_widget.setMaximumWidth(newWidth)


def switchPages():
    ui.show_bud_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(0))
    ui.add_log_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(1))
    ui.show_inv_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(2))
    ui.add_inv_button.clicked.connect(lambda: ui.stackedWidget.setCurrentIndex(3))
    
def clearEdits():
    saveLog()
    ui.place_edit.clear()
    ui.title_edit.clear()
    ui.amount_edit.clear()
    ui.place_edit.setFocus()
    setTotals()

def controls():
    ui.exit_button.clicked.connect(sys.exit)
    ui.minimize_button.clicked.connect(MainWindow.showMinimized)
    # ui.back_button.clicked.connect()

    ui.menu_button.clicked.connect(leftSlideMenu)
    ui.ab_save_button.clicked.connect(saveLog)
    ui.year_combo.currentTextChanged.connect(setMonth)

    # Set totals refreshers
    ui.ab_save_button.clicked.connect(setTotals)
    ui.month_combo.activated.connect(setTotals)

    ui.place_edit.returnPressed.connect(clearEdits)
    ui.title_edit.returnPressed.connect(clearEdits)
    ui.amount_edit.returnPressed.connect(clearEdits)


def saveLog():
    try:
        if ui.exp_radio.isChecked(): log_type = 'exp'
        elif ui.inc_radio.isChecked(): log_type = 'inc'
        
        log_place = ui.place_edit.text()
        log_title = ui.title_edit.text()
        log_amount = ui.amount_edit.text()

        filePath = './bin/log/' +  ui.year_combo.currentText() + '/' + ui.month_combo.currentText() + '.txt'
        misc.saveToFile([log_type, log_place, log_title, float(log_amount)], filePath)
    except:
        print('Error')

def pieChart():
    series = QtCharts.QPieSeries()
    series.append('Python', 20)
    series.append('C++', 30)
    series.append('C', 10)

    chart = QtCharts.QChart()
    chart.addSeries(series)
    chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
    chart.setTitle('Test')

    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    lay = QtWidgets.QHBoxLayout()
    # lay.addWidget(chartView)

    ui.bd_exp_widget.setLayout(lay)


    # print(type(chartView))
    # chartView.sizePolicy(QtWidgets.QFrame.Expanding, QtWidgets.QFrame.Expanding)
    # size = QtWidgets.QSizePolicy(QtWidgets.QWidget.Expanding, QtWidgets.QWidget.Expanding)
    # chartView.setSizePolicy(size)
    
    # layout = QtWidgets.QHBoxLayout()
    # layout.addWidget(chartView)
    # ui.exp_graph_frame.setLayout(layout)
    
    


if __name__ == "__main__":
    misc.createFiles()
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    controls()
    switchPages()
    setYear()
    pieChart()
    
    sys.exit(app.exec_())