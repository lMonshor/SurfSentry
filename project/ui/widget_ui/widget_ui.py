from PyQt6 import QtCore, QtGui, QtWidgets
from ui.toggle_button_ui import toggle_switch
from features import blocking_operations
from redirections import redirection_operations
from features import workers
import os


class uiWidget(QtWidgets.QWidget):
    def __init__(self, my_tray_app_ui, my_menu_ui, my_pref_ui):
        self.my_tray_app_ui = my_tray_app_ui
        self.my_menu_ui = my_menu_ui
        self.my_pref_ui = my_pref_ui

        super().__init__()
        self.initUI()

    def initUI(self):
        self.active_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\..\\assets', 'icon_active.png')
        self.pasive_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\..\\assets', 'icon_passive.png')
        control_logo_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\..\\assets', 'control_logo.png')
        bottom_settings_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\..\\assets', 'bottom_settings_button.png')
        bottom_bug_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\..\\assets', 'bottom_bug_logo.png')
        bottom_logo_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\..\\assets', 'bottom_logo.png')

        self.setFixedSize(326, 426)
        self.setWindowFlags(QtCore.Qt.WindowType.Popup |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.control_widget = QtWidgets.QWidget(self)
        self.control_widget.setGeometry(QtCore.QRect(0, 0, 326, 380))
        self.control_widget.setAutoFillBackground(False)
        self.control_widget.setStyleSheet("background-color: #0f0f0f")
        self.control_logo = QtWidgets.QLabel(self)
        self.control_logo.setGeometry(QtCore.QRect(73, 50, 180, 84))
        self.control_logo.setText("")

        self.control_logo.setPixmap(QtGui.QPixmap(control_logo_icon_path))
        self.control_logo.setScaledContents(True)
        self.control_logo.setWordWrap(False)

        self.control_toggle_button = toggle_switch.CustomToggleSwitch()
        self.control_toggle_button.setParent(self.control_widget)
        self.control_toggle_button.setGeometry(QtCore.QRect(88, 155, 140, 70))
        self.control_toggle_button.toggleChanged.connect(self.switchChanged)

        self.control_status_title_label = QtWidgets.QLabel(self)
        self.control_status_title_label.setGeometry(
            QtCore.QRect(88, 240, 150, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.control_status_title_label.setFont(font)
        self.control_status_title_label.setStyleSheet("color:#FEFEFE;")
        self.control_status_title_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.control_status_title_label.setText("Disconnected")
        self.control_status_desc_label = QtWidgets.QLabel(self)
        self.control_status_desc_label.setGeometry(
            QtCore.QRect(40, 270, 246, 28))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.control_status_desc_label.sizePolicy().hasHeightForWidth())
        self.control_status_desc_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.control_status_desc_label.setFont(font)
        self.control_status_desc_label.setStyleSheet("color:#FEFEFE;")
        self.control_status_desc_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.control_status_desc_label.setText("Your Internet is not secure")
        self.bottom_widget = QtWidgets.QWidget(parent=self)
        self.bottom_widget.setGeometry(QtCore.QRect(0, 380, 326, 46))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.bottom_widget.setFont(font)
        self.bottom_widget.setAutoFillBackground(False)
        self.bottom_widget.setStyleSheet("background-color:#393E46")
        self.bottom_settings_button = QtWidgets.QPushButton(
            parent=self.bottom_widget)
        self.bottom_settings_button.setGeometry(QtCore.QRect(286, 8, 30, 30))
        self.bottom_settings_button.setStyleSheet("QPushButton:hover {\n"
                                                  "                background-color: #696969;}\n"
                                                  "            QPushButton {\n"
                                                  "                border-style: none;\n"
                                                  "                color: black;}")
        self.bottom_settings_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(bottom_settings_icon_path),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bottom_settings_button.setIcon(icon)
        self.bottom_settings_button.setIconSize(QtCore.QSize(24, 24))
        self.bottom_settings_button.clicked.connect(self.showMenu_ui)
        self.bottom_bug_button = QtWidgets.QPushButton(
            parent=self.bottom_widget)
        self.bottom_bug_button.setGeometry(QtCore.QRect(250, 8, 30, 30))
        self.bottom_bug_button.setStyleSheet("QPushButton:hover {\n"
                                             "                background-color: #696969;}\n"
                                             "            QPushButton {\n"
                                             "                border-style: none;\n"
                                             "                color: black;}")
        self.bottom_bug_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(bottom_bug_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bottom_bug_button.setIcon(icon1)
        self.bottom_bug_button.setIconSize(QtCore.QSize(24, 24))
        self.bottom_logo_label = QtWidgets.QLabel(parent=self.bottom_widget)
        self.bottom_logo_label.setGeometry(QtCore.QRect(10, 8, 140, 30))
        self.bottom_logo_label.setText("")
        self.bottom_logo_label.setPixmap(QtGui.QPixmap(bottom_logo_icon_path))
        self.bottom_logo_label.setScaledContents(True)

    def showMenu_ui(self):
        click_pos = QtGui.QCursor.pos()
        menu_width = self.my_menu_ui.width()
        menu_height = self.my_menu_ui.height()
        menu_pos = click_pos - QtCore.QPoint(menu_width, menu_height)
        self.my_menu_ui.setGeometry(
            menu_pos.x(), menu_pos.y(), menu_width, menu_height)
        self.my_menu_ui.show()

    def switchChanged(self):
        self.control_toggle_button.setEnabled(False)

        if self.control_toggle_button.toggled:
            sender = "switch_opened"
            self.my_tray_app_ui.setIcon(QtGui.QIcon(self.active_icon_path))
            redirection_operations.start_server()
        else:
            sender = "switch_closed"
            self.my_tray_app_ui.setIcon(QtGui.QIcon(self.pasive_icon_path))
            redirection_operations.stop_server()

        blocking_operations.block_unblock(control_toggle_button=self.control_toggle_button,
                                          selected_blocked_item_detail=None, sender=sender,
                                          fillBlockedList=self.my_pref_ui.my_stacked_widget.my_mal_data_page.fillMalList)
