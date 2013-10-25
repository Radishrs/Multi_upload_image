__author__ = 'Radish'

import sys

from PySide import QtCore
from PySide import QtGui
from PySide.QtDeclarative import QDeclarativeView

app = QtGui.QApplication(sys.argv)
view = QDeclarativeView()
url = QtCore.QUrl('view.qml')
view.setSource(url)
view.show()

#label = qt_gui.QLabel("<font color=red size=40>Hello world</font>")
#label.show()

sys.exit(app.exec_())
