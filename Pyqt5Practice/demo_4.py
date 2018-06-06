# http://code.py40.com/2004.html
__author__ = 'zhaicao'

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QDesktopWidget, QPushButton

class simple(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Message Box')
        self.show()

    def closeEvent(self, event):
        mesbox = QMessageBox(self)
        mesbox.setWindowTitle('提示')
        okBtn = mesbox.addButton('是', QMessageBox.AcceptRole)
        noBtn = mesbox.addButton('否', QMessageBox.RejectRole)
        mesbox.setText('确定要退出吗？')
        mesbox.exec_()
        #reply = QMessageBox.question(self, '提示', '确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # reply = QMessageBox.information(self, '提示', '确定要退出吗？')
        # okBtn = QPushButton('是',self)
        # noBtn = QPushButton('否',self)
        #     event.accept()
        # else:
        #     event.ignore()

class simple1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.center()
        self.setWindowTitle('居中')
        self.show()

    def center(self):
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中点
        cp = QDesktopWidget().availableGeometry().center()
        #显示要屏幕中点
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = simple()
    sys.exit(app.exec_())