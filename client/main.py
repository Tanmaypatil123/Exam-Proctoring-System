import typing
from PyQt5 import QtCore,QtGui,QtWidgets
# from .helpful_scripts.resolution import scrn_res
from helpful_scripts.resolution import scrn_res
from PyQt5.QtWidgets import QWidget
from pages.candidate_login_page_for_exam import Candidate_login_Window

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        (self.width, self.height) = scrn_res()
        # following staked widgetstores pages or gui class related to software
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.setFixedSize(self.width,self.height)

        self.setCentralWidget(self.stacked_widget)
        self.setGeometry(0,0,self.width,self.height)


        ### pages object are as follows

        ## Candidate login page index - 0
        self.candidate_login_window = Candidate_login_Window() 
        self.stacked_widget.addWidget(self.candidate_login_window)

        ## go to first page
        self.go_to_candidate_login_page()

    def go_to_candidate_login_page(self):
        self.stacked_widget.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())     