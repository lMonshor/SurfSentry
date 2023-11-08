from PyQt6.QtCore import Qt, QRect, QSize, QPoint
from PyQt6.QtWidgets import QApplication, QAbstractButton, QPushButton, QWidget, QLabel, QSizePolicy, QCheckBox, QVBoxLayout
from PyQt6.QtGui import QPixmap, QFont, QIcon, QCursor
from ui import menu_ui,toggle_switch
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class uiWidget(QWidget):
    def __init__(self):
        self.my_tray_app_ui = None
        self.my_menu_ui = None
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("widget_ui")
        self.setFixedSize(326, 426)
        self.setWindowFlags(Qt.WindowType.Popup |
                            Qt.WindowType.WindowStaysOnTopHint)
        self.control_widget = QtWidgets.QWidget(self)
        self.control_widget.setGeometry(QtCore.QRect(0, 0, 326, 380))
        self.control_widget.setAutoFillBackground(False)
        self.control_widget.setStyleSheet("background-color: #0f0f0f")
        self.control_widget.setObjectName("control_widget")
        self.control_logo = QtWidgets.QLabel(self)
        self.control_logo.setGeometry(QtCore.QRect(73, 50, 180, 84))
        self.control_logo.setText("")
        self.control_logo.setPixmap(QtGui.QPixmap("project/assets/control_logo.png"))
        self.control_logo.setScaledContents(True)
        self.control_logo.setWordWrap(False)
        self.control_logo.setObjectName("control_logo")

        self.control_toggle_button = toggle_switch.CustomToggleSwitch()
        self.control_toggle_button.setParent(self.control_widget)
        self.control_toggle_button.setGeometry(QRect(88, 155, 140, 70))
        self.control_toggle_button.toggleChanged.connect(self.startSniff)
        self.control_toggle_button.setObjectName("control_toggle_button")


        self.control_status_title_label = QtWidgets.QLabel(self)
        self.control_status_title_label.setGeometry(QtCore.QRect(88, 240, 150, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.control_status_title_label.setFont(font)
        self.control_status_title_label.setStyleSheet("color:#FEFEFE;")
        self.control_status_title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.control_status_title_label.setObjectName("control_status_title_label")
        self.control_status_title_label.setText("Disconnected")
        self.control_status_desc_label = QtWidgets.QLabel(self)
        self.control_status_desc_label.setGeometry(QtCore.QRect(40, 270, 246, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_status_desc_label.sizePolicy().hasHeightForWidth())
        self.control_status_desc_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.control_status_desc_label.setFont(font)
        self.control_status_desc_label.setStyleSheet("color:#FEFEFE;")
        self.control_status_desc_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.control_status_desc_label.setObjectName("control_status_desc_label")
        self.control_status_desc_label.setText("Your Internet is not secure")
        self.bottom_widget = QtWidgets.QWidget(parent=self)
        self.bottom_widget.setGeometry(QtCore.QRect(0, 380, 326, 46))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.bottom_widget.setFont(font)
        self.bottom_widget.setAutoFillBackground(False)
        self.bottom_widget.setStyleSheet("background-color:#393E46")
        self.bottom_widget.setObjectName("bottom_widget")
        self.bottom_settings_button = QtWidgets.QPushButton(parent=self.bottom_widget)
        self.bottom_settings_button.setGeometry(QtCore.QRect(286, 8, 30, 30))
        self.bottom_settings_button.setStyleSheet("QPushButton:hover {\n"
"                background-color: #696969;}\n"
"            QPushButton {\n"
"                border-style: none;\n"
"                color: black;}")
        self.bottom_settings_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("project/assets/bottom_setting_button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bottom_settings_button.setIcon(icon)
        self.bottom_settings_button.setIconSize(QtCore.QSize(24, 24))
        self.bottom_settings_button.clicked.connect(self.showMenu_ui)
        self.bottom_settings_button.setObjectName("bottom_settings_button")
        self.bottom_bug_button = QtWidgets.QPushButton(parent=self.bottom_widget)
        self.bottom_bug_button.setGeometry(QtCore.QRect(250, 8, 30, 30))
        self.bottom_bug_button.setStyleSheet("QPushButton:hover {\n"
"                background-color: #696969;}\n"
"            QPushButton {\n"
"                border-style: none;\n"
"                color: black;}")
        self.bottom_bug_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("project/assets/bottom_bug_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bottom_bug_button.setIcon(icon1)
        self.bottom_bug_button.setIconSize(QtCore.QSize(24, 24))
        self.bottom_bug_button.setObjectName("bottom_bug_button")
        self.bottom_logo_label = QtWidgets.QLabel(parent=self.bottom_widget)
        self.bottom_logo_label.setGeometry(QtCore.QRect(10, 8, 140, 30))
        self.bottom_logo_label.setText("")
        self.bottom_logo_label.setPixmap(QtGui.QPixmap("project/assets/bottom_logo.png"))
        self.bottom_logo_label.setScaledContents(True)
        self.bottom_logo_label.setObjectName("bottom_logo_label")

    def showMenu_ui(self):
        click_pos = QCursor.pos()
        menu_width = self.my_menu_ui.width()
        menu_height = self.my_menu_ui.height()
        menu_pos = click_pos - QPoint(menu_width, menu_height)
        self.my_menu_ui.setGeometry(
            menu_pos.x(), menu_pos.y(), menu_width, menu_height)
        self.my_menu_ui.show()
        
    def startSniff(self):
        if self.control_toggle_button.toggled:
            self.my_tray_app_ui.setIcon(QIcon("project/assets/icon_active.png"))
            print("started")
        else:
            self.my_tray_app_ui.setIcon(QIcon("project/assets/icon_passive.png"))
            print("stopped")
   

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget_ui = uiWidget()
    widget_ui.show()
    sys.exit(app.exec())
