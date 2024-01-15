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
