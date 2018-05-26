
__author__ = 'zhaicao'

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QColorDialog,
                             QFrame, QVBoxLayout, QSizePolicy, QLabel, QFontDialog, QTextEdit, QAction, QFileDialog ,QMainWindow)
from PyQt5.QtGui import QColor, QIcon

#通过输入框改变文字
class simple_1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor()

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        #绑定按钮点击信号和槽函数
        self.btn.clicked.connect(self.showDialog)

        self.el = QLineEdit(self)
        self.el.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.el.setText(str(text))

#通过对话框改变颜色
class simple_2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        #绑定按钮点击信号和槽函数
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


#通过对话框改变字体
class simple_3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)


        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


#通过对话框选择文件或目录
class simple_4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('web.png'), 'OPen', self)
        openFile.setShortcut('Ctrl+o')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,
                                            'Open File',
                                            'C:/Users/slave/Desktop',
                                            'Xml Files(*.xml);;Excel Files(*.xls *.xlsx);;Word Files(*.doc)')
        print(fname)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(str(data))

if __name__=='__main__':
    app = QApplication(sys.argv)
    s = simple_4()
    sys.exit(app.exec_())