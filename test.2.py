import sys
import cv2
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QImage, QPixmap


class UpperBodyDetector(QThread):
    upper_body_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.body_parts = {
            "Nose": 0,
            "Neck": 1,
            "RShoulder": 2,
            "RElbow": 3,
            "RWrist": 4,
            "LShoulder": 5,
            "LElbow": 6,
            "LWrist": 7,
            "RHip": 8,
            "RKnee": 9,
            "RAnkle": 10,
            "LHip": 11,
            "LKnee": 12,
            "LAnkle": 13,
            "REye": 14,
            "LEye": 15,
            "REar": 16,
            "LEar": 17,
            "Background": 18,
        }
        self.pose_pairs = [
            ["Neck", "RShoulder"],
            ["Neck", "LShoulder"],
            ["RShoulder", "RElbow"],
            ["RElbow", "RWrist"],
            ["LShoulder", "LElbow"],
            ["LElbow", "LWrist"],
            ["Neck", "RHip"],
            ["RHip", "RKnee"],
            ["RKnee", "RAnkle"],
            ["Neck", "LHip"],
            ["LHip", "LKnee"],
            ["LKnee", "LAnkle"],
            ["Neck", "Nose"],
            ["Nose", "REye"],
            ["REye", "REar"],
            ["Nose", "LEye"],
            ["LEye", "LEar"],
        ]

        self.in_width = 368
        self.in_height = 368
        self.thr = 0.2

        self.net = cv2.dnn.readNetFromTensorflow("graph_opt.pb")
        self.upper_body_parts = [
            "Nose",
            "Neck",
            "RShoulder",
            "LShoulder",
            "REye",
            "LEye",
        ]

        self.cap = cv2.VideoCapture(0)  # Use 0 instead of 1 for the default camera

    def run(self):
        while True:
            has_frame, frame = self.cap.read()
            if not has_frame:
                break

            frame_width = frame.shape[1]
            frame_height = frame.shape[0]

            self.net.setInput(
                cv2.dnn.blobFromImage(
                    frame,
                    1.0,
                    (self.in_width, self.in_height),
                    (127.5, 127.5, 127.5),
                    swapRB=True,
                    crop=False,
                )
            )
            out = self.net.forward()
            out = out[
                :, :19, :, :
            ]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

            assert len(self.body_parts) == out.shape[1]

            points = []
            for i in range(len(self.body_parts)):
                heat_map = out[0, i, :, :]

                _, conf, _, point = cv2.minMaxLoc(heat_map)
                x = (frame_width * point[0]) / out.shape[3]
                y = (frame_height * point[1]) / out.shape[2]
                points.append((int(x), int(y)) if conf > self.thr else None)

            upper_body_visible = all(
                points[self.body_parts[part]] is not None
                for part in self.upper_body_parts
            )
            self.upper_body_signal.emit(upper_body_visible)

    def stop(self):
        self.cap.release()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.upper_body_detector = UpperBodyDetector()
        self.upper_body_detector.upper_body_signal.connect(self.on_upper_body_signal)

        self.upper_body_detector.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_warning)
        self.timer.start(300)  # Check every 0.01 second for upper body detection

        self.upper_body_visible = False

    def on_upper_body_signal(self, visible):
        self.upper_body_visible = visible

    def show_warning(self):
        if not self.upper_body_visible:
            self.statusBar().showMessage(
                "Upper body is not visible for more than 3 seconds"
            )
        else:
            self.statusBar().clearMessage()

    def closeEvent(self, event):
        self.upper_body_detector.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
