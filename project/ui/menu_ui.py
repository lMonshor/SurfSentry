from PyQt6 import QtCore, QtWidgets


class uiMenu(QtWidgets.QWidget):
    def __init__(self,my_pref_ui):
        self.my_pref_ui = my_pref_ui
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("menu_ui")
        self.setFixedSize(150, 90)
        self.setWindowFlags(QtCore.Qt.WindowType.Popup |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 148, 90))
        self.frame.setStyleSheet("border: 1px solid white;")
        self.frame.setObjectName("frame")
        self.setStyleSheet("background-color:black")
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("background-color:black")
        self.menu_preferences_button = QtWidgets.QPushButton(self)
        self.menu_preferences_button.setGeometry(QtCore.QRect(1, 1, 146, 28))
        self.menu_preferences_button.setText("Preferences")
        self.menu_preferences_button.setStyleSheet("QPushButton:hover {\n"
                                                   "    background-color:rgb(41, 49, 50);\n"
                                                   "}\n"
                                                   "QPushButton {\n"
                                                   "    border-style: none;\n"
                                                   "    color:white;\n"
                                                   "}")
        self.menu_preferences_button.clicked.connect(self.showPreferences_ui)
        self.menu_preferences_button.setObjectName("menu_preferences_button")
        self.menu_about_button = QtWidgets.QPushButton(self)
        self.menu_about_button.setGeometry(QtCore.QRect(1, 31, 146, 28))
        self.menu_about_button.setText("About Me")
        self.menu_about_button.setStyleSheet("QPushButton:hover {\n"
                                             "    background-color:rgb(41, 49, 50);\n"
                                             "}\n"
                                             "QPushButton {\n"
                                             "    border-style: none;\n"
                                             "    color:white;\n"
                                             "}")
        self.menu_about_button.setObjectName("menu_about_button")
        self.menu_exit_button = QtWidgets.QPushButton(self)
        self.menu_exit_button.setGeometry(QtCore.QRect(1, 61, 146, 28))
        self.menu_exit_button.setText("Exit")
        self.menu_exit_button.setStyleSheet("QPushButton:hover {\n"
                                            "    background-color:rgb(41, 49, 50);\n"
                                            "}\n"
                                            "QPushButton {\n"
                                            "    border-style: none;\n"
                                            "    color:white;\n"
                                            "}")
        self.menu_exit_button.setObjectName("menu_exit_button")
        self.menu_exit_button.clicked.connect(QtWidgets.QApplication.quit)
        self.first_qframe_hline = QtWidgets.QFrame(self)
        self.first_qframe_hline.setGeometry(QtCore.QRect(20, 31, 108, 1))
        self.first_qframe_hline.setStyleSheet("QFrame{\n"
                                              "border:none;\n"
                                              "background:white;\n"
                                              "}")
        self.first_qframe_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.first_qframe_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.first_qframe_hline.setLineWidth(1)
        self.first_qframe_hline.setMidLineWidth(0)
        self.first_qframe_hline.setObjectName("first_qframe_hline")
        self.second_qframe_hline = QtWidgets.QFrame(self)
        self.second_qframe_hline.setGeometry(QtCore.QRect(20, 61, 108, 1))
        self.second_qframe_hline.setStyleSheet("QFrame{\n"
                                               "border:none;\n"
                                               "background:white;\n"
                                               "}")
        self.second_qframe_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.second_qframe_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.second_qframe_hline.setLineWidth(1)
        self.second_qframe_hline.setMidLineWidth(0)
        self.second_qframe_hline.setObjectName("second_qframe_hline")

    def showPreferences_ui(self):
        if not self.my_pref_ui.isVisible():
            self.my_pref_ui.hide()
            self.my_pref_ui.show()
        else:
            self.my_pref_ui.hide()