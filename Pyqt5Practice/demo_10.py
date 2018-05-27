import sys
from PyQt5.QtCore import (QDate, Qt)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
        QDialogButtonBox, QDoubleSpinBox, QGridLayout, QHBoxLayout,
        QLabel, QLineEdit, QSpinBox, QTabWidget, QVBoxLayout, QWidget)


class PaymentDlg(QDialog):

    def __init__(self, parent=None):
        super(PaymentDlg, self).__init__(parent)

        forenameLabel = QLabel("&Forename:")
        self.forenameLineEdit = QLineEdit()
        forenameLabel.setBuddy(self.forenameLineEdit)
        surnameLabel = QLabel("&Surname:")
        self.surnameLineEdit = QLineEdit()
        surnameLabel.setBuddy(self.surnameLineEdit)
        invoiceLabel = QLabel("&Invoice No.:")
        self.invoiceSpinBox = QSpinBox()
        invoiceLabel.setBuddy(self.invoiceSpinBox)
        self.invoiceSpinBox.setRange(1, 10000000)
        self.invoiceSpinBox.setValue(100000)
        self.invoiceSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        amountLabel = QLabel("&Amount:")
        self.amountSpinBox = QDoubleSpinBox()
        amountLabel.setBuddy(self.amountSpinBox)
        self.amountSpinBox.setRange(0, 5000.0)
        self.amountSpinBox.setPrefix("$ ")
        self.amountSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.paidCheckBox = QCheckBox("&Paid")
        checkNumLabel = QLabel("Check &No.:")
        self.checkNumLineEdit = QLineEdit()
        checkNumLabel.setBuddy(self.checkNumLineEdit)
        bankLabel = QLabel("&Bank:")
        self.bankLineEdit = QLineEdit()
        bankLabel.setBuddy(self.bankLineEdit)
        accountNumLabel = QLabel("Acco&unt No.:")
        self.accountNumLineEdit = QLineEdit()
        accountNumLabel.setBuddy(self.accountNumLineEdit)
        sortCodeLabel = QLabel("Sort &Code:")
        self.sortCodeLineEdit = QLineEdit()
        sortCodeLabel.setBuddy(self.sortCodeLineEdit)
        creditCardLabel = QLabel("&Number:")
        self.creditCardLineEdit = QLineEdit()
        creditCardLabel.setBuddy(self.creditCardLineEdit)
        validFromLabel = QLabel("&Valid From:")
        self.validFromDateEdit = QDateEdit()
        validFromLabel.setBuddy(self.validFromDateEdit)
        self.validFromDateEdit.setDisplayFormat("MMM yyyy")
        self.validFromDateEdit.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        expiryLabel = QLabel("E&xpiry Date:")
        self.expiryDateEdit = QDateEdit()
        expiryLabel.setBuddy(self.expiryDateEdit)
        self.expiryDateEdit.setDisplayFormat("MMM yyyy")
        self.expiryDateEdit.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                          QDialogButtonBox.Cancel)

        tabWidget = QTabWidget()
        cashWidget = QWidget()
        cashLayout = QHBoxLayout()
        cashLayout.addWidget(self.paidCheckBox)
        cashWidget.setLayout(cashLayout)
        tabWidget.addTab(cashWidget, "Cas&h")
        checkWidget = QWidget()
        checkLayout = QGridLayout()
        checkLayout.addWidget(checkNumLabel, 0, 0)
        checkLayout.addWidget(self.checkNumLineEdit, 0, 1)
        checkLayout.addWidget(bankLabel, 0, 2)
        checkLayout.addWidget(self.bankLineEdit, 0, 3)
        checkLayout.addWidget(accountNumLabel, 1, 0)
        checkLayout.addWidget(self.accountNumLineEdit, 1, 1)
        checkLayout.addWidget(sortCodeLabel, 1, 2)
        checkLayout.addWidget(self.sortCodeLineEdit, 1, 3)
        checkWidget.setLayout(checkLayout)
        tabWidget.addTab(checkWidget, "Chec&k")
        creditWidget = QWidget()
        creditLayout = QGridLayout()
        creditLayout.addWidget(creditCardLabel, 0, 0)
        creditLayout.addWidget(self.creditCardLineEdit, 0, 1, 1, 3)
        creditLayout.addWidget(validFromLabel, 1, 0)
        creditLayout.addWidget(self.validFromDateEdit, 1, 1)
        creditLayout.addWidget(expiryLabel, 1, 2)
        creditLayout.addWidget(self.expiryDateEdit, 1, 3)
        creditWidget.setLayout(creditLayout)
        tabWidget.addTab(creditWidget, "Credit Car&d")

        gridLayout = QGridLayout()
        gridLayout.addWidget(forenameLabel, 0, 0)
        gridLayout.addWidget(self.forenameLineEdit, 0, 1)
        gridLayout.addWidget(surnameLabel, 0, 2)
        gridLayout.addWidget(self.surnameLineEdit, 0, 3)
        gridLayout.addWidget(invoiceLabel, 1, 0)
        gridLayout.addWidget(self.invoiceSpinBox, 1, 1)
        gridLayout.addWidget(amountLabel, 1, 2)
        gridLayout.addWidget(self.amountSpinBox, 1, 3)
        layout = QVBoxLayout()
        layout.addLayout(gridLayout)
        layout.addWidget(tabWidget)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

        for lineEdit in (self.forenameLineEdit, self.surnameLineEdit,
                self.checkNumLineEdit, self.accountNumLineEdit,
                self.bankLineEdit, self.sortCodeLineEdit,
                self.creditCardLineEdit):
            lineEdit.textEdited.connect(self.updateUi)
        for dateEdit in (self.validFromDateEdit, self.expiryDateEdit):
            dateEdit.dateChanged.connect(self.updateUi)

        self.paidCheckBox.clicked.connect(self.updateUi)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.updateUi()
        self.setWindowTitle("Payment Form")


    def updateUi(self):
        today = QDate.currentDate()
        enable = (self.forenameLineEdit.text() and
                       self.surnameLineEdit.text())
        if enable:
            enable = (self.paidCheckBox.isChecked() or
                  (self.checkNumLineEdit.text() and
                        self.accountNumLineEdit.text() and
                        self.bankLineEdit.text() and
                        self.sortCodeLineEdit.text()) or
                  (self.creditCardLineEdit.text() and
                   self.validFromDateEdit.date() <= today and
                   self.expiryDateEdit.date() >= today))
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(bool(enable))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PaymentDlg()
    form.show()
    app.exec_()