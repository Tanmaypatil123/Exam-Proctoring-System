import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPlainTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QColor

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Code Editor')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        self.editor = QPlainTextEdit()
        self.editor.setFont(QFont("Consolas", 12))  # Set font
        self.editor.setStyleSheet("background-color: black; color: white;")  # Set background color and font color
        self.layout.addWidget(self.editor)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.createMenuBar()

    def createMenuBar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.saveFile)
        file_menu.addAction(save_action)

    def saveFile(self):
        text = self.editor.toPlainText()
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;Python Files (*.py)')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text)

def main():
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
