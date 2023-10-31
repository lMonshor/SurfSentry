
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class uiLoading(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("dialog_ui")
        self.setFixedSize(410, 140)
        self.setStyleSheet("background-color:black;")
        self.setWindowFlags(
                            Qt.WindowType.WindowStaysOnTopHint)
        self.dialog_loading_cancel_button = QtWidgets.QDialogButtonBox(self)
        self.dialog_loading_cancel_button.setGeometry(QtCore.QRect(167, 100, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.dialog_loading_cancel_button.setFont(font)
        self.dialog_loading_cancel_button.setStyleSheet("QPushButton{\n"
"    background-color:#1F1F1F;\n"
"   color:white;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #484848;\n"
"}")
        self.dialog_loading_cancel_button.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dialog_loading_cancel_button.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.dialog_loading_cancel_button.setCenterButtons(False)
        self.dialog_loading_cancel_button.setObjectName("dialog_loading_cancel_button")
        self.dialog_loading_prog_bar = QtWidgets.QProgressBar(self)
        self.dialog_loading_prog_bar.setGeometry(QtCore.QRect(95, 60, 220, 24))
        self.dialog_loading_prog_bar.setProperty("value", 0)
        self.dialog_loading_prog_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dialog_loading_prog_bar.setTextVisible(False)
        self.dialog_loading_prog_bar.setInvertedAppearance(False)
        self.dialog_loading_prog_bar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateProgressBar)

        self.timer.start(5)
        self.dialog_loading_prog_bar.setObjectName("dialog_loading_prog_bar")
        self.dialog_loading_logo = QtWidgets.QLabel(self)
        self.dialog_loading_logo.setGeometry(QtCore.QRect(20, 50, 33, 38))
        self.dialog_loading_logo.setText("")
        self.dialog_loading_logo.setPixmap(QtGui.QPixmap("project/assets/icon_active.png"))
        self.dialog_loading_logo.setScaledContents(True)
        self.dialog_loading_logo.setObjectName("dialog_loading_logo")
        self.dialog_loading_title = QtWidgets.QLabel(self)
        self.dialog_loading_title.setGeometry(QtCore.QRect(73, 20, 264, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.dialog_loading_title.setFont(font)
        self.dialog_loading_title.setStyleSheet("color:white;")
        self.dialog_loading_title.setObjectName("dialog_loading_title")

      
        self.dialog_loading_cancel_button.accepted.connect(self.accept)
        self.dialog_loading_cancel_button.rejected.connect(self.reject) 
    
        self.dialog_loading_title.setText("Checking for new malicious data...")
        self.bool = False

    def updateProgressBar(self):
        value = self.dialog_loading_prog_bar.value()
        if value <= 100:
            if self.bool:
                if value ==0:
                    self.bool = False
                value -= 1
            elif not self.bool:
                value += 1
                if value == 100:
                    self.bool = True
            self.dialog_loading_prog_bar.setInvertedAppearance(self.bool)
            self.dialog_loading_prog_bar.setValue(value)
        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     loading_ui = uiLoading()
#     loading_ui.show()
#     sys.exit(app.exec())
