import sys
import cv2
import os
import shutil
from ultralytics import YOLO
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal

class DetectionThread(QThread):
    finished = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def run(self):
        self.model = YOLO("best.pt")
        self.model.fuse()

        self.detectObjects("captured_image.png")

    def detectObjects(self, image_path):
        predictions = self.model(image_path, verbose=False, save_txt=True)
        txt_file_path = "runs\detect\predict\labels\captured_image.txt"
        file_exists = os.path.exists(txt_file_path)
        
        if file_exists:
            print("Text file generated.")
            shutil.rmtree("runs\detect\predict")  # Remove the entire folder predict and its contents
            print("Folder 'predict' deleted.")
            self.finished.emit(True)
        else:
            print("Text file not generated.")
            self.finished.emit(False)

class Worker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Object Detection")
        self.setGeometry(100, 100, 640, 480)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)

        self.capture_btn = QPushButton("Capture")
        self.capture_btn.clicked.connect(self.captureImage)
        self.layout.addWidget(self.capture_btn)

        self.central_widget.setLayout(self.layout)

        self.video_capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(30)

        self.detection_thread = DetectionThread()
        self.detection_thread.finished.connect(self.detectionFinished)

    def captureImage(self):
        ret, frame = self.video_capture.read()
        cv2.imwrite("captured_image.png", frame)
        self.detection_thread.start()

    def updateFrame(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            image = QPixmap.fromImage(convert_to_Qt_format)
            self.image_label.setPixmap(image)

    def detectionFinished(self, result):
        print("Result:", result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    worker = Worker()
    worker.show()
    sys.exit(app.exec_())
