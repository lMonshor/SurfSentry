
from PyQt6 import QtCore, QtGui, QtWidgets
from styles.components_styles import qfonts_styles, qlabels_styles, qprogressbars_styles
from ui.components import qlabel_generator
from styles.ui_styles import default_styles


class UiLoading(QtWidgets.QDialog):
    def __init__(self):
        self.my_update_data_worker = None
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(410, 140)
        self.setStyleSheet(default_styles.dark_style)
        self.setWindowFlags(
            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.loading_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(50, 20, 200, 46)),
            color=qlabels_styles.title_color,
            font=qfonts_styles.subtitle_font,
            text="Checking for new Malicious Data. Please Wait...")
        self.loading_title.adjustSize()
        self.loading_title.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        self.loading_prog_bar = QtWidgets.QProgressBar(self)
        self.loading_prog_bar.setGeometry(QtCore.QRect(95, 70, 220, 24))
        self.loading_prog_bar.setProperty("value", 0)
        self.loading_prog_bar.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loading_prog_bar.setTextVisible(False)
        self.loading_prog_bar.setInvertedAppearance(False)
        self.loading_prog_bar.setTextDirection(
            QtWidgets.QProgressBar.Direction.TopToBottom)
        self.loading_prog_bar.setStyleSheet(
            qprogressbars_styles.qprogressbar_style)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateProgressBar)

        self.timer.start(5)

        self.loading_prg_bar_direction = False

    def updateProgressBar(self):
        value = self.loading_prog_bar.value()
        if value <= 100:
            if self.loading_prg_bar_direction:
                if value == 0:
                    self.loading_prg_bar_direction = False
                value -= 1
            elif not self.loading_prg_bar_direction:
                value += 1
                if value == 100:
                    self.loading_prg_bar_direction = True
            self.loading_prog_bar.setInvertedAppearance(
                self.loading_prg_bar_direction)
            self.loading_prog_bar.setValue(value)

    def stop_worker(self):
        self.my_update_data_worker.exit()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UiLoading()
    ui.show()
    app.exec()
