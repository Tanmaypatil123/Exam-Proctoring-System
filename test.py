from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel

class QuestionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Create buttons for question numbers and arrange them in a grid
        num_questions = 10  # Assuming 10 questions
        cols = 4  # Number of columns
        self.buttons = []  # To store references to the buttons

        for question_number in range(1, num_questions + 1):
            row = (question_number - 1) // cols
            col = (question_number - 1) % cols
            button = QPushButton(f"Question {question_number}")
            button.clicked.connect(lambda checked, q=question_number: self.load_question(q))
            layout.addWidget(button, row, col)
            self.buttons.append(button)

        # Label to display the loaded question
        self.question_label = QLabel()
        layout.addWidget(self.question_label, num_questions // cols + 1, 0, 1, cols)

        self.setLayout(layout)

    def load_question(self, question_number):
        # Change color of clicked button to red and reset others to green
        for button in self.buttons:
            if button.text() == f"Question {question_number}":
                button.setStyleSheet("background-color: red;")
            else:
                button.setStyleSheet("background-color: green;")

        # Here, you can implement code to load the question based on the question number
        # For example, fetch the question from a database or predefined list
        questions = {
            1: "What is the capital of France?",
            2: "Who painted the Mona Lisa?",
            # Add more questions as needed
        }

        # Display the loaded question in the label
        self.question_label.setText(questions.get(question_number, "Question not found"))

if __name__ == '__main__':
    app = QApplication([])
    window = QuestionApp()
    window.show()
    app.exec_()
