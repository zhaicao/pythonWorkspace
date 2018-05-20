# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form1)
        self.lineEdit.setGeometry(QtCore.QRect(200, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form1)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "Form"))
        self.label.setText(_translate("Form1", "第二个页面"))

