__author__ = 'Radish'

import sys

from PySide import QtGui, QtCore


class MainWin(QtGui.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.init_ui()

    def init_ui(self):
        exit_act = self.exit_action()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_act)

        toolbar = self.addToolBar('Tools')
        toolbar.addAction(exit_act)
        toolbar.addAction(self.open_action())

        QtGui.QToolTip.setFont(QtGui.QFont('Minion Pro', 10))
        self.statusBar()

        self.text = QtGui.QTextEdit()
        self.setCentralWidget(self.text)

        self.main_window()
        self.show()

    def main_window(self):
        self.setGeometry(300, 200, 600, 400)
        self.setWindowTitle('Multi upload')
        self.setWindowIcon(QtGui.QIcon('img/main.png'))

    def exit_action(self):
        tip = 'Exit application'
        exit_act = QtGui.QAction(QtGui.QIcon('img/exit.png'), 'Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setToolTip(tip)
        exit_act.setStatusTip(tip)
        exit_act.triggered.connect(self.close)
        return exit_act

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Quit?', 'Are you done?', QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def open_action(self):
        tip = 'Add files'
        open_act = QtGui.QAction(QtGui.QIcon('img/open.png'), 'Open', self)
        open_act.setShortcut('Ctrl+O')
        open_act.setToolTip(tip)
        open_act.setStatusTip(tip)
        open_act.triggered.connect(self.show_dialog)
        return open_act

    def show_dialog(self):
        file_names, _ = QtGui.QFileDialog.getOpenFileNames(self, 'Open files', '/home')

        for file in file_names:
            self.text.append(file)


app = QtGui.QApplication(sys.argv)
main = MainWin()

sys.exit(app.exec_())