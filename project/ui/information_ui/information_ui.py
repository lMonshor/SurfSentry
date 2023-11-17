
from PyQt6 import QtCore, QtGui, QtWidgets
from styles.components_styles import qfonts_styles, qlabels_styles
from ui.components import qlabel_generator,qpushbutton_generator


class UiInformation(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(390, 110)
        self.setStyleSheet("background-color:#0f0f0f;")
        self.setWindowFlags(
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        
        self.information_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(75, 20, 200, 46)),
            color=qlabels_styles.title_color,
            font=qfonts_styles.subtitle_font,
            text="Succesfully updated")
        self.information_title.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.information_title.adjustSize()
        
        
        self.information_ok_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(157, 70, 75, 24)),
            on_click=(self.deleteLater),
            text="OK")