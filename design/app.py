# coding=utf-8

from __future__ import division
from design.MainData import MainData
from canvas import *
from algorithm import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtWidgets import (qApp,
                             QAction,
                             QComboBox,
                             QDesktopWidget,
                             QFileDialog,
                             QGridLayout,
                             QInputDialog,
                             QRadioButton,
                             QLabel,
                             QLCDNumber,
                             QMainWindow,
                             QMessageBox,
                             QPushButton,
                             QSpinBox,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextEdit,
                             QToolTip,
                             QWidget)


# noinspection PyNonAsciiChar
class App(QMainWindow, MainData):
    """
    @
    """

    # noinspection PyArgumentList,PyMissingConstructor
    def __init__(self):
        # noinspection PyCompatibility
        QMainWindow.__init__(self)

        # noinspection PyCallByClass,PyTypeChecker
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(100, 100, 900, 550)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('MathDemo')
        self.setWindowIcon(QIcon('python.png'))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.actionLoad()

        self.menuBarLoad()

        #############################################
        # set current image that you are operating. #
        #############################################
        self.currentImage = ""
        self.rainImage()

        self.statusBar().showMessage('Ready')

        self.show()

    def actionLoad(self):
        """
        set MainData.action
        """

        self.action["showOpenDialog"] = QAction('Open File', self)
        self.action["showOpenDialog"].setIcon(QIcon('open.png'))
        self.action["showOpenDialog"].setShortcut('Ctrl+O')
        self.action["showOpenDialog"].setStatusTip('Open File')
        self.action["showOpenDialog"].triggered.connect(self.showOpenDialog)

        self.action["qApp.quit"] = QAction('Exit application', self)
        self.action["qApp.quit"].setIcon(QIcon('exit.jpg'))
        self.action["qApp.quit"].setShortcut('Ctrl+Q')
        self.action["qApp.quit"].setStatusTip('Exit application')
        self.action["qApp.quit"].triggered.connect(qApp.quit)

        self.action["orthogonalTableImage"] = QAction('Orthogonal Table', self)
        self.action["orthogonalTableImage"].setIcon(QIcon('numpy_logo.jpg'))
        self.action["orthogonalTableImage"].setShortcut('Ctrl+T')
        self.action["orthogonalTableImage"].setStatusTip('Orthogonal Table')
        self.action["orthogonalTableImage"].triggered.connect(self.orthogonalTableImage)

        self.action["convexHullImage"] = QAction('Convex Hull', self)
        self.action["convexHullImage"].setIcon(QIcon('numpy_logo.jpg'))
        self.action["convexHullImage"].setShortcut('Ctrl+C')
        self.action["convexHullImage"].setStatusTip('Convex Hull')
        self.action["convexHullImage"].triggered.connect(self.convexHullImage)

        self.action["gravitationalSystemImage"] = QAction('Gravitational System', self)
        self.action["gravitationalSystemImage"].setIcon(QIcon('scipy_logo.jpg'))
        self.action["gravitationalSystemImage"].setShortcut('Ctrl+G')
        self.action["gravitationalSystemImage"].setStatusTip('Gravitational System')
        self.action["gravitationalSystemImage"].triggered.connect(self.gravitationalSystemImage)

        self.action["analyticFunctionImage"] = QAction('Analytic Function', self)
        self.action["analyticFunctionImage"].setIcon(QIcon('numpy_logo.jpg'))
        self.action["analyticFunctionImage"].setShortcut('Ctrl+A')
        self.action["analyticFunctionImage"].setStatusTip('Analytic Function')
        self.action["analyticFunctionImage"].triggered.connect(self.analyticFunctionImage)

        self.action["sourceCodeImage"] = QAction('Source Code', self)
        self.action["sourceCodeImage"].setShortcut('F2')
        self.action["sourceCodeImage"].setStatusTip('Source Code')
        self.action["sourceCodeImage"].triggered.connect(self.sourceCodeImage)

    def menuBarLoad(self):
        """
        set MainWindow.menuBar
        """
        self.statusBar()
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.action["showOpenDialog"])
        fileMenu.addAction(self.action["qApp.quit"])

        statisticsMenu = menubar.addMenu('&Statistics')
        statisticsMenu.addAction(self.action["orthogonalTableImage"])

        statisticsMenu = menubar.addMenu('&Geometry')
        statisticsMenu.addAction(self.action["convexHullImage"])

        statisticsMenu = menubar.addMenu('&Ode')
        statisticsMenu.addAction(self.action["gravitationalSystemImage"])

        statisticsMenu = menubar.addMenu('&Complex')
        statisticsMenu.addAction(self.action["analyticFunctionImage"])

        statisticsMenu = menubar.addMenu('&Help')
        statisticsMenu.addAction(self.action["sourceCodeImage"])

    def controlLayout(self, layout=None, name=None, var=None, position=None, signal=None):
        """
        control layout
        :param layout: GridLayout = QGridLayout()
        :param name: name of control, name is a string
        :param var: var is a dict
        :param position: position is a list with 4 numeric
        :param signal: signal function
        """
        if name == "QLabel":
            # var = {"text": [string]}
            for j in range(0, len(position)):
                self.control[name].append(QLabel(var["text"][j]))
                self.control[name][-1].setAlignment(Qt.AlignCenter)
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])

        if name == "QTabWidget":
            # var = {"text": [[string]], "widget": [[PyQt5.QtWidgets.QWidget]]}
            for j in range(0, len(position)):
                self.control[name].append(QTabWidget())
                for k in range(0, len(var["text"][j])):
                    self.control[name][-1].addTab(var["widget"][j][k], self.tr(var["text"][j][k]))
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])

        if name == "QPushButton":
            # var = {"text": [string]}
            for j in range(0, len(position)):
                self.control[name].append(QPushButton(var["text"][j]))
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])
                if signal is not None:
                    self.control[name][-1].clicked.connect(signal)

        if name == "QTextEdit":
            # var = {"text": [[string]]}
            for j in range(0, len(position)):
                self.control[name].append(QTextEdit())
                if len(var["text"]) != 0:
                    if len(var["text"][j]) != 0:
                        for line in var["text"][j]:
                            self.control[name][-1].append(line)
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])

        if name == "QRadioButton":
            # var = {"text": [string], "isChecked": [bool]}
            for j in range(0, len(position)):
                self.control[name].append(QRadioButton(var["text"][j]))
                self.control[name][-1].setChecked(var["isChecked"][j])
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])
                if signal is not None:
                    self.control[name][-1].clicked.connect(signal)

        if name == "QComboBox":
            # var = {"itemText": [[string]], "currentIndex": [int]}
            for j in range(0, len(position)):
                self.control[name].append(QComboBox())
                self.control[name][-1].addItems(var["itemText"][j])
                if len(var["currentIndex"]) != 0:
                    self.control[name][-1].setCurrentIndex(var["currentIndex"][j])
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])
                if signal is not None:
                    self.control[name][-1].currentIndexChanged.connect(signal)

        if name == "QSpinBox":
            # var = {"range": [[int, int]], "singleStep": [int], "prefix": [string], "suffix": [string], "value": [int]}
            for j in range(0, len(position)):
                self.control[name].append(QSpinBox())
                self.control[name][-1].setRange(var["range"][j][0], var["range"][j][1])
                self.control[name][-1].setSingleStep(var["singleStep"][j])
                if len(var["prefix"]) != 0:
                    if len(var["prefix"][j]) != 0:
                        self.control[name][-1].setPrefix(var["prefix"][j])
                if len(var["suffix"]) != 0:
                    if len(var["suffix"][j]) != 0:
                        self.control[name][-1].setSuffix(var["suffix"][j])
                self.control[name][-1].setValue(var["value"][j])
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])
                if signal is not None:
                    self.control[name][-1].valueChanged.connect(signal)

        if name == "QTableWidget":
            # var = {"headerLabels": [[string]], "data": [numpy.array]}
            for i in range(0, len(position)):
                self.control[name].append(QTableWidget(1, 1))
                if len(var["headerLabels"]) != 0:
                    if len(var["headerLabels"][i]) != 0:
                        self.control[name][-1].setColumnCount(len(var["headerLabels"][i]))
                        self.control[name][-1].setHorizontalHeaderLabels(var["headerLabels"][i])
                if len(var["data"]) != 0:
                    if len(var["data"][i]) != 0:
                        row, column = var["data"][i].shape
                        self.control[name][-1].setRowCount(row)
                        self.control[name][-1].setColumnCount(column)
                        for j in range(0, row):
                            for k in range(0, column):
                                newItem = QTableWidgetItem(str(var["data"][i][j][k]))
                                self.control[name][-1].setItem(j, k, newItem)
                self.control[name][-1].resizeColumnsToContents()
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[i][0], position[i][1], position[i][2], position[i][3])

        if name == "QLCDNumber":
            # var = {"value": [int]}
            for j in range(0, len(position)):
                self.control[name].append(QLCDNumber(self))
                if len(var["value"]) != 0:
                    if len(var["value"][j]) != 0:
                        self.control[name][-1].display(var["value"][j])
                    else:
                        self.control[name][-1].display(0)
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])

    def imageRead(self, imageName=None):
        """
        load data into current page, or write data from current page.
        """
        if len(self.control["QRadioButton"]) != 0:
            length = len(self.control["QRadioButton"])
            for j in range(0, length):
                isChecked = self.controlData[imageName]["QRadioButton"]["isChecked"][j]
                self.control["QRadioButton"][j].setChecked(isChecked)

        if len(self.control["QComboBox"]) != 0:
            pass

        if len(self.control["QComboBox"]) != 0:
            length = len(self.control["QComboBox"])
            for j in range(0, length):
                currentIndex = self.controlData[imageName]["QComboBox"]["currentIndex"][j]
                self.control["QComboBox"][j].setCurrentIndex(currentIndex)

        if len(self.control["QSpinBox"]) != 0:
            length = len(self.control["QSpinBox"])
            for j in range(0, length):
                value = self.controlData[imageName]["QSpinBox"]["value"][j]
                self.control["QSpinBox"][j].setValue(value)

        if len(self.control["QTableWidget"]) != 0:
            length = len(self.control["QTableWidget"])
            for i in range(0, length):
                data = self.controlData[imageName]["QTableWidget"]["data"][i]
                row, column = data.shape
                self.control["QTableWidget"][i].setRowCount(row)
                self.control["QTableWidget"][i].setColumnCount(column)
                for j in range(0, row):
                    for k in range(0, column):
                        newItem = QTableWidgetItem(str(data[j][k]))
                        self.control["QTableWidget"][i].setItem(j, k, newItem)
                self.control["QTableWidget"][i].resizeColumnsToContents()

        if len(self.control["QLCDNumber"]) != 0:
            length = len(self.control["QLCDNumber"])
            for j in range(0, length):
                value = self.controlData[imageName]["QLCDNumber"]["value"][j]
                self.control["QLCDNumber"][j].display(value)

    def rainImage(self):
        """
        @
        """
        self.currentImage = "rainImage"
        self.controlClear()

        layout = QGridLayout()
        layout.setSpacing(10)

        # noinspection PyArgumentList
        widget = QWidget()
        self.canvas["rainImage"] = RainCanvas(parent=widget)
        layout.addWidget(self.canvas["rainImage"])

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def orthogonalTableImage(self):
        """
        layout and initialization data
        """
        ##########################
        # layout of current page #
        ##########################
        self.currentImage = "orthogonalTableImage"
        self.controlClear()

        layout = QGridLayout()
        layout.setSpacing(10)

        text = ['水平数', '重复次数', '实验次数', '因素数']
        position = [[0, 0, 1, 1], [0, 2, 1, 1], [0, 4, 1, 1], [0, 6, 1, 1]]
        self.controlLayout(layout=layout, name="QLabel", var={"text": text}, position=position, signal=None)

        itemText = [list(map(str, range(2, 10))), list(map(str, range(0, 10)))]
        position = [[0, 1, 1, 1], [0, 3, 1, 1]]
        self.controlLayout(layout=layout, name="QComboBox", var={"itemText": itemText, "currentIndex": []},
                           position=position, signal=self.orthogonalTableImageSignal)

        position = [[0, 5, 1, 1], [0, 7, 1, 1]]
        self.controlLayout(layout=layout, name="QLCDNumber", var={"value": []}, position=position, signal=None)

        # noinspection PyArgumentList
        widget = [[QWidget(), QWidget()]]
        for j in range(0, 2):
            widgetLayout = QGridLayout()
            position = [[0, 0, 1, 1]]
            self.controlLayout(layout=widgetLayout, name="QTableWidget", var={"headerLabels": [], "data": []},
                               position=position, signal=None)
            widget[0][j].setLayout(widgetLayout)
        text = [["Table", "Title"]]
        position = [[1, 0, 1, 8]]
        self.controlLayout(layout=layout, name="QTabWidget", var={"text": text, "widget": widget},
                           position=position, signal=None)

        # noinspection PyArgumentList
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        ###########################################################################
        # initialization self.controlData["orthogonalTableImage"] then refresh it #
        # refresh self.control["orthogonalTableImage"]                            #
        ###########################################################################
        if "orthogonalTableImage" not in self.controlData:
            self.addFrame("orthogonalTableImage")
            self.orthogonalTableImageSignal()
        else:
            for j in range(0, len(self.control["QComboBox"])):
                self.control["QComboBox"][j].currentIndexChanged.disconnect(self.orthogonalTableImageSignal)
            self.imageRead(imageName="orthogonalTableImage")
            for j in range(0, len(self.control["QComboBox"])):
                self.control["QComboBox"][j].currentIndexChanged.connect(self.orthogonalTableImageSignal)

        self.statusBar().showMessage('Ready')

    def orthogonalTableImageSignal(self):
        """
        respond of current page(orthogonalTableImage), then write data into MainData.controlData
        """
        self.statusBar().showMessage('Starting generate table and title...')

        ###########################################################
        # initialization self.controlData["orthogonalTableImage"] #
        ###########################################################
        imageName = "orthogonalTableImage"
        self.controlDataClear(imageName)

        ####################################################
        # refresh self.controlData["orthogonalTableImage"] #
        ####################################################
        for j in range(0, len(self.control["QComboBox"])):
            itemText = list()
            for k in range(0, self.control["QComboBox"][j].count()):
                itemText.append(self.control["QComboBox"][j].itemText(k))
            self.controlData[imageName]["QComboBox"]["itemText"].append(itemText)

            currentIndex = self.control["QComboBox"][j].currentIndex()
            self.controlData[imageName]["QComboBox"]["currentIndex"].append(currentIndex)

        level = int(self.control["QComboBox"][0].currentText())
        time = int(self.control["QComboBox"][1].currentText())
        obj = OrthogonalTableMap(level, time)
        row, column = obj.table.shape

        self.controlData[imageName]["QLCDNumber"]["value"].append(row)
        self.controlData[imageName]["QLCDNumber"]["value"].append(column)

        self.controlData[imageName]["QTableWidget"]["data"].append(obj.table)
        self.controlData[imageName]["QTableWidget"]["data"].append(obj.title)

        self.controlData[imageName]["save"] = [level, time, obj.table, obj.title]

        ################################################
        # refresh self.control["orthogonalTableImage"] #
        ################################################
        for j in range(0, len(self.control["QComboBox"])):
            self.control["QComboBox"][j].currentIndexChanged.disconnect(self.orthogonalTableImageSignal)
        self.imageRead(imageName=imageName)
        for j in range(0, len(self.control["QComboBox"])):
            self.control["QComboBox"][j].currentIndexChanged.connect(self.orthogonalTableImageSignal)

        if obj.error == 1:
            self.statusBar().showMessage('Unable to generate title.')
        else:
            self.statusBar().showMessage('Table and title generated.')

    def gravitationalSystemImage(self):
        """
        layout and initialization data
        """
        ##########################
        # layout of current page #
        ##########################
        self.currentImage = "gravitationalSystemImage"
        self.controlClear()

        layout = QGridLayout()
        layout.setSpacing(10)

        text = ['长度单位', '时间单位', '质量单位', '电量单位',
                '质点类型', '质点个数', '动画时长', '总帧数', '播放速率',
                '坐标轴标签', '视角', '速度矢量', '加速度矢量']
        position = [[0, 0, 1, 1], [0, 1, 1, 1], [0, 2, 1, 1], [0, 3, 1, 1],
                    [0, 4, 1, 1], [0, 5, 1, 1], [0, 6, 1, 1], [2, 0, 1, 1], [2, 1, 1, 1],
                    [2, 2, 1, 1], [2, 3, 1, 1], [2, 4, 1, 1], [2, 5, 1, 1]]
        self.controlLayout(layout=layout, name="QLabel", var={"text": text}, position=position, signal=None)

        itemText = [['ly', 'km', 'm', 'mm', 'nm'], ['year', 'day', 's', 'ms', 'μs'],
                    ['kg', '太阳(1.99+e30kg)', '质子(1.7-e27kg)', '电子(9.1-e31kg)'], ['C', 'e(1.6-e19C)'],
                    ['天体-天体', '电荷-电荷', '自定义-自定义'], list(map(str, range(2, 10))),
                    list(map(str, range(5, 65, 5))), ['100', '1000', '10000', '100000'],
                    ['显示', '隐藏'], ['静止', '旋转'], ['隐藏速度矢量', '显示当前速度矢量', '显示所有速度矢量'],
                    ['隐藏加速度矢量', '显示当前加速度矢量', '显示所有加速度矢量']]
        currentIndex = [2, 2, 0, 0, 2, 1, 2, 2, 0, 1, 1, 1]
        position = [[1, 0, 1, 1], [1, 1, 1, 1], [1, 2, 1, 1], [1, 3, 1, 1],
                    [1, 4, 1, 1], [1, 5, 1, 1], [1, 6, 1, 1], [3, 0, 1, 1],
                    [3, 2, 1, 1], [3, 3, 1, 1], [3, 4, 1, 1], [3, 5, 1, 1]]
        self.controlLayout(layout=layout, name="QComboBox", var={"itemText": itemText, "currentIndex": currentIndex},
                           position=position, signal=self.gravitationalSystemImageSignal)

        var = {"range": [[1, 1000]], "singleStep": [1], "prefix": ['X  '], "suffix": ["  倍"], "value": [100]}
        position = [[3, 1, 1, 1]]
        self.controlLayout(layout=layout, name="QSpinBox", var=var,
                           position=position, signal=self.gravitationalSystemImageSignal)

        text = ['启用调试单位']
        isChecked = [True]
        position = [[2, 6, 1, 1]]
        self.controlLayout(layout=layout, name="QRadioButton", var={"text": text, "isChecked": isChecked},
                           position=position, signal=self.gravitationalSystemImageSignal)

        text = ['播放动画']
        position = [[3, 6, 1, 1]]
        self.controlLayout(layout=layout, name="QPushButton", var={"text": text},
                           position=position, signal=self.gravitationalSystemImageDraw)

        # noinspection PyArgumentList
        widget = [[QWidget(), QWidget()]]
        name = ["QTableWidget", "QTextEdit"]
        var = [{"headerLabels": [["mass", "electricity", "X-coordinate", "Y-coordinate", "Z-coordinate",
                                  "X-velocity", "Y-velocity", "Z-velocity"]],
                "data": [numpy.array([[1, 0, 1, 0, 0, 0, 1, 0],
                                      [1, 1, 0, 1, 0, 0, 0, 1],
                                      [1, -1, 0, 0, 1, 1, 0, 0]])]},
               {"text": [["yes", "no"]]}]
        for j in range(0, 2):
            widgetLayout = QGridLayout()
            position = [[0, 0, 1, 1]]
            self.controlLayout(layout=widgetLayout, name=name[j], var=var[j], position=position, signal=None)
            widget[0][j].setLayout(widgetLayout)
        text = [["Initial Condition", "Note"]]
        position = [[4, 0, 1, 7]]
        self.controlLayout(layout=layout, name="QTabWidget", var={"text": text, "widget": widget},
                           position=position, signal=None)

        # noinspection PyArgumentList
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        ###############################################################################
        # initialization self.controlData["gravitationalSystemImage"] then refresh it #
        # refresh self.control["gravitationalSystemImage"]                            #
        ###############################################################################
        if "gravitationalSystemImage" not in self.controlData:
            self.addFrame("gravitationalSystemImage")
            self.gravitationalSystemImageSignal()
        else:
            for j in range(0, len(self.control["QComboBox"])):
                self.control["QComboBox"][j].currentIndexChanged.disconnect(self.gravitationalSystemImageSignal)
            for j in range(0, len(self.control["QSpinBox"])):
                self.control["QSpinBox"][j].valueChanged.disconnect(self.gravitationalSystemImageSignal)
            for j in range(0, len(self.control["QRadioButton"])):
                self.control["QRadioButton"][j].clicked.disconnect(self.gravitationalSystemImageSignal)
            self.imageRead(imageName="gravitationalSystemImage")
            for j in range(0, len(self.control["QComboBox"])):
                self.control["QComboBox"][j].currentIndexChanged.connect(self.gravitationalSystemImageSignal)
            for j in range(0, len(self.control["QSpinBox"])):
                self.control["QSpinBox"][j].valueChanged.connect(self.gravitationalSystemImageSignal)
            for j in range(0, len(self.control["QRadioButton"])):
                self.control["QRadioButton"][j].clicked.connect(self.gravitationalSystemImageSignal)

        self.statusBar().showMessage('Ready')

    def gravitationalSystemImageSignal(self):
        """
        respond of current page(gravitationalSystemImage), then write data into MainData.dataClasses
        """
        self.statusBar().showMessage('Saving Page data...')

        ###############################################################
        # initialization self.controlData["gravitationalSystemImage"] #
        ###############################################################
        imageName = "gravitationalSystemImage"
        self.controlDataClear(imageName)

        ########################################################
        # refresh self.controlData["gravitationalSystemImage"] #
        ########################################################
        for j in range(0, len(self.control["QComboBox"])):
            itemText = list()
            for k in range(0, self.control["QComboBox"][j].count()):
                itemText.append(self.control["QComboBox"][j].itemText(k))
            self.controlData[imageName]["QComboBox"]["itemText"].append(itemText)

            currentIndex = self.control["QComboBox"][j].currentIndex()
            self.controlData[imageName]["QComboBox"]["currentIndex"].append(currentIndex)

        for i in range(0, len(self.control["QTableWidget"])):
            currentRow = self.control["QTableWidget"][i].rowCount()
            row = int(self.control["QComboBox"][5].currentText())
            column = self.control["QTableWidget"][i].columnCount()
            data = numpy.zeros((row, column), dtype=numpy.float64)
            for j in range(0, row):
                for k in range(0, column):
                    if j < currentRow:
                        # noinspection PyBroadException
                        try:
                            data[j][k] = float(self.control["QTableWidget"][i].item(j, k).text())
                        except:
                            data[j][k] = 0
            self.controlData[imageName]["QTableWidget"]["data"].append(data)

        for j in range(0, len(self.control["QSpinBox"])):
            value = self.control["QSpinBox"][j].value()
            self.controlData[imageName]["QSpinBox"]["value"].append(value)

        for j in range(0, len(self.control["QRadioButton"])):
            isChecked = self.control["QRadioButton"][j].isChecked()
            self.controlData[imageName]["QRadioButton"]["isChecked"].append(isChecked)

        ####################################################
        # refresh self.control["gravitationalSystemImage"] #
        ####################################################
        for j in range(0, len(self.control["QComboBox"])):
            self.control["QComboBox"][j].currentIndexChanged.disconnect(self.gravitationalSystemImageSignal)
        for j in range(0, len(self.control["QSpinBox"])):
            self.control["QSpinBox"][j].valueChanged.disconnect(self.gravitationalSystemImageSignal)
        for j in range(0, len(self.control["QRadioButton"])):
            self.control["QRadioButton"][j].clicked.disconnect(self.gravitationalSystemImageSignal)
        self.imageRead(imageName="gravitationalSystemImage")
        for j in range(0, len(self.control["QComboBox"])):
            self.control["QComboBox"][j].currentIndexChanged.connect(self.gravitationalSystemImageSignal)
        for j in range(0, len(self.control["QSpinBox"])):
            self.control["QSpinBox"][j].valueChanged.connect(self.gravitationalSystemImageSignal)
        for j in range(0, len(self.control["QRadioButton"])):
            self.control["QRadioButton"][j].clicked.connect(self.gravitationalSystemImageSignal)

        self.statusBar().showMessage('Page data Saved.')

    def gravitationalSystemImageDraw(self):
        """
        Draw animation of solution of ordinary differential equations
        """
        ########################################################
        # refresh self.controlData["gravitationalSystemImage"] #
        ########################################################
        self.gravitationalSystemImageSignal()
        self.statusBar().showMessage('Start to solving the ordinary differential equations...')

        #####################################################
        # get parameters of ordinary differential equations #
        #####################################################
        imageName = "gravitationalSystemImage"
        aniArg = self.controlData[imageName]["QComboBox"]["currentIndex"][8:]

        data = self.controlData[imageName]["QTableWidget"]["data"][0]
        mass = data[:, 0]
        for j in range(0, len(mass)):
            if mass[j] < 0 or mass[j] == 0:
                self.statusBar().showMessage('mass[%d] must be positive.' % j)
                return

        electric = numpy.abs(data[:, 1])

        electricType = numpy.sign(data[:, 1])

        cood = data[:, 2:5]
        coodCheck = numpy.dot(cood, cood.T)
        for j in range(0, len(mass)):
            for k in range(j, len(mass)):
                if (coodCheck[j, j] + coodCheck[k, k]) == 2 * coodCheck[j, k] and j != k:
                    self.statusBar().showMessage('point[%d] and point[%d] share the same coordinate.' % (j, k))
                    return

        vel = data[:, 5:]

        if self.controlData[imageName]["QRadioButton"]["isChecked"][0]:
            GUnit = 1
            KUnit = 1
        else:
            lenUnitMap = {0: 9.46 * 10 ** 15, 1: 1000, 2: 1, 3: 0.001, 4: 10 ** (-9)}
            lenUnit = lenUnitMap[self.controlData[imageName]["QComboBox"]["currentIndex"][0]]

            timeUnitMap = {0: 3.1536 * 10 ** 7, 1: 86400, 2: 1, 3: 0.001, 4: 10 ** (-6)}
            timeUnit = timeUnitMap[self.controlData[imageName]["QComboBox"]["currentIndex"][1]]

            massUnitMap = {0: 1, 1: 1.99 * 10 ** 30, 2: 1.7 * 10 ** (-27), 3: 9.1 * 10 ** (-31)}
            massUnit = massUnitMap[self.controlData[imageName]["QComboBox"]["currentIndex"][2]]

            electricUnitMap = {0: 1, 1: 1.6 * 10 ** (-19)}
            electricUnit = electricUnitMap[self.controlData[imageName]["QComboBox"]["currentIndex"][3]]

            GUnit = 6.67408 * 10 ** (-11) * massUnit * timeUnit ** 2 / lenUnit ** 3
            KUnit = 8.987 * 10 ** 9 * electricUnit ** 2 * timeUnit ** 2 / lenUnit ** 3 / massUnit

        timeLength = int(self.control["QComboBox"][6].currentText())
        nodeNumber = int(self.control["QComboBox"][7].currentText())
        t = numpy.arange(0, timeLength, timeLength / nodeNumber)

        aniSpeed = self.controlData[imageName]["QSpinBox"]["value"][0]

        ########################################################
        # draw the solution of ordinary differential equations #
        ########################################################
        self.controlClear()

        layout = QGridLayout()
        layout.setSpacing(10)

        # noinspection PyArgumentList
        widget = QWidget()
        self.canvas["gravitationalSystemImage"] = GravitationCanvas(aniArg, mass, electric, electricType, cood, vel,
                                                                    GUnit, KUnit, t, aniSpeed, parent=widget)
        self.controlData[imageName]["save"] = [mass, electric, electricType, cood, vel, GUnit, KUnit, t,
                                               self.canvas["gravitationalSystemImage"].track,
                                               self.canvas["gravitationalSystemImage"].vector,
                                               self.canvas["gravitationalSystemImage"].acc]

        layout.addWidget(self.canvas["gravitationalSystemImage"])
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.statusBar().showMessage('Ready')

    def convexHullImage(self):
        """
        layout and initialization data
        """
        ##########################
        # layout of current page #
        ##########################
        self.currentImage = "convexHullImage"
        self.controlClear()

        layout = QGridLayout()
        layout.setSpacing(10)

        text = ['空间维数', '散点个数', '查看迭代步数']
        position = [[0, 0, 1, 1], [0, 2, 1, 1], [0, 4, 1, 1]]
        self.controlLayout(layout=layout, name="QLabel", var={"text": text}, position=position, signal=None)

        itemText = [list(map(str, range(2, 15))), list(map(str, range(3, 50))),
                    ["-complete-"] + list(map(str, range(1, 9)))]
        currentIndex = [1, 6, 0]
        position = [[0, 1, 1, 1], [0, 3, 1, 1], [0, 5, 1, 1]]
        self.controlLayout(layout=layout, name="QComboBox", var={"itemText": itemText, "currentIndex": currentIndex},
                           position=position, signal=self.convexHullImageSignal)

        text = ['随机生成散点集']
        position = [[0, 6, 1, 1]]
        self.controlLayout(layout=layout, name="QPushButton", var={"text": text},
                           position=position, signal=self.convexHullImageRandom)

        # noinspection PyArgumentList
        widget = [[QWidget(), QWidget(), QWidget()]]
        matrixLayout = QGridLayout()
        matrix = [numpy.array([[6, 0, 9, 9, 6, 6, 2, 0, 6],
                               [5, 7, 2, 6, 7, 3, 7, 4, 4],
                               [8, 3, 2, 5, 0, 0, 7, 6, 5]])]
        self.controlLayout(layout=matrixLayout, name="QTableWidget", var={"headerLabels": [], "data": matrix},
                           position=[[0, 0, 1, 1]], signal=None)
        widget[0][0].setLayout(matrixLayout)

        patches_listLayout = QGridLayout()
        patches_list = [numpy.array([[4, 2, 6, 0, 1, 1, 0, 0, 2, 5, 5, 5],
                                     [6, 4, 0, 6, 6, 7, 2, 7, 5, 2, 1, 7],
                                     [3, 3, 3, 7, 4, 6, 3, 2, 4, 7, 4, 1]])]
        self.controlLayout(layout=patches_listLayout, name="QTableWidget",
                           var={"headerLabels": [], "data": patches_list}, position=[[0, 0, 1, 1]], signal=None)
        widget[0][1].setLayout(patches_listLayout)

        canvasLayout = QGridLayout()
        self.canvas["convexHullImage"] = ConvexHullCanvas(matrix[0], patches_list, parent=widget[0][2])
        canvasLayout.addWidget(self.canvas["convexHullImage"])
        widget[0][2].setLayout(canvasLayout)

        text = [["Points", "Patches", "Convex Hull 3D"]]
        position = [[1, 0, 1, 7]]
        self.controlLayout(layout=layout, name="QTabWidget", var={"text": text, "widget": widget},
                           position=position, signal=None)

        # noinspection PyArgumentList
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        ######################################################################
        # initialization self.controlData["convexHullImage"] then refresh it #
        # refresh self.control["convexHullImage"]                            #
        ######################################################################
        if "convexHullImage" not in self.controlData:
            self.addFrame("convexHullImage")
            self.convexHullImageSignal()
        else:
            for j in range(0, len(self.control["QComboBox"])):
                self.control["QComboBox"][j].currentIndexChanged.disconnect(self.convexHullImageSignal)
            self.imageRead(imageName="convexHullImage")
            for j in range(0, len(self.control["QComboBox"])):
                self.control["QComboBox"][j].currentIndexChanged.connect(self.convexHullImageSignal)

        self.statusBar().showMessage('Ready')

    def convexHullImageSignal(self):
        """
        respond of current page(convexHullImage), then write data into MainData.controlData
        """
        self.statusBar().showMessage('Setting patches...')

        ######################################################
        # initialization self.controlData["convexHullImage"] #
        ######################################################
        imageName = "convexHullImage"
        self.controlDataClear(imageName)

        ###############################################
        # refresh self.controlData["convexHullImage"] #
        ###############################################
        m = int(self.control["QComboBox"][0].itemText(self.control["QComboBox"][0].currentIndex()))
        n = int(self.control["QComboBox"][1].itemText(self.control["QComboBox"][1].currentIndex()))
        if m < n:
            pass
        else:
            self.statusBar().showMessage('The number of points should be more than dimension.')
            return

        list(map(str, range(4, 50)))
        for j in range(0, len(self.control["QComboBox"])):
            itemText = list()
            for k in range(0, self.control["QComboBox"][j].count()):
                itemText.append(self.control["QComboBox"][j].itemText(k))
            self.controlData[imageName]["QComboBox"]["itemText"].append(itemText)

            currentIndex = self.control["QComboBox"][j].currentIndex()
            self.controlData[imageName]["QComboBox"]["currentIndex"].append(currentIndex)

        row = int(self.control["QComboBox"][0].currentText())
        column = int(self.control["QComboBox"][1].currentText())
        currentRow = self.control["QTableWidget"][0].rowCount()
        currentColumn = self.control["QTableWidget"][0].columnCount()
        matrix = numpy.zeros((row, column), dtype=numpy.float64)
        for j in range(0, row):
            for k in range(0, column):
                if j < currentRow and k < currentColumn:
                    # noinspection PyBroadException
                    try:
                        matrix[j][k] = float(self.control["QTableWidget"][0].item(j, k).text())
                    except:
                        matrix[j][k] = 0
        self.controlData[imageName]["QTableWidget"]["data"].append(matrix)

        obj = ConvexHullMap(matrix=matrix)
        obj.complete()
        patches = numpy.array(obj.patches).T
        self.controlData[imageName]["QTableWidget"]["data"].append(patches)

        self.controlData[imageName]["save"] = [matrix, patches]

        ##############
        # draw image #
        ##############
        if int(self.control["QComboBox"][0].currentText()) == 3:
            self.canvas[imageName].canvasData["matrix"] = matrix
            if self.control["QComboBox"][2].currentIndex() == 0:
                self.canvas[imageName].canvasData["patches_list"] = [obj.patches]
            else:
                new_obj = ConvexHullMap(matrix=matrix)
                self.canvas[imageName].canvasData["patches_list"] = [copy.deepcopy(new_obj.patches)]
                for j in range(0, int(self.control["QComboBox"][2].currentText())):
                    new_obj.classify_points()
                    if new_obj.next_points.count(None) == len(new_obj.next_points):
                        break
                    new_obj.expand_patches()
                    self.canvas[imageName].canvasData["patches_list"].append(copy.deepcopy(new_obj.patches))
        self.canvas[imageName].fig.clf()
        self.canvas[imageName].axes = axes3d.Axes3D(self.canvas[imageName].fig)
        self.canvas[imageName].complete_draw()
        self.canvas[imageName].fig.canvas.draw()

        ###########################################
        # refresh self.control["convexHullImage"] #
        ###########################################
        for j in range(0, len(self.control["QComboBox"])):
            self.control["QComboBox"][j].currentIndexChanged.disconnect(self.convexHullImageSignal)
        self.imageRead(imageName=imageName)
        for j in range(0, len(self.control["QComboBox"])):
            self.control["QComboBox"][j].currentIndexChanged.connect(self.convexHullImageSignal)

        self.statusBar().showMessage('End of setting title.')

    def convexHullImageRandom(self):
        """
        Reset coordinates of scattered point set
        """
        ###############################################
        # refresh self.controlData["convexHullImage"] #
        ###############################################
        self.statusBar().showMessage('Start to resetting coordinates of scattered points...')

        #########################################
        # get parameters of scattered point set #
        #########################################
        imageName = "convexHullImage"

        n = int(self.control["QComboBox"][0].currentText())
        m = int(self.control["QComboBox"][1].currentText())
        matrix = numpy.random.random_integers(low=0, high=10, size=(n, m))
        self.controlData[imageName]["QTableWidget"]["data"][0] = matrix
        self.controlData[imageName]["save"][0] = matrix

        self.imageRead(imageName=imageName)

        self.convexHullImageSignal()

        self.statusBar().showMessage('End of resetting coordinates of scattered points.')

    def analyticFunctionImage(self):
        """
        layout and initialization data
        """
        ##########################
        # layout of current page #
        ##########################
        self.currentImage = "analyticFunctionImage"
        self.controlClear()

        layout = QGridLayout()
        layout.setSpacing(10)

        text = ['次方数', '拉伸系数', '辐角']
        position = [[0, 0, 1, 1], [0, 2, 1, 1], [0, 4, 1, 1]]
        self.controlLayout(layout=layout, name="QLabel", var={"text": text}, position=position, signal=None)

        itemText = [list(map(str, range(1, 20)))]
        position = [[0, 1, 1, 1]]
        self.controlLayout(layout=layout, name="QComboBox", var={"itemText": itemText, "currentIndex": []},
                           position=position, signal=self.analyticFunctionImageSignal)

        var = {"range": [[1, 100], [-180, 180]], "singleStep": [1, 1],
               "prefix": [], "suffix": ['*0.1', '*pi/180'], "value": [10, 0]}
        position = [[0, 3, 1, 1], [0, 5, 1, 1]]
        self.controlLayout(layout=layout, name="QSpinBox", var=var,
                           position=position, signal=self.analyticFunctionImageSignal)

        text = [['%f*e**(i*%f)*z**%d + z = 1' % (1, 1, 0)]]
        # noinspection PyArgumentList
        widget = [[QWidget()]]
        position = [[1, 0, 1, 6]]
        widgetLayout = QGridLayout()
        self.canvas["analyticFunctionImage"] = AnalyticFunctionCanvas(1, 1, 0, parent=widget[0][0])
        widgetLayout.addWidget(self.canvas["analyticFunctionImage"])
        widget[0][0].setLayout(widgetLayout)
        self.controlLayout(layout=layout, name="QTabWidget", var={"text": text, "widget": widget},
                           position=position, signal=None)

        # noinspection PyArgumentList
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        ############################################################################
        # initialization self.controlData["analyticFunctionImage"] then refresh it #
        # refresh self.control["analyticFunctionImage"]                            #
        ############################################################################
        if "analyticFunctionImage" not in self.controlData:
            self.addFrame("analyticFunctionImage")
            self.analyticFunctionImageSignal()
        else:
            for j in range(0, len(self.control["QComboBox"])):
                self.control["QComboBox"][j].currentIndexChanged.disconnect(self.analyticFunctionImageSignal)
            for j in range(0, len(self.control["QSpinBox"])):
                self.control["QSpinBox"][j].valueChanged.disconnect(self.analyticFunctionImageSignal)
            self.imageRead(imageName="analyticFunctionImage")
            for j in range(0, len(self.control["QComboBox"])):
                self.control["QComboBox"][j].currentIndexChanged.connect(self.analyticFunctionImageSignal)
            for j in range(0, len(self.control["QSpinBox"])):
                self.control["QSpinBox"][j].valueChanged.disconnect(self.analyticFunctionImageSignal)

        self.statusBar().showMessage('Ready')

    def analyticFunctionImageSignal(self):
        """
        respond of current page(analyticFunctionImage), then write data into MainData.controlData
        """
        self.statusBar().showMessage('Starting draw image...')

        ############################################################
        # initialization self.controlData["analyticFunctionImage"] #
        ############################################################
        imageName = "analyticFunctionImage"
        self.controlDataClear(imageName)

        #####################################################
        # refresh self.controlData["analyticFunctionImage"] #
        #####################################################
        for j in range(0, len(self.control["QComboBox"])):
            itemText = list()
            for k in range(0, self.control["QComboBox"][j].count()):
                itemText.append(self.control["QComboBox"][j].itemText(k))
            self.controlData[imageName]["QComboBox"]["itemText"].append(itemText)

            currentIndex = self.control["QComboBox"][j].currentIndex()
            self.controlData[imageName]["QComboBox"]["currentIndex"].append(currentIndex)

        for j in range(0, len(self.control["QSpinBox"])):
            value = self.control["QSpinBox"][j].value()
            self.controlData[imageName]["QSpinBox"]["value"].append(value)

        ##############
        # draw image #
        ##############
        self.canvas[imageName].n = self.controlData[imageName]["QComboBox"]["currentIndex"][0] + 1
        self.canvas[imageName].r = self.controlData[imageName]["QSpinBox"]["value"][0] * 0.1
        self.canvas[imageName].t = self.controlData[imageName]["QSpinBox"]["value"][1] * math.pi / 180
        text = '%f*e**(i*%f)*z**%d + z = 1' % (self.canvas[imageName].n, self.canvas[imageName].r,
                                               self.canvas[imageName].t)
        self.control["QTabWidget"][0].setTabText(0, text)
        self.canvas[imageName].fig.clf()
        self.canvas[imageName].axes = self.canvas[imageName].fig.add_subplot(111)
        self.canvas[imageName].axes.grid(True)
        self.canvas[imageName].complete_draw()
        self.canvas[imageName].fig.canvas.draw()

        ################################################
        # refresh self.control["analyticFunctionImage"] #
        ################################################
        for j in range(0, len(self.control["QComboBox"])):
            self.control["QComboBox"][j].currentIndexChanged.disconnect(self.analyticFunctionImageSignal)
        self.imageRead(imageName=imageName)
        for j in range(0, len(self.control["QComboBox"])):
            self.control["QComboBox"][j].currentIndexChanged.connect(self.analyticFunctionImageSignal)

        self.statusBar().showMessage('Image is drawn.')

    @staticmethod
    def sourceCodeImage():
        """
        @
        """
        pass

    def keyPressEvent(self, event):
        """
        :param event:
        :return:
        """
        if event.key() == Qt.Key_Escape:
            try:
                if self.currentImage == "rainImage":
                    self.orthogonalTableImage()
                elif self.currentImage == "orthogonalTableImage":
                    pass
                elif self.currentImage == "convexHullImage":
                    pass
                elif self.currentImage == "gravitationalSystemImage":
                    self.gravitationalSystemImage()
                elif self.currentImage == "analyticFunctionImage":
                    pass
            except KeyError:
                self.startImage()
            self.statusBar().showMessage('Esc is pressed!')

    def showOpenDialog(self):
        """
        @
        """
        # noinspection PyCallByClass,SpellCheckingInspection
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        # if fname[0]:
        #     # noinspection PyArgumentEqualDefault
        #     f = open(fname[0], 'r')
        #     with f:
        #         data = f.read()
        #         self.textEdit.setText(data)

    def buttonClicked(self):
        """
        @
        """
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        # noinspection PyCallByClass,PyTypeChecker
        QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

    def closeEvent(self, event):
        """
        @
        """
        # noinspection PyCallByClass,PyTypeChecker
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
