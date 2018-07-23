
__author__ = 'zhaicao'

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QTextEdit
from PyQt5.QtGui import QIcon

class simple(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI_2()

    def initUI(self):
        self.statusBar().showMessage('ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('状态栏')
        self.show()

    def initUI_1(self):
        exitAction = QAction(QIcon('web.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        #创建菜单栏
        menuBar = self.menuBar()
        #添加菜单
        fileMenu = menuBar.addMenu('&File')
        #添加事件
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

    #工具栏
    def initUI_2(self):
        exitAction = QAction(QIcon('web.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('toolBar')
        self.show()


    def initUI_3(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        #增加事件
        exitAction = QAction(QIcon('web.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()
        #增加菜单栏
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        #增加工具栏
        toolBar = self.addToolBar('Exit')
        toolBar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('toolBar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = simple()
    sys.exit(app.exec_())

