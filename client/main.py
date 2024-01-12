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
from dotenv import load_dotenv
from pages.code_questino import Code_window
from ultralytics import YOLO
import json
import shutil
import os
import cv2

load_dotenv()

class YOLODetectionWorker(QObject):
    phone_detection = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.model = YOLO("best.pt")
        self.model.fuse()

    def detect_objects(self, image_path):
        predictions = self.model(image_path, verbose=False, save_txt=True)
        txt_file_path = "runs/detect/predict/labels/captured_image.txt"
        file_exists = os.path.exists(txt_file_path)
        runs_path = "runs"

        if file_exists:
            print("Text file generated.")
            shutil.rmtree(runs_path)
            print("Folder 'runs' deleted.")
            self.phone_detection.emit(True)
        else:
            print("Text file not generated.")
            shutil.rmtree(runs_path)
            self.phone_detection.emit(False)
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
        self.examdetails = os.getenv("EXAM_DETAILS")
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.setFixedSize(self.width,self.height)
        self.question_data = load_questions()
        self.current_question = 1
        self.setCentralWidget(self.stacked_widget)
        self.setGeometry(0,0,self.width,self.height)
        self.cols = 4
        self.buttons = []
        self.questions  = []
        self.video_capture = cv2.VideoCapture(0)
        self.yolo_worker = YOLODetectionWorker()
        self.thread_yolo_detection = QThread(self)

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
        self.load_query()

        ## event handling 
        self.candidate_login_window.pushButton.clicked.connect(self.get_email_password)
        self.instruction_window.pushButton.clicked.connect(self.go_to_question_window)
        self.start_workers()

    def start_workers(self):
        # self.face_worker.moveToThread(self.thread_face_detection)
        self.yolo_worker.moveToThread(self.thread_yolo_detection)

        # self.face_worker.update_frame.connect(self.display_frame)
        # self.thread_face_detection.started.connect(self.perform_face_detection)
        self.thread_yolo_detection.started.connect(self.perform_yolo_detection)
        self.yolo_worker.phone_detection.connect(self.handle_yolo_detection)
        
        # self.thread_face_detection.start()
        self.thread_yolo_detection.start()

    def perform_yolo_detection(self):
        while True:
            ret, frame = self.video_capture.read()
            if ret:
                image_path = "captured_image.png"
                cv2.imwrite(image_path, frame)
                self.yolo_worker.detect_objects(image_path)
                cv2.waitKey(1)

    def handle_yolo_detection(self, result):
        # Handle YOLO detection result, e.g., show message or update UI based on phone detection
        print("YOLO Phone Detection Result:", result)
    def go_to_question_window(self):
        self.load_questions_ui()
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

    def load_questions_ui(self):
        no_of_questions = len(self.response["queations"])
        for question_number in range(1,no_of_questions + 1):
            row = (question_number - 1) // self.cols
            col = (question_number - 1) %  self.cols
            button = QPushButton(f"{question_number}")
            button.clicked.connect(lambda checked , q = question_number : self.load_question_backend(q))
            self.question_window.gridLayout.addWidget(button,row,col)
            self.buttons.append(button)
        button = QPushButton(f"{question_number + 1}")
        self.question_window.gridLayout.addWidget(button,row,col + 1)
        button.clicked.connect(self.go_to_code_window)
        # coding_window = Code_window()

    def go_to_code_window(self):
        coding_window = Code_window()
        self.stacked_widget.addWidget(coding_window)
        self.stacked_widget.setCurrentWidget(coding_window)

    def load_query(self):
        response = requests.get("http://127.0.0.1:8000/api/exam/get-exam-deails/",data={
            "exam_id" : self.examdetails
        })
        self.response = response.json()
        for i in self.response["queations"]:
            self.questions.append(self.response["queations"][i])
        
        print(response.json())
    def load_question_backend(self,q):
        print(self.examdetails)
        print(self.response)
        print(self.questions)
        
        attempting_window = Question_attempting_window()
        attempting_window.set_question(q,self.questions[q - 1]["title"],self.questions[q -1]["options"])
        self.stacked_widget.addWidget(attempting_window)
        self.stacked_widget.setCurrentWidget(attempting_window)
        print(q)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())     