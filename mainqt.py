__author__ = 'Radish'

import sys


from PySide import QtGui, QtCore


class Communicate(QtCore.QObject):

    close_app = QtCore.Signal()


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.init_ui_font_dialog()

    def init_ui_font_dialog(self):

        vbox = QtGui.QVBoxLayout()

        btn = QtGui.QPushButton("Select font", self)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.show_font_dialog)

        self.lbl = QtGui.QLabel('Knowledge only matters, ПиСайд па русски ни пишед', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def show_font_dialog(self):

        font, ok = QtGui.QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)

    def init_ui_color_dialog(self):

        color = QtGui.QColor(0, 0, 0)

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.show_color_dialog)

        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % color.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def show_color_dialog(self):

        color = QtGui.QColorDialog.getColor()

        if color.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % color.name())

    def init_ui_input_dialog(self):

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('line edit')
        self.show()

    def show_dialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input dialog', 'Enter youre name:')
        if ok:
            self.le.setText(str(text))

    def init_ui_signals_emit(self):

        self.c = Communicate()
        self.c.close_app.connect(self.close)

        self.setGeometry(300, 200, 300, 300)
        self.setWindowTitle('Signals and slots')
        self.show()

    def init_ui_signals_main(self):

        btn1 = QtGui.QPushButton('Button 1', self)
        btn1.move(20, 20)

        btn2 = QtGui.QPushButton('Button 2', self)
        btn2.move(50, 50)

        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.statusBar()

        self.setGeometry(300, 200, 300, 300)
        self.setWindowTitle('Signals and slots')
        self.show()

    def init_ui_signals(self):

        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 200, 300, 300)
        self.setWindowTitle('Signals and slots')
        self.show()

    def init_ui_grid2(self):

        title = QtGui.QLabel("Title")
        author = QtGui.QLabel("Author")
        review = QtGui.QLabel("Review")

        title_edit = QtGui.QLineEdit()
        author_edit = QtGui.QLineEdit()
        review_edit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(review_edit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    def init_ui_grid(self):

        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
                 '4', '5', '6', '*', '1', '2', '3', '-',
                 '0', '.', '=', '+']

        grid = QtGui.QGridLayout()

        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3),
               (4, 0,), (4, 1), (4, 2), (4, 3)]

        for i in names:
            button = QtGui.QPushButton(i)
            if j == 2:
                grid.addWidget(QtGui.QLabel(''), 0, 2)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1

        self.setLayout(grid)

        self.setWindowTitle('Calculator')
        self.move(300, 150)
        self.show()

    def init_ui_main(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('Their some text in <b>HTML</b> bitch!')

        btn = QtGui.QPushButton("Quit")  # Текст кнопки и ссылка на окно в которое добавить.
        btn2 = QtGui.QPushButton("Open")
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.setToolTip('This is <b>BUTTON</b> bitch')
        btn.resize(btn.sizeHint())
        #btn.move(100, 100)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(btn2)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        #exit_action = QtGui.QAction(QtGui.QIcon('img\exit.png'), 'Exit', self)
        #exit_action.setShortcut('Ctrl+Q')
        #exit_action.setStatusTip('Exit application')
        #exit_action.triggered.connect(self.close)
        #
        #menu_bar = self.menuBar()
        #file_menu = menu_bar.addMenu('File')
        #file_menu.addAction(exit_action)
        #
        #toolbar = self.addToolBar('Exit')
        #toolbar.addAction(exit_action)
        #
        #self.statusBar()

        self.setGeometry(300, 250, 450, 350)
        #self.center()
        self.setWindowTitle('name of window')
        self.setWindowIcon(QtGui.QIcon('img/main.png'))

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

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def button_clicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    #def mousePressEvent(self, event):

        #self.c.close_app.emit()

app = QtGui.QApplication(sys.argv)
examp = Example()

sys.exit(app.exec_())
