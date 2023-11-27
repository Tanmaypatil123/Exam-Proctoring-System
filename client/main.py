import typing
from PyQt5 import QtCore,QtGui,QtWidgets
# from .helpful_scripts.resolution import scrn_res
from helpful_scripts.resolution import scrn_res
from PyQt5.QtWidgets import QWidget
from pages.candidate_login_page_for_exam import Candidate_login_Window
from pages.Candidate_System_check_and_block import SystemCheckWindow
from pages.instruction_page import INstructiionWindow
# from pages.question_atempting_screen_candidate_view import Question_attempting_window
# from pages.question import QuestionWindow
from pages.question_new import Question_attempting_window
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pages.question_window import QuestionWindow

def load_questions():
    questions = {
        1 : {
            "question" : "what is your name ?",
            "options" : [
                "h","k","l",'j'
            ]
        },
        2 : {
            "question" : "what is your name ? second",
            "options" : [
                "h","k","l",'f'
            ]
        }
    }

    return questions

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # (self.width, self.height) = scrn_res()
        (self.width, self.height) = (1280,600)
        # following staked widgetstores pages or gui class related to software
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.setFixedSize(self.width,self.height)
        self.question_data = load_questions()
        self.current_question = 1
        self.setCentralWidget(self.stacked_widget)
        self.setGeometry(0,0,self.width,self.height)
        self.cols = 4
        self.buttons = []

        ### pages object are as follows

        ## Candidate login page index - 0
        self.candidate_login_window = Candidate_login_Window() 
        self.stacked_widget.addWidget(self.candidate_login_window)
        # self.candidate_login_window.pushButton.clicked.connect(self.go_to_instruction_page)
        # self.candidate_login_window.pushButton.clicked.connect(self.go_to_question_attempting_page)

        ## System check page - 1
        self.systemcheck_window = SystemCheckWindow()
        self.stacked_widget.addWidget(self.systemcheck_window)

        ## Instruction page - 2
        self.instruction_window = INstructiionWindow()
        self.stacked_widget.addWidget(self.instruction_window)


        ## Questions window  - 3
        self.question_window = QuestionWindow()
        self.stacked_widget.addWidget(self.question_window)

        ## Question attempting window - 4
        self.attempting_window = Question_attempting_window()
        self.stacked_widget.addWidget(self.attempting_window)


        self.attempting_window.set_question(
            1,"hey" , ["h",'j','k','l']
        )
        self.connect_submit_button()

        ## go to first page
        self.go_to_candidate_login_page()


        ## event handling 
        self.candidate_login_window.pushButton.clicked.connect(self.get_email_password)
        self.instruction_window.pushButton.clicked.connect(self.go_to_question_window)

    def go_to_question_window(self):
        self.load_questions_ui(10)
        self.stacked_widget.setCurrentIndex(3)
    def go_to_instruction_page(self):
        self.stacked_widget.setCurrentIndex(2)
    
    def go_to_question_attempting_page(self):
        self.stacked_widget.setCurrentIndex(4)
    def connect_submit_button(self):
        self.attempting_window.pushButton_4.clicked.connect(self.load_next_question)
    
    def load_next_question(self):
        # Increment to load the next question
        self.current_question += 1
        if self.current_question in self.question_data:
            question_info = self.question_data[self.current_question]
            question = question_info["question"]
            options = question_info["options"]

            self.attempting_window.set_question(self.current_question, question, options)
        else:
            # No more questions, handle completion or action
            pass

    def go_to_candidate_login_page(self):
        self.stacked_widget.setCurrentIndex(0)
    
    def get_email_password(self):
        email = self.candidate_login_window.lineEdit.text()
        password = self.candidate_login_window.lineEdit_2.text()
        response = self.request_verify(email,password)
        self.go_to_instruction_page()
        print(response)

    def request_verify(self,email,password):
        response = requests.post("http://127.0.0.1:8000/api/student/verify/",data={
            "email" : email,
            "password" : password
        })
        if response.status_code == 200 :
            return True
        else : return False

    def load_questions_ui(self,no_of_questions):
        for question_number in range(1,no_of_questions + 1):
            row = (question_number - 1) // self.cols
            col = (question_number - 1) %  self.cols
            button = QPushButton(f"{question_number}")
            button.clicked.connect(lambda checked , q = question_number : self.load_question_backend(q))
            self.question_window.gridLayout.addWidget(button,row,col)
            self.buttons.append(button)

    def load_question_backend(self,q):
        print(q)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())     