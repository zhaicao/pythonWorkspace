
__author__='zhaicao'


import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QLineEdit, QTextEdit

class simple_1(QWidget):
    def __init__(self):
        super().__init__()
        #self.initUI()
        #self.initUI_1()
        #self.initUI_2()
        self.initUI_3()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl1.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Absolute')
        self.show()

    #横向纵向布局
    def initUI_1(self):
        okBut = QPushButton('ok')
        canBut = QPushButton('cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okBut)
        hbox.addWidget(canBut)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    #栅格网格
    def initUI_2(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            but = QPushButton(name)
            grid.addWidget(but, *position)

        self.move(300, 300)
        self.setWindowTitle('计算器')
        self.show()

    #网格多跨几行
    def initUI_3(self):
        title = QLabel('Title')
        作者 = QLabel('Author')
        评审 = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        #控件上下间距
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(作者, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(评审, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = simple_1()
    sys.exit(app.exec_())


