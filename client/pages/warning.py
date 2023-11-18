import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class WarningWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(246, 72)
        Dialog.setMinimumSize(QtCore.QSize(246, 72))
        Dialog.setMaximumSize(QtCore.QSize(246, 72))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 50, 56, 17))
        self.pushButton.setMinimumSize(QtCore.QSize(56, 17))
        self.pushButton.setMaximumSize(QtCore.QSize(56, 17))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 101, 16))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label.wordWrap()
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 10, 51, 51))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/images/pngwing.com.png);")
        self.widget.setObjectName("widget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "Warning !"))

    def set_text(self,text):
        self.label.setText(f"Warning ! {text}")

import resources_rc

class Warning(QtWidgets.QDialog,WarningWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.set_text("hey some thing went wrong")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Warning()
    ui.show()
    sys.exit(app.exec_())
