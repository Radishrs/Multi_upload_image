__author__ = 'Radish'

import sys

import PySide.QtCore as qt_core
import PySide.QtGui as qt_gui

app = qt_gui.QApplication(sys.argv)

label = qt_gui.QLabel("Hello world")
label.show()

app.exec_()
sys.exit()
