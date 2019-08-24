# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\...\Desktop\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class View(object):
    """
    View Class of the MVC Pattern. Generated with PyQT5 Designer.
    View is highly scalable due to the use of multiple Layouts.
    """

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 425)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.routeText = QtWidgets.QPlainTextEdit(Form)
        self.routeText.setObjectName("routeText")
        self.gridLayout_2.addWidget(self.routeText, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.toText = QtWidgets.QLineEdit(Form)
        self.toText.setObjectName("toText")
        self.horizontalLayout_2.addWidget(self.toText)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fromText = QtWidgets.QLineEdit(Form)
        self.fromText.setObjectName("fromText")
        self.horizontalLayout.addWidget(self.fromText)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.submitButton = QtWidgets.QPushButton(Form)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_3.addWidget(self.submitButton)
        self.resetButton = QtWidgets.QPushButton(Form)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_3.addWidget(self.resetButton)
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)

        self.retranslateUi(Form)
        self.closeButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "To:     "))
        self.label.setText(_translate("Form", "From: "))
        self.submitButton.setText(_translate("Form", "submit"))
        self.resetButton.setText(_translate("Form", "reset"))
        self.closeButton.setText(_translate("Form", "close"))

