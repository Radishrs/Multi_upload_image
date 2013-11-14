__author__ = 'Radish'

import sys

#from PySide import QtCore
from PySide import QtGui, QtCore
#from PySide.QtDeclarative import QDeclarativeView


###########
#app = QtGui.QApplication(sys.argv)
#view = QDeclarativeView()
#url = QtCore.QUrl('view.qml')
#view.setSource(url)
#view.show()


#label = qt_gui.QLabel("<font color=red size=40>Hello world</font>")
#label.show()
############################

#app = QtGui.QApplication(sys.argv)
#
#wid = QtGui.QWidget()
#wid.resize(200, 200)
#wid.setWindowTitle("Test example")
#wid.show()
#############

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('Their some text in <b>HTML</b> bitch!')

        btn = QtGui.QPushButton("Quit", self)  # Текст кнопки и ссылка на окно в которое добавить.
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.setToolTip('This is <b>BUTTON</b> bitch')
        btn.resize(btn.sizeHint())
        btn.move(100, 100)

        exit_action = QtGui.QAction(QtGui.QIcon('img\exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_action)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)

        self.statusBar()

        self.setGeometry(300, 250, 450, 350)
        self.center()
        self.setWindowTitle('name of window')
        self.setWindowIcon(QtGui.QIcon('img/icon.png'))

        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "u want exit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        #print(qr, '\n', cp)
        qr.moveCenter(cp)
        #print(qr, qr.topLeft())
        self.move(qr.topLeft())

app = QtGui.QApplication(sys.argv)
examp = Example()

sys.exit(app.exec_())
