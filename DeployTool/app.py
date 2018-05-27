
__author__='zhaicao'

import sys
from PyQt5 import QtWidgets
from DeployTool.frameUI import frameHome
from DeployTool.frameUI import home

if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QWidget()
        ui = frameHome.Ui_Form()
        ui.setupUi(w)
        w.show()
        sys.exit(app.exec_())