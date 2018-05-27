import sys

from PyQt5 import QtWidgets

import sys
import frame

if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        mainwindow = QtWidgets.QMainWindow()
        ui = frame.Ui_MainWindow()
        ui.setupUi(mainwindow)
        mainwindow.show()
        sys.exit(app.exec_())