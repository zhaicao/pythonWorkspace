#!/usr/bin/python


class MainData:
    """
    frame of page data about PyQt5
    """

    def __init__(self):
        self.action = dict()
        self.canvas = dict()
        self.control = {"QLabel": [], "QTabWidget": [], "QPushButton": [], "QTextEdit": [],
                        "QRadioButton": [], "QComboBox": [], "QSpinBox": [], "QTableWidget": [], "QLCDNumber": []}
        self.controlData = dict()

    def controlClear(self):
        """
        remove all the controls except menuBar before open a new page
        """
        self.control = {"QLabel": [], "QTabWidget": [], "QPushButton": [], "QTextEdit": [],
                        "QRadioButton": [], "QComboBox": [], "QSpinBox": [], "QTableWidget": [], "QLCDNumber": []}

    def addFrame(self, imageName):
        """
        add a empty dictionary to record page data
        """
        self.controlData[imageName] = dict()
        self.controlData[imageName]["QRadioButton"] = {"isChecked": []}
        self.controlData[imageName]["QComboBox"] = {"itemText": [], "currentIndex": []}
        self.controlData[imageName]["QSpinBox"] = {"value": []}
        self.controlData[imageName]["QTableWidget"] = {"data": []}
        self.controlData[imageName]["QLCDNumber"] = {"value": []}
        self.controlData[imageName]["save"] = []

    def controlDataClear(self, imageName):
        """
        remove data  before refresh current page
        """
        self.controlData[imageName]["QRadioButton"]["isChecked"] = []
        self.controlData[imageName]["QComboBox"]["itemText"] = []
        self.controlData[imageName]["QComboBox"]["currentIndex"] = []
        self.controlData[imageName]["QSpinBox"]["value"] = []
        self.controlData[imageName]["QTableWidget"]["data"] = []
        self.controlData[imageName]["QLCDNumber"]["value"] = []
        self.controlData[imageName]["save"] = []