# from PyQt5.QtCore import QObject, Qt, pyqtSignal, QThread, QTimer
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QImage, QPixmap
# import cv2
# import os
# import shutil
# from ultralytics import YOLO
# import sys

# class FaceDetectionWorker(QObject):
#     update_frame = pyqtSignal(QImage, int)

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#         self.frame = None

#     def detect_faces(self, frame):
#         self.frame = frame
#         gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
#         faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

#         for (x, y, w, h) in faces:
#             cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#         num_faces = len(faces)
#         print(f"Number of detected faces: {num_faces}")

#         image = self.convert_frame(self.frame)
#         self.update_frame.emit(image, num_faces)

#     def convert_frame(self, frame):
#         rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = rgb_image.shape
#         bytes_per_line = ch * w
#         convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         return convert_to_qt_format


# class YOLODetectionWorker(QObject):
#     phone_detection = pyqtSignal(bool)

#     def __init__(self, image_path, parent=None):
#         super().__init__(parent)
#         self.image_path = image_path

#     def detect_objects(self):
#         model = YOLO("best.pt")
#         model.fuse()
#         predictions = model(self.image_path, verbose=False, save_txt=True)
#         txt_file_path = "runs/detect/predict/labels/captured_image.txt"
#         file_exists = os.path.exists(txt_file_path)
#         runs_path = "runs"

#         if file_exists:
#             print("Text file generated.")
#             shutil.rmtree(runs_path)
#             print("Folder 'runs' deleted.")
#             self.phone_detection.emit(True)
#         else:
#             print("Text file not generated.")
#             shutil.rmtree(runs_path)
#             self.phone_detection.emit(False)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.label = QLabel()
#         self.setCentralWidget(self.label)

#         self.video_capture = cv2.VideoCapture(0)

#         self.face_worker = FaceDetectionWorker()
#         self.yolo_worker = YOLODetectionWorker("captured_image.png")

#         self.thread_face_detection = QThread(self)
#         self.thread_yolo_detection = QThread(self)

#         self.setup_workers()
#         # self.start_threads()

#     def setup_workers(self):
#         self.face_worker.moveToThread(self.thread_face_detection)
#         self.yolo_worker.moveToThread(self.thread_yolo_detection)

#         self.face_worker.update_frame.connect(self.display_frame)
#         self.yolo_worker.phone_detection.connect(self.handle_yolo_detection)

#         self.thread_face_detection.started.connect(self.perform_face_detection)
#         self.thread_yolo_detection.started.connect(self.perform_yolo_detection)

#     def perform_face_detection(self):
#         while True:
#             ret, frame = self.video_capture.read()
#             if ret:
#                 self.face_worker.detect_faces(frame)

#     def perform_yolo_detection(self):
#         self.yolo_worker.detect_objects()

#     def display_frame(self, frame, num_persons):
#         pixmap = QPixmap.fromImage(frame)
#         self.label.setPixmap(pixmap)
#         # Handle displaying faces or any necessary UI updates based on face detection

#     def handle_yolo_detection(self, result):
#         # Handle YOLO detection result, e.g., show message or update UI based on phone detection
#         print("YOLO Phone Detection Result:", result)

#     def closeEvent(self, event):
#         self.video_capture.release()
#         event.accept()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QImage, QPixmap
import cv2
import os
import shutil
from ultralytics import YOLO
import sys

class FaceDetectionWorker(QObject):
    update_frame = pyqtSignal(QImage, int)

    def __init__(self):
        super().__init__()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        num_faces = len(faces)
        image = self.convert_frame(frame)
        self.update_frame.emit(image, num_faces)

    def convert_frame(self, frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return convert_to_qt_format


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.setCentralWidget(self.label)

        self.video_capture = cv2.VideoCapture(0)

        self.face_worker = FaceDetectionWorker()
        self.yolo_worker = YOLODetectionWorker()

        self.thread_face_detection = QThread(self)
        self.thread_yolo_detection = QThread(self)

        self.start_workers()

    def start_workers(self):
        self.face_worker.moveToThread(self.thread_face_detection)
        self.yolo_worker.moveToThread(self.thread_yolo_detection)

        self.face_worker.update_frame.connect(self.display_frame)
        self.thread_face_detection.started.connect(self.perform_face_detection)
        self.thread_yolo_detection.started.connect(self.perform_yolo_detection)
        
        self.thread_face_detection.start()
        self.thread_yolo_detection.start()

    def perform_face_detection(self):
        while True:
            ret, frame = self.video_capture.read()
            if ret:
                self.face_worker.detect_faces(frame)
                cv2.waitKey(1)

    def perform_yolo_detection(self):
        while True:
            ret, frame = self.video_capture.read()
            if ret:
                image_path = "captured_image.png"
                cv2.imwrite(image_path, frame)
                self.yolo_worker.detect_objects(image_path)
                cv2.waitKey(1)

    def display_frame(self, frame, num_persons):
        pixmap = QPixmap.fromImage(frame)
        self.label.setPixmap(pixmap)
        # Handle displaying faces or any necessary UI updates based on face detection

    def handle_yolo_detection(self, result):
        # Handle YOLO detection result, e.g., show message or update UI based on phone detection
        print("YOLO Phone Detection Result:", result)

    def closeEvent(self, event):
        self.thread_face_detection.quit()
        self.thread_yolo_detection.quit()
        self.video_capture.release()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
