# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.helloLabel = QtWidgets.QLabel(self.centralwidget)
        self.helloLabel.setGeometry(QtCore.QRect(260, 210, 71, 16))
        self.helloLabel.setObjectName("helloLabel")
        self.showLableButton = QtWidgets.QPushButton(self.centralwidget)
        self.showLableButton.setGeometry(QtCore.QRect(240, 240, 113, 32))
        self.showLableButton.setObjectName("showLableButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.helloLabel.setText(_translate("MainWindow", "Hello World"))
        self.showLableButton.setText(_translate("MainWindow", "Hidden"))
