# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uis\question_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(301, 41))
        self.label_3.setMaximumSize(QtCore.QSize(301, 41))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 214, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(56, 17))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(56, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(56, 17))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(150, 0))
        self.widget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_7.setMaximumSize(QtCore.QSize(31, 21))
        self.pushButton_7.setStyleSheet("background-color: rgb(125, 255, 155);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_6.setMaximumSize(QtCore.QSize(31, 21))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_5.setMaximumSize(QtCore.QSize(31, 21))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_8.setMaximumSize(QtCore.QSize(31, 21))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_13.setMaximumSize(QtCore.QSize(31, 21))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_6.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget)
        self.pushButton_14.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_14.setMaximumSize(QtCore.QSize(31, 21))
        self.pushButton_14.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_6.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget)
        self.pushButton_15.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_15.setMaximumSize(QtCore.QSize(31, 21))
        self.pushButton_15.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_6.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget)
        self.pushButton_16.setMinimumSize(QtCore.QSize(31, 21))
        self.pushButton_16.setMaximumSize(QtCore.QSize(31, 21))
        self.pushButton_16.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_6.addWidget(self.pushButton_16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(138, 31))
        self.pushButton_4.setMaximumSize(QtCore.QSize(138, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout_8.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def set_question(self,id,question,options):
        self.label_2.setText(f"{id} .")
        self.label_3.setText(question)
        self.question = question
        self.options = options
        # self.options_id = option_id

        self.radioButton.setText(options[0])
        self.radioButton_2.setText(options[1])
        self.radioButton_3.setText(options[2])
        self.radioButton_4.setText(options[3])
    
    def reset_window(self):
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Test Name"))
        self.label_4.setText(_translate("MainWindow", "Time Left : 30.00"))
        self.label_2.setText(_translate("MainWindow", "1 ."))
        self.label_3.setText(_translate("MainWindow", "Question text goes here .. "))
        self.radioButton.setText(_translate("MainWindow", "Option 1"))
        self.radioButton_2.setText(_translate("MainWindow", "Option 2"))
        self.radioButton_3.setText(_translate("MainWindow", "Option 3"))
        self.radioButton_4.setText(_translate("MainWindow", "Option 4"))
        self.pushButton.setText(_translate("MainWindow", "Previous"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.pushButton_3.setText(_translate("MainWindow", "Save & Next"))
        self.pushButton_7.setText(_translate("MainWindow", "1"))
        self.pushButton_6.setText(_translate("MainWindow", "1"))
        self.pushButton_5.setText(_translate("MainWindow", "1"))
        self.pushButton_8.setText(_translate("MainWindow", "1"))
        self.pushButton_13.setText(_translate("MainWindow", "1"))
        self.pushButton_14.setText(_translate("MainWindow", "1"))
        self.pushButton_15.setText(_translate("MainWindow", "1"))
        self.pushButton_16.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "Submit"))

class Question_attempting_window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_answer = None
        self.setupUi(self)
        self.radioButton.clicked.connect(self.radiobutton_clicked)
        self.radioButton_2.clicked.connect(self.radiobutton2_clicked)
        self.radioButton_3.clicked.connect(self.radiobutton3_clicked)
        self.radioButton_4.clicked.connect(self.radiobutton4_clicked)
    
    def radiobutton_clicked(self):
        sender = self.sender()
        if sender.isChecked():
            self.selected_answer = 1
        print(self.selected_answer)
    
    def radiobutton2_clicked(self):
        sender = self.sender()
        if sender.isChecked():
            self.selected_answer = 2
        print(self.selected_answer)

    def radiobutton3_clicked(self):
        sender = self.sender()
        if sender.isChecked():
            self.selected_answer = 3

    def radiobutton4_clicked(self):
        sender = self.sender()
        if sender.isChecked():
            self.selected_answer = 4


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Question_attempting_window()
    ui.show()
    sys.exit(app.exec_())