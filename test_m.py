import sys
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class TimerWorker(QThread):
    timer_updated = pyqtSignal()
    timer_completed = pyqtSignal()

    def __init__(self, duration_minutes):
        super().__init__()
        self.duration_seconds = duration_minutes * 60

    def run(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_timer)
        timer.start(1000)  # Update every second

        self.exec_()

    def update_timer(self):
        self.duration_seconds -= 1
        self.timer_updated.emit()  # Emit signal for timer update

        if self.duration_seconds <= 0:
            self.timer_completed.emit()
            self.quit()

    def update_timer_label(self):
        minutes, seconds = divmod(self.duration_seconds, 60)
        print(f"{minutes:02d}:{seconds:02d}")


class ExamTimerApp(QWidget):
    def __init__(self, duration_minutes):
        super().__init__()

        self.timer_worker = TimerWorker(duration_minutes)
        self.timer_worker.timer_completed.connect(self.on_timer_completed)
        self.timer_worker.timer_updated.connect(self.update_timer_label)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Exam Timer")
        self.setGeometry(100, 100, 300, 150)

        self.timer_label = QLabel()
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.update_timer_label()

        layout = QVBoxLayout()
        layout.addWidget(self.timer_label)
        self.setLayout(layout)

        self.show()

        self.timer_worker.start()

    def update_timer_label(self):
        minutes, seconds = divmod(self.timer_worker.duration_seconds, 60)
        self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")

    def on_timer_completed(self):
        print("Timer Completed!")
        # Add your code here for actions to be taken when the timer completes,
        # such as showing a message or triggering another event.


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # You can set the duration in minutes here
    duration_minutes = 1

    exam_timer_app = ExamTimerApp(duration_minutes)
    sys.exit(app.exec_())
