# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uis\Insturction page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Instructionpage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Headline = QtWidgets.QTextEdit(self.centralwidget)
        self.Headline.setGeometry(QtCore.QRect(280, 0, 231, 41))
        self.Headline.setStyleSheet("background -color:rgb(0, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.Headline.setObjectName("Headline")
        self.insturctioninfo = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.insturctioninfo.setGeometry(QtCore.QRect(90, 90, 621, 281))
        self.insturctioninfo.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.insturctioninfo.setObjectName("insturctioninfo")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(110, 270, 121, 21))
        self.checkBox.setObjectName("checkBox")
        self.Proceed = QtWidgets.QPushButton(self.centralwidget)
        self.Proceed.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.Proceed.setObjectName("Proceed")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Headline.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Instructions</span></p></body></html>"))
        self.insturctioninfo.setPlainText(_translate("MainWindow", "                              Instructions\n"
" \n"
"1.Exam has Total 15 Question.\n"
"2.Total Exam timining is 30 Minutes\n"
"3.Camera should be on during test\n"
"4.Do not Close the window otherwise the test will be submitted automatically \n"
"\n"
"\n"
"\n"
"Best of Luck!"))
        self.checkBox.setText(_translate("MainWindow", "Agree  and continue"))
        self.Proceed.setText(_translate("MainWindow", "proceed"))

class InstructionWindow(QtWidgets.QDialog,Instructionpage):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)