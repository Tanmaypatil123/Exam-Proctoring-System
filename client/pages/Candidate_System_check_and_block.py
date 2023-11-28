# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uis\Candidate_System_check_and_block.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class System_check_page(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.SystemCHeckPageLabel = QtWidgets.QLabel(self.frame_2)
        self.SystemCHeckPageLabel.setGeometry(QtCore.QRect(20, 20, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.SystemCHeckPageLabel.setFont(font)
        self.SystemCHeckPageLabel.setStyleSheet("/* Define a class for your label */\n"
".QLabel {\n"
"    font-family: Arial, sans-serif; /* Use a web-safe font or a custom Shopify font if available */\n"
"    font-size: 16px; /* Adjust the font size as needed */\n"
"    font-weight: bold; /* Make the text bold if desired */\n"
"    color: #333; /* Set the text color to a Shopify-like color */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    padding: 10px; /* Add some padding around the text */\n"
"    background-color: #f4f4f4; /* Set a background color */\n"
"    border: 1px solid #ccc; /* Add a border for a clean look */\n"
"    border-radius: 5px; /* Round the corners of the label */\n"
"}\n"
"")
        self.SystemCHeckPageLabel.setObjectName("SystemCHeckPageLabel")
        self.AntiVCheckLabel = QtWidgets.QLabel(self.frame_2)
        self.AntiVCheckLabel.setGeometry(QtCore.QRect(20, 100, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.AntiVCheckLabel.setFont(font)
        self.AntiVCheckLabel.setStyleSheet("/* Define a class for your label */\n"
".QLabel {\n"
"    font-family: Arial, sans-serif; /* Use a web-safe font or a custom Shopify font if available */\n"
"    font-size: 16px; /* Adjust the font size as needed */\n"
"    font-weight: bold; /* Make the text bold if desired */\n"
"    color: #333; /* Set the text color to a Shopify-like color */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    padding: 10px; /* Add some padding around the text */\n"
"    background-color: #f4f4f4; /* Set a background color */\n"
"    border: 1px solid #ccc; /* Add a border for a clean look */\n"
"    border-radius: 5px; /* Round the corners of the label */\n"
"}\n"
"")
        self.AntiVCheckLabel.setObjectName("AntiVCheckLabel")
        self.ASPB = QtWidgets.QProgressBar(self.frame_2)
        self.ASPB.setGeometry(QtCore.QRect(20, 150, 118, 23))
        self.ASPB.setProperty("value", 24)
        self.ASPB.setObjectName("ASPB")
        self.HWCheckLabel = QtWidgets.QLabel(self.frame_2)
        self.HWCheckLabel.setGeometry(QtCore.QRect(400, 100, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.HWCheckLabel.setFont(font)
        self.HWCheckLabel.setStyleSheet("/* Define a class for your label */\n"
".QLabel {\n"
"    font-family: Arial, sans-serif; /* Use a web-safe font or a custom Shopify font if available */\n"
"    font-size: 16px; /* Adjust the font size as needed */\n"
"    font-weight: bold; /* Make the text bold if desired */\n"
"    color: #333; /* Set the text color to a Shopify-like color */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    padding: 10px; /* Add some padding around the text */\n"
"    background-color: #f4f4f4; /* Set a background color */\n"
"    border: 1px solid #ccc; /* Add a border for a clean look */\n"
"    border-radius: 5px; /* Round the corners of the label */\n"
"}\n"
"")
        self.HWCheckLabel.setObjectName("HWCheckLabel")
        self.CHPB = QtWidgets.QProgressBar(self.frame_2)
        self.CHPB.setGeometry(QtCore.QRect(400, 150, 118, 23))
        self.CHPB.setProperty("value", 24)
        self.CHPB.setObjectName("CHPB")
        self.NetworkConnLabel = QtWidgets.QLabel(self.frame_2)
        self.NetworkConnLabel.setGeometry(QtCore.QRect(20, 200, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.NetworkConnLabel.setFont(font)
        self.NetworkConnLabel.setStyleSheet("/* Define a class for your label */\n"
".QLabel {\n"
"    font-family: Arial, sans-serif; /* Use a web-safe font or a custom Shopify font if available */\n"
"    font-size: 16px; /* Adjust the font size as needed */\n"
"    font-weight: bold; /* Make the text bold if desired */\n"
"    color: #333; /* Set the text color to a Shopify-like color */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    padding: 10px; /* Add some padding around the text */\n"
"    background-color: #f4f4f4; /* Set a background color */\n"
"    border: 1px solid #ccc; /* Add a border for a clean look */\n"
"    border-radius: 5px; /* Round the corners of the label */\n"
"}\n"
"")
        self.NetworkConnLabel.setObjectName("NetworkConnLabel")
        self.NCPB = QtWidgets.QProgressBar(self.frame_2)
        self.NCPB.setGeometry(QtCore.QRect(20, 260, 118, 23))
        self.NCPB.setProperty("value", 24)
        self.NCPB.setObjectName("NCPB")
        self.OTPB = QtWidgets.QProgressBar(self.frame_2)
        self.OTPB.setGeometry(QtCore.QRect(400, 260, 118, 23))
        self.OTPB.setProperty("value", 24)
        self.OTPB.setObjectName("OTPB")
        self.ClosingTabsLabel = QtWidgets.QLabel(self.frame_2)
        self.ClosingTabsLabel.setGeometry(QtCore.QRect(400, 200, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.ClosingTabsLabel.setFont(font)
        self.ClosingTabsLabel.setStyleSheet("/* Define a class for your label */\n"
".QLabel {\n"
"    font-family: Arial, sans-serif; /* Use a web-safe font or a custom Shopify font if available */\n"
"    font-size: 16px; /* Adjust the font size as needed */\n"
"    font-weight: bold; /* Make the text bold if desired */\n"
"    color: #333; /* Set the text color to a Shopify-like color */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    padding: 10px; /* Add some padding around the text */\n"
"    background-color: #f4f4f4; /* Set a background color */\n"
"    border: 1px solid #ccc; /* Add a border for a clean look */\n"
"    border-radius: 5px; /* Round the corners of the label */\n"
"}\n"
"")
        self.ClosingTabsLabel.setObjectName("ClosingTabsLabel")
        self.SRPB = QtWidgets.QProgressBar(self.frame_2)
        self.SRPB.setGeometry(QtCore.QRect(20, 350, 118, 23))
        self.SRPB.setProperty("value", 24)
        self.SRPB.setObjectName("SRPB")
        self.BackProcessLabel = QtWidgets.QLabel(self.frame_2)
        self.BackProcessLabel.setGeometry(QtCore.QRect(20, 300, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.BackProcessLabel.setFont(font)
        self.BackProcessLabel.setStyleSheet("/* Define a class for your label */\n"
".QLabel {\n"
"    font-family: Arial, sans-serif; /* Use a web-safe font or a custom Shopify font if available */\n"
"    font-size: 16px; /* Adjust the font size as needed */\n"
"    font-weight: bold; /* Make the text bold if desired */\n"
"    color: #333; /* Set the text color to a Shopify-like color */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    padding: 10px; /* Add some padding around the text */\n"
"    background-color: #f4f4f4; /* Set a background color */\n"
"    border: 1px solid #ccc; /* Add a border for a clean look */\n"
"    border-radius: 5px; /* Round the corners of the label */\n"
"}\n"
"")
        self.BackProcessLabel.setObjectName("BackProcessLabel")
        self.BackgroundPB = QtWidgets.QProgressBar(self.frame_2)
        self.BackgroundPB.setGeometry(QtCore.QRect(410, 350, 118, 23))
        self.BackgroundPB.setProperty("value", 24)
        self.BackgroundPB.setObjectName("BackgroundPB")
        self.SysReqLabel = QtWidgets.QLabel(self.frame_2)
        self.SysReqLabel.setGeometry(QtCore.QRect(400, 300, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.SysReqLabel.setFont(font)
        self.SysReqLabel.setStyleSheet("/* Define a class for your label */\n"
".QLabel {\n"
"    font-family: Arial, sans-serif; /* Use a web-safe font or a custom Shopify font if available */\n"
"    font-size: 16px; /* Adjust the font size as needed */\n"
"    font-weight: bold; /* Make the text bold if desired */\n"
"    color: #333; /* Set the text color to a Shopify-like color */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    padding: 10px; /* Add some padding around the text */\n"
"    background-color: #f4f4f4; /* Set a background color */\n"
"    border: 1px solid #ccc; /* Add a border for a clean look */\n"
"    border-radius: 5px; /* Round the corners of the label */\n"
"}\n"
"")
        self.SysReqLabel.setObjectName("SysReqLabel")
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SystemCHeckPageLabel.setText(_translate("MainWindow", "Checking Your System Status..."))
        self.AntiVCheckLabel.setText(_translate("MainWindow", "Checking for Antivirus Software"))
        self.HWCheckLabel.setText(_translate("MainWindow", "Checking Hardware"))
        self.NetworkConnLabel.setText(_translate("MainWindow", "Checking Network Connectivity"))
        self.ClosingTabsLabel.setText(_translate("MainWindow", "Closing Other Tabs"))
        self.BackProcessLabel.setText(_translate("MainWindow", "Checking Background Processes"))
        self.SysReqLabel.setText(_translate("MainWindow", "Checking system requirements"))


class SystemCheckWindow(QtWidgets.QMainWindow,System_check_page):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = SystemCheckWindow()
    ui.show()
    sys.exit(app.exec_())