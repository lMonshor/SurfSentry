
from PyQt6 import QtCore, QtGui, QtWidgets


class uiInformation(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(390, 110)
        self.setStyleSheet("background-color:black;")
        self.setWindowFlags(
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.dialog_inf_ok_button = QtWidgets.QDialogButtonBox(parent=self)
        self.dialog_inf_ok_button.setGeometry(QtCore.QRect(157, 70, 75, 24))
        self.dialog_inf_ok_button.setStyleSheet("QPushButton{\n"
"    background-color:#1F1F1F;\n"
"   color:white;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #484848;\n"
"}")
        self.dialog_inf_ok_button.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dialog_inf_ok_button.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.dialog_inf_ok_button.clicked.connect(self.deleteLater)
        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(10, 0, 370, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setText(("Succesfully updated"))
