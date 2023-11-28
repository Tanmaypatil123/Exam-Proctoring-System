import sys
import cv2
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QImage, QPixmap

class Worker(QThread):
    update_frame = pyqtSignal(QImage, int)

    def __init__(self):
        super().__init__()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        self.running = True
        self.no_persons_time = 0

    def run(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

                num_persons = len(faces)

                if num_persons == 0:
                    self.no_persons_time += 1
                    if self.no_persons_time >= 90:  # 3 seconds threshold (30 frames per second)
                        image = self.convert_frame(frame)
                        self.update_frame.emit(image, num_persons)
                else:
                    self.no_persons_time = 0

                if num_persons != 1:
                    image = self.convert_frame(frame)
                    self.update_frame.emit(image, num_persons)
                else:
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    image = self.convert_frame(frame)
                    self.update_frame.emit(image, num_persons)

    def convert_frame(self, frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return convert_to_qt_format

    def stop(self):
        self.running = False
        self.wait()
        self.cap.release()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.update_frame.connect(self.display_frame)

        self.label = QLabel()
        self.setCentralWidget(self.label)

        self.worker.start()

    def display_frame(self, frame, num_persons):
        pixmap = QPixmap.fromImage(frame)
        self.label.setPixmap(pixmap)
        if num_persons == 0:
            self.statusBar().showMessage("No person detected for more than 3 seconds")
        elif num_persons != 1:
            self.statusBar().showMessage("More than one person detected")
        else:
            self.statusBar().clearMessage()

    def closeEvent(self, event):
        self.worker.stop()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
