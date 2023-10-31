import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QRect, QTimer, QPropertyAnimation, pyqtSignal

class CustomToggleSwitch(QWidget):
    toggleChanged = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.toggle_frame = QWidget(self)
        self.toggle_frame.setFixedSize(130, 60)
        self.toggle_frame.setStyleSheet(
            "background-color: #555; border-radius: 30px;")

        # Hareket eden topu ortala
        self.toggle_button = QLabel(self.toggle_frame)
        self.toggle_button.setGeometry(6, 8, 44, 44)
        self.toggle_button.setStyleSheet(
            "background-color: #fff; border-radius: 22px;")

        layout.addWidget(self.toggle_frame)

        self.setLayout(layout)

        self.toggle_frame.mousePressEvent = self.toggleSwitch

        self.animation = QPropertyAnimation(self.toggle_button, b"geometry")
        self.animation.setDuration(150)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateToggle)
        self.toggled = False

    def toggleSwitch(self, event):
        if not self.toggled:
            self.animation.setStartValue(QRect(6, 8, 44, 44)) 
            self.animation.setEndValue(QRect(80, 8, 44, 44)) 
            self.toggled = True
            self.toggle_frame.setStyleSheet(
                "background-color: #4caf50; border-radius: 30px;")
        else:
            self.animation.setStartValue(QRect(80, 8, 44, 44)) 
            self.animation.setEndValue(QRect(6, 8, 44, 44))
            self.toggled = False
            self.toggle_frame.setStyleSheet(
                "background-color: #555; border-radius: 30px;")

        self.animation.start()
        self.timer.start(100)

        self.toggleChanged.emit(self.toggled) 
    def updateToggle(self):
        if self.animation.state() == QPropertyAnimation.State.Running:
            self.toggle_button.setGeometry(self.animation.currentValue())
        else:
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomToggleSwitch()
    window.show()
    sys.exit(app.exec())
