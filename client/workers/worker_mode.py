import sys
import cv2
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QImage, QPixmap
from ultralytics import YOLO
import os
import shutil

# class Worker(QThread):
#     update_frame = pyqtSignal(QImage, int)
#     phone_detection = pyqtSignal(bool)

#     def __init__(self):
#         super().__init__()
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#         self.cap = cv2.VideoCapture(0)
#         self.running = True
#         self.no_persons_time = 0
#         self.more_than_one_person_time = 0
#         self.model = YOLO("best.pt")
#         self.model.fuse()

#     def run(self):
#         while self.running:
#             ret, frame = self.cap.read()
#             if ret:
#                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                 faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

#                 num_persons = len(faces)

#                 if num_persons == 0:
#                     self.no_persons_time += 1
#                     if self.no_persons_time >= 90:  # 3 seconds threshold (30 frames per second)
#                         image = self.convert_frame(frame)
#                         self.update_frame.emit(image, num_persons)
#                 else:
#                     self.no_persons_time = 0

#                 if num_persons > 1:
#                     self.more_than_one_person_time += 1
#                     if self.more_than_one_person_time >= 90:  # 3 seconds threshold (30 frames per second)
#                         image = self.convert_frame(frame)
#                         self.update_frame.emit(image, num_persons)
#                 else:
#                     self.more_than_one_person_time = 0

#                 image = self.convert_frame(frame)
#                 self.update_frame.emit(image, num_persons)
#                 print(num_persons)
#                 self.save_frame_as_png(frame,"captured_image.png")
#                 self.detectObjects("captured_image.png")

#     def convert_frame(self, frame):
#         rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = rgb_image.shape
#         bytes_per_line = ch * w
#         convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         return convert_to_qt_format
    
#     def save_frame_as_png(self,frame, filename):
#         cv2.imwrite(filename, frame)
    
#     def detectObjects(self, image_path):
#         predictions = self.model(image_path, verbose=False, save_txt=True)
#         txt_file_path = "runs\detect\predict\labels\captured_image.txt"
#         file_exists = os.path.exists(txt_file_path)
#         runs_path = "runs"
#         if file_exists:
#             print("Text file generated.")
#             # shutil.rmtree(r"C:\Users\patil\Desktop\SIH Project\Ctrl-Alt-Defeat\runs\detect")  # Remove the entire folder predict and its contents
#             self.removeRunsDirectory(runs_path)
#             print("Folder 'predict' deleted.")
#             self.phone_detection.emit(True)
#         else:
#             print("Text file not generated.")
#             self.removeRunsDirectory(runs_path)
#             self.phone_detection.emit(False)

#     def removeRunsDirectory(self, dir_path):
#         print(f"Deleting directory: {dir_path}")
#         # Use shutil.rmtree to remove the 'runs' directory and its contents
#         shutil.rmtree(dir_path)
#     def stop(self):
#         self.running = False
#         self.wait()
#         self.cap.release()


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.worker = Worker()
#         self.worker.update_frame.connect(self.display_frame)

#         self.label = QLabel()
#         self.setCentralWidget(self.label)

#         self.worker.start()

#         self.no_persons_timer = QTimer()
#         self.no_persons_timer.timeout.connect(self.show_no_person_warning)
#         self.no_persons_timer.start(300)  # Check every 0.01 second

#         self.more_than_one_person_timer = QTimer()
#         self.more_than_one_person_timer.timeout.connect(self.show_more_than_one_person_warning)
#         self.more_than_one_person_timer.start(300)  # Check every 0.01 second

#         self.no_persons_flag = False
#         self.more_than_one_person_flag = False

#     def display_frame(self, frame, num_persons):
#         pixmap = QPixmap.fromImage(frame)
#         self.label.setPixmap(pixmap)

#         if num_persons == 0:
#             self.no_persons_flag = True
#             self.more_than_one_person_flag = False
#         elif num_persons > 1:
#             self.no_persons_flag = False
#             self.more_than_one_person_flag = True
#         else:
#             self.no_persons_flag = False
#             self.more_than_one_person_flag = False

#     def show_no_person_warning(self):
#         if self.no_persons_flag:
#             self.worker.no_persons_time += 1
#             if self.worker.no_persons_time >= 90:  # 3 seconds threshold (30 frames per second)
#                 self.statusBar().showMessage("No person detected for more than 3 seconds")
#         else:
#             self.worker.no_persons_time = 0
#             self.statusBar().clearMessage()

#     def show_more_than_one_person_warning(self):
#         if self.more_than_one_person_flag:
#             self.worker.more_than_one_person_time += 1
#             if self.worker.more_than_one_person_time >= 90:  # 3 seconds threshold (30 frames per second)
#                 self.statusBar().showMessage("More than one person detected")
#         else:
#             self.worker.more_than_one_person_time = 0
#             self.statusBar().clearMessage()

#     def closeEvent(self, event):
#         self.worker.stop()
#         event.accept()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# Face Detection Worker
class FaceDetectionWorker(QThread):
    update_frame = pyqtSignal(QImage, int)

    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def run(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        num_faces = len(faces)
        print(f"Number of detected faces: {num_faces}")

        image = self.convert_frame(self.frame)
        self.update_frame.emit(image, num_faces)

    def convert_frame(self, frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return convert_to_qt_format


# YOLO Detection Worker
class YOLODetectionWorker(QThread):
    phone_detection = pyqtSignal(bool)

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.model = YOLO("best.pt")
        self.model.fuse()

    def run(self):
        predictions = self.model(self.image_path, verbose=False, save_txt=True)
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

        self.face_worker = None
        self.yolo_worker = None

        self.start_workers()

    def start_workers(self):
        while True:
            ret, frame = self.video_capture.read()
            if ret:
                if self.face_worker is None or not self.face_worker.isRunning():
                    self.face_worker = FaceDetectionWorker(frame)
                    self.face_worker.update_frame.connect(self.display_frame)
                    self.face_worker.start()

                if self.yolo_worker is None or not self.yolo_worker.isRunning():
                    # Convert frame to image path and start YOLO worker
                    image_path = "captured_image.png"
                    cv2.imwrite(image_path, frame)

                    self.yolo_worker = YOLODetectionWorker(image_path)
                    self.yolo_worker.phone_detection.connect(self.handle_yolo_detection)
                    self.yolo_worker.start()

                cv2.waitKey(1)

    def display_frame(self, frame, num_persons):
        pixmap = QPixmap.fromImage(frame)
        self.label.setPixmap(pixmap)
        # Handle displaying faces or any necessary UI updates based on face detection

    def handle_yolo_detection(self, result):
        # Handle YOLO detection result, e.g., show message or update UI based on phone detection
        print("YOLO Phone Detection Result:", result)

    def closeEvent(self, event):
        self.video_capture.release()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
