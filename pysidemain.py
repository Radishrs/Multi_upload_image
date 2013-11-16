__author__ = 'Radish'
__version__ = '0.2.1'

import sys

from PySide import QtGui, QtCore


class MainWin(QtGui.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.init_ui()

    def init_ui(self):

        #Create actions
        self.create_actions()
        #Create menu
        self.create_menu_bar()
        #ToolBar
        self.create_tool_bar()
        #CENTER
        self.create_center_widget()
        #STATUSBAR
        self.create_status_bar()
        #DEFAULT WINDOW SET
        self.main_window()
        #SHOW WINDOW
        self.show()

    def create_status_bar(self):
        self.statusBar()

    def create_center_widget(self):

        self.text = QtGui.QTextEdit()
        self.table = QtGui.QTableWidget(10, 6)
        self.table.setHorizontalHeaderLabels(['Id', 'name', 'ok', 'fuck', 'this', 'shit'])


        grid = QtGui.QGridLayout()
        grid.addWidget(self.table, 0, 0)
        grid.addWidget(self.text, 0, 1, )
        self.area = QtGui.QWidget(self)
        self.area.setLayout(grid)
        self.setCentralWidget(self.area)

    def create_tool_bar(self):
        self.toolbar = self.addToolBar('Tools')
        self.toolbar.addAction(self.exit_act)
        self.toolbar.addAction(self.open_act)

    def create_menu_bar(self):
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('File')
        self.file_menu.addAction(self.exit_act)
        self.file_menu.addAction(self.open_act)
        self.about_menu = self.menu.addMenu('About')

    def main_window(self):
        self.setGeometry(300, 100, 800, 600)
        self.setWindowTitle('Multi upload')
        self.setWindowIcon(QtGui.QIcon('img/main.png'))

    def create_actions(self):
        self.exit_action()
        self.open_action()

    def exit_action(self):
        tip = 'Exit application'
        self.exit_act = QtGui.QAction(QtGui.QIcon('img/exit.png'), 'Exit', self)
        #exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setToolTip(tip)
        self.exit_act.setStatusTip(tip)
        self.exit_act.triggered.connect(self.close)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Quit?', 'Are you done?', QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def open_action(self):
        tip = 'Add files'
        self.open_act = QtGui.QAction(QtGui.QIcon('img/open.png'), 'Open', self)
        #open_act.setShortcut('Ctrl+O')
        self.open_act.setToolTip(tip)
        self.open_act.setStatusTip(tip)
        self.open_act.triggered.connect(self.show_dialog)

    def show_dialog(self):
        file_names, _ = QtGui.QFileDialog.getOpenFileNames(self, 'Open files', '/')

        for file in file_names:
            self.text.append(file)


app = QtGui.QApplication(sys.argv)
main = MainWin()

sys.exit(app.exec_())