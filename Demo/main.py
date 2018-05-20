import sys

from PyQt5 import QtWidgets

import sys
import frame1, frame

if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        mainwindow = QtWidgets.QMainWindow()
        ui = frame1.Ui_mainwindows()
        ui.setupUi(mainwindow)
        mainwindow.show()
        sys.exit(app.exec_())