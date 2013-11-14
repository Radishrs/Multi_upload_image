__author__ = 'Radish'

import sys

from PySide import QtGui, QtCore


class MainWin(QtGui.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.init_ui()

    def init_ui(self):

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.exit_action())

        self.statusBar()

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Multi upload')

        self.show()

    def exit_action(self):
        exit_act = QtGui.QAction(QtGui.QIcon('img/exit.png'), 'Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setToolTip('Exit application')
        exit_act.triggered.connect(self.close)
        return exit_act

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Quit?', 'Are you done?', QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QtGui.QApplication(sys.argv)
main = MainWin()

sys.exit(app.exec_())