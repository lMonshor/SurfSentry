from PyQt6.QtWidgets import QApplication, QInputDialog, QMessageBox
from PyQt6 import QtWidgets, QtCore
import socket
from ui.loading_ui import loading_ui
from features import helper_methods
from features import workers

from PyQt6 import QtCore, QtGui, QtWidgets
from styles.components_styles import qfonts_styles, qlabels_styles, qprogressbars_styles
from ui.components import qlabel_generator
from styles.ui_styles import default_styles
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QVBoxLayout, QPushButton
from ui.components import component_hcenterer, qpushbutton_generator, qlayout_qwidget_generator


class UiInputWidget(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(280, 130)
        self.setStyleSheet(default_styles.dark_style)
        self.setWindowFlags(
            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.input_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(20, 15, 1, 1)),
            color=qlabels_styles.title_color,
            font=qfonts_styles.title_font,
            text="Please insert an IP or Domain:")
        self.input_title.adjustSize()

        self.input_line = QLineEdit(self)
        self.input_line.setGeometry(QtCore.QRect(20, 50, 240, 20))
        self.input_line.setStyleSheet('''
            QLineEdit {
                color: white;
                border: 1px solid white;  /* Remove border */
            }
        ''')

        self.input_ok_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(30, 85, 100, 25)),
            text="OK",
            on_click=self.accept
        )

        self.input_cancel_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(150, 85, 100, 25)),
            text="Cancel",
            on_click=self.reject
        )

if __name__ == '__main__':
    app = QApplication([])

    input_dialog = UiInputWidget()

    app.exec()
