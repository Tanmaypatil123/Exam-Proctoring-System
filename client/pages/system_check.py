# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uis\SYSTEM_CHECk_ED.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 561)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: #F0F0F4;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sYSTEM_LABEL = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sYSTEM_LABEL.setFont(font)
        self.sYSTEM_LABEL.setStyleSheet("QLabel { \n"
"color: #3baef0; \n"
"}")
        self.sYSTEM_LABEL.setObjectName("sYSTEM_LABEL")
        self.horizontalLayout.addWidget(self.sYSTEM_LABEL)
        self.verticalLayout.addWidget(self.frame)
        self.LAB1_F1 = QtWidgets.QFrame(self.centralwidget)
        self.LAB1_F1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LAB1_F1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LAB1_F1.setObjectName("LAB1_F1")
        self.F1_LAB1 = QtWidgets.QLabel(self.LAB1_F1)
        self.F1_LAB1.setGeometry(QtCore.QRect(40, 10, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F1_LAB1.setFont(font)
        self.F1_LAB1.setObjectName("F1_LAB1")
        self.verticalLayout.addWidget(self.LAB1_F1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.LAB2_F2 = QtWidgets.QFrame(self.centralwidget)
        self.LAB2_F2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LAB2_F2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LAB2_F2.setObjectName("LAB2_F2")
        self.F2_LAB2 = QtWidgets.QLabel(self.LAB2_F2)
        self.F2_LAB2.setGeometry(QtCore.QRect(40, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F2_LAB2.setFont(font)
        self.F2_LAB2.setObjectName("F2_LAB2")
        self.verticalLayout.addWidget(self.LAB2_F2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.LAB4_F4 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LAB4_F4.setFont(font)
        self.LAB4_F4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LAB4_F4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LAB4_F4.setObjectName("LAB4_F4")
        self.F4_LAB4 = QtWidgets.QLabel(self.LAB4_F4)
        self.F4_LAB4.setGeometry(QtCore.QRect(40, 10, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F4_LAB4.setFont(font)
        self.F4_LAB4.setObjectName("F4_LAB4")
        self.verticalLayout.addWidget(self.LAB4_F4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.LAB6_F6 = QtWidgets.QFrame(self.centralwidget)
        self.LAB6_F6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LAB6_F6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LAB6_F6.setObjectName("LAB6_F6")
        self.F6_LAB6 = QtWidgets.QLabel(self.LAB6_F6)
        self.F6_LAB6.setGeometry(QtCore.QRect(40, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F6_LAB6.setFont(font)
        self.F6_LAB6.setObjectName("F6_LAB6")
        self.verticalLayout.addWidget(self.LAB6_F6)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.LAB5_F5 = QtWidgets.QFrame(self.centralwidget)
        self.LAB5_F5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LAB5_F5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LAB5_F5.setObjectName("LAB5_F5")
        self.F5_LAB5 = QtWidgets.QLabel(self.LAB5_F5)
        self.F5_LAB5.setGeometry(QtCore.QRect(40, 10, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F5_LAB5.setFont(font)
        self.F5_LAB5.setObjectName("F5_LAB5")
        self.verticalLayout.addWidget(self.LAB5_F5)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.LAB3_F3 = QtWidgets.QFrame(self.centralwidget)
        self.LAB3_F3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LAB3_F3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LAB3_F3.setObjectName("LAB3_F3")
        self.F3_LAB3 = QtWidgets.QLabel(self.LAB3_F3)
        self.F3_LAB3.setGeometry(QtCore.QRect(40, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.F3_LAB3.setFont(font)
        self.F3_LAB3.setObjectName("F3_LAB3")
        self.verticalLayout.addWidget(self.LAB3_F3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sYSTEM_LABEL.setText(_translate("MainWindow", "System check is under process"))
        self.F1_LAB1.setText(_translate("MainWindow", "CHECKING OS"))
        self.F2_LAB2.setText(_translate("MainWindow", "SYSTEM VERSION "))
        self.F4_LAB4.setText(_translate("MainWindow", "CAMERA CHECK"))
        self.F6_LAB6.setText(_translate("MainWindow", "CHECKING MICROPHONE"))
        self.F5_LAB5.setText(_translate("MainWindow", "CHECKING INTERNET CONNECTIVITY"))
        self.F3_LAB3.setText(_translate("MainWindow", "RAM CHECK"))


class INstructiionWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.selected_answer = None
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = INstructiionWindow()
    ui.show()
    sys.exit(app.exec_())