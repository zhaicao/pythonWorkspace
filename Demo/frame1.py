# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwindows(object):
    def setupUi(self, mainwindows):
        mainwindows.setObjectName("mainwindows")
        mainwindows.resize(476, 541)
        self.centralwidget = QtWidgets.QWidget(mainwindows)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 70, 321, 361))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        mainwindows.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindows)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        mainwindows.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindows)
        self.statusbar.setObjectName("statusbar")
        mainwindows.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(mainwindows)
        QtCore.QMetaObject.connectSlotsByName(mainwindows)

    def retranslateUi(self, mainwindows):
        _translate = QtCore.QCoreApplication.translate
        mainwindows.setWindowTitle(_translate("mainwindows", "MainWindow"))
        self.label.setText(_translate("mainwindows", "业务数据库IP地址"))
        self.pushButton.setText(_translate("mainwindows", "测试"))
        self.label_2.setText(_translate("mainwindows", "业务数据库端口"))
        self.menu.setTitle(_translate("mainwindows", "数据配置"))
        self.menu_2.setTitle(_translate("mainwindows", "Nifi配置"))

