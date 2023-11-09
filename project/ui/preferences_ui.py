from PyQt6 import QtCore, QtGui, QtWidgets
from db import db_operations
from features import methods, blocking_operations
from styles import md_styles, bd_styles
import os


class uiPreferences(QtWidgets.QMainWindow):
    def __init__(self):
        self.my_tray_app_ui = None
        self.my_menu_ui = None
        self.my_update_data_worker = None
        self.my_loading_ui = None
        self.my_information_ui = None

        super().__init__()
        self.initUI()

    def initUI(self):
        single_right_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\assets', 'single_right_logo.png')
        double_right_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\assets', 'double_right_logo.png')
        single_left_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\assets', 'single_left_logo.png')
        double_left_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\assets', 'double_left_logo.png')
        add_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\assets', 'add_logo.png')
        trash_icon_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '..\\assets', 'trash_logo.png')
        self.setObjectName("MainWindow")
        self.resize(940, 528)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(940, 528))
        self.setMaximumSize(QtCore.QSize(940, 528))
        self.centralwidget = QtWidgets.QWidget(parent=self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(940, 528))
        self.centralwidget.setMaximumSize(QtCore.QSize(940, 528))
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 941, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_page = QtWidgets.QWidget(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.menu_page.sizePolicy().hasHeightForWidth())
        self.menu_page.setSizePolicy(sizePolicy)
        self.menu_page.setMinimumSize(QtCore.QSize(0, 0))
        self.menu_page.setMaximumSize(QtCore.QSize(300, 999))
        self.menu_page.setStyleSheet("background-color:#393E46;")
        self.menu_page.setObjectName("menu_page")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.menu_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 171, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vmenu_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vmenu_layout.setContentsMargins(0, 0, 0, 0)
        self.vmenu_layout.setSpacing(0)
        self.vmenu_layout.setObjectName("vmenu_layout")
        self.menu_gen_button = QtWidgets.QRadioButton(
            parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.menu_gen_button.sizePolicy().hasHeightForWidth())
        self.menu_gen_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.menu_gen_button.setFont(font)
        self.menu_gen_button.setStyleSheet("QRadioButton {\n"
                                           "    border: none;\n"
                                           "    color: white;\n"
                                           "}\n"
                                           "QRadioButton:hover {\n"
                                           "    background-color: #DDDDDD;\n"
                                           "    color: #0f0f0f;\n"
                                           "}\n"
                                           "QRadioButton::indicator {\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "\n"
                                           "QRadioButton::indicator:checked {\n"
                                           "     border-left: 6px solid #4088D6;\n"
                                           "}\n"
                                           "")
        self.menu_gen_button.setChecked(True)
        self.menu_gen_button.setObjectName("menu_gen_button")
        self.vmenu_layout.addWidget(self.menu_gen_button)
        self.menu_md_button = QtWidgets.QRadioButton(
            parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.menu_md_button.sizePolicy().hasHeightForWidth())
        self.menu_md_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.menu_md_button.setFont(font)
        self.menu_md_button.setStyleSheet("QRadioButton {\n"
                                          "    border: none;\n"
                                          "    color: white;\n"
                                          "}\n"
                                          "QRadioButton:hover {\n"
                                          "    background-color: #DDDDDD;\n"
                                          "    color: #0f0f0f;\n"
                                          "}\n"
                                          "QRadioButton::indicator {\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QRadioButton::indicator:checked {\n"
                                          "     border-left: 6px solid #4088D6;\n"
                                          "}\n"
                                          "")
        self.menu_md_button.setChecked(False)
        self.menu_md_button.setObjectName("menu_md_button")
        self.vmenu_layout.addWidget(self.menu_md_button)
        self.menu_bd_button = QtWidgets.QRadioButton(
            parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.menu_bd_button.sizePolicy().hasHeightForWidth())
        self.menu_bd_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.menu_bd_button.setFont(font)
        self.menu_bd_button.setStyleSheet("QRadioButton {\n"
                                          "    border: none;\n"
                                          "    color: white;\n"
                                          "}\n"
                                          "QRadioButton:hover {\n"
                                          "    background-color: #DDDDDD;\n"
                                          "    color: #0f0f0f;\n"
                                          "}\n"
                                          "QRadioButton::indicator {\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QRadioButton::indicator:checked {\n"
                                          "     border-left: 6px solid #4088D6;\n"
                                          "}\n"
                                          "")
        self.menu_bd_button.setChecked(False)
        self.menu_bd_button.setObjectName("menu_bd_button")
        self.vmenu_layout.addWidget(self.menu_bd_button)
        self.menu_fb_button = QtWidgets.QRadioButton(
            parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.menu_fb_button.sizePolicy().hasHeightForWidth())
        self.menu_fb_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.menu_fb_button.setFont(font)
        self.menu_fb_button.setStyleSheet("QRadioButton {\n"
                                          "    border: none;\n"
                                          "    color: white;\n"
                                          "}\n"
                                          "QRadioButton:hover {\n"
                                          "    background-color: #DDDDDD;\n"
                                          "    color: #0f0f0f;\n"
                                          "}\n"
                                          "QRadioButton::indicator {\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QRadioButton::indicator:checked {\n"
                                          "     border-left: 6px solid #4088D6;\n"
                                          "}\n"
                                          "")
        self.menu_fb_button.setChecked(False)
        self.menu_fb_button.setObjectName("menu_fb_button")
        self.vmenu_layout.addWidget(self.menu_fb_button)
        self.menu_ab_button = QtWidgets.QRadioButton(
            parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.menu_ab_button.sizePolicy().hasHeightForWidth())
        self.menu_ab_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.menu_ab_button.setFont(font)
        self.menu_ab_button.setStyleSheet("QRadioButton {\n"
                                          "    border: none;\n"
                                          "    color: white;\n"
                                          "}\n"
                                          "QRadioButton:hover {\n"
                                          "    background-color: #DDDDDD;\n"
                                          "    color: #0f0f0f;\n"
                                          "}\n"
                                          "QRadioButton::indicator {\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QRadioButton::indicator:checked {\n"
                                          "     border-left: 6px solid #4088D6;\n"
                                          "}\n"
                                          "")
        self.menu_ab_button.setChecked(False)
        self.menu_ab_button.setObjectName("menu_ab_button")
        self.vmenu_layout.addWidget(self.menu_ab_button)
        self.menu_version_label = QtWidgets.QLabel(parent=self.menu_page)
        self.menu_version_label.setGeometry(QtCore.QRect(10, 500, 101, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.menu_version_label.sizePolicy().hasHeightForWidth())
        self.menu_version_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.menu_version_label.setFont(font)
        self.menu_version_label.setStyleSheet("color:#777777;")
        self.menu_version_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.menu_version_label.setObjectName("menu_version_label")
        self.horizontalLayout.addWidget(self.menu_page)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.layoutWidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(999, 999))
        self.stackedWidget.setStyleSheet("background-color: #0f0f0f;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.general_page = QtWidgets.QWidget()
        self.general_page.setStyleSheet("")
        self.general_page.setObjectName("general_page")
        self.gen_apply_button = QtWidgets.QPushButton(parent=self.general_page)
        self.gen_apply_button.setEnabled(False)
        self.gen_apply_button.setGeometry(QtCore.QRect(540, 470, 191, 27))
        self.gen_apply_button.setStyleSheet("QPushButton{\n"
                                            "    background-color:#393E46;\n"
                                            "    color: white;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: #DDDDDD;\n"
                                            "    color: #0f0f0f;\n"
                                            "}\n"
                                            "QPushButton:disabled { \n"
                                            "    background-color: #101112; \n"
                                            "}")
        self.gen_apply_button.setObjectName("gen_apply_button")
        self.gen_second_hline = QtWidgets.QFrame(parent=self.general_page)
        self.gen_second_hline.setGeometry(QtCore.QRect(48, 332, 672, 1))
        self.gen_second_hline.setStyleSheet("background-color:#393E46;")
        self.gen_second_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gen_second_hline.setLineWidth(0)
        self.gen_second_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.gen_second_hline.setObjectName("gen_second_hline")
        self.gen_first_hline = QtWidgets.QFrame(parent=self.general_page)
        self.gen_first_hline.setGeometry(QtCore.QRect(48, 174, 672, 1))
        self.gen_first_hline.setStyleSheet("background-color:#393E46;")
        self.gen_first_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.gen_first_hline.setLineWidth(0)
        self.gen_first_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.gen_first_hline.setObjectName("gen_first_hline")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.general_page)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 100, 311, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gen_top_glayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gen_top_glayout.setContentsMargins(0, 0, 0, 0)
        self.gen_top_glayout.setHorizontalSpacing(6)
        self.gen_top_glayout.setObjectName("gen_top_glayout")
        self.gen_adapter_cbox = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.gen_adapter_cbox.setObjectName("gen_adapter_cbox")
        self.gen_top_glayout.addWidget(self.gen_adapter_cbox, 1, 2, 1, 1)
        self.gen_ip_title = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.gen_ip_title.setFont(font)
        self.gen_ip_title.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.gen_ip_title.setStyleSheet("color:white;")
        self.gen_ip_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                       QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gen_ip_title.setObjectName("gen_ip_title")
        self.gen_top_glayout.addWidget(self.gen_ip_title, 0, 0, 1, 1)
        self.gen_ip_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gen_ip_label.sizePolicy().hasHeightForWidth())
        self.gen_ip_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_ip_label.setFont(font)
        self.gen_ip_label.setStyleSheet("color:#777777;")
        self.gen_ip_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gen_ip_label.setWordWrap(True)
        self.gen_ip_label.setObjectName("gen_ip_label")
        self.gen_top_glayout.addWidget(self.gen_ip_label, 0, 2, 1, 1)
        self.gen_colon3 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_colon3.setFont(font)
        self.gen_colon3.setStyleSheet("color:white;")
        self.gen_colon3.setObjectName("gen_colon3")
        self.gen_top_glayout.addWidget(self.gen_colon3, 1, 1, 1, 1)
        self.gen_adapter_title = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.gen_adapter_title.setFont(font)
        self.gen_adapter_title.setStyleSheet("color:white;")
        self.gen_adapter_title.setObjectName("gen_adapter_title")
        self.gen_top_glayout.addWidget(self.gen_adapter_title, 1, 0, 1, 1)
        self.gen_colon1 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_colon1.setFont(font)
        self.gen_colon1.setStyleSheet("color:white;")
        self.gen_colon1.setObjectName("gen_colon1")
        self.gen_top_glayout.addWidget(self.gen_colon1, 0, 1, 1, 1)
        self.gen_information_title = QtWidgets.QLabel(parent=self.general_page)
        self.gen_information_title.setGeometry(QtCore.QRect(30, 61, 222, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        self.gen_information_title.setFont(font)
        self.gen_information_title.setStyleSheet("color:white;")
        self.gen_information_title.setObjectName("gen_information_title")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.general_page)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 230, 491, 74))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gen_bottom_glayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gen_bottom_glayout.setContentsMargins(0, 0, 0, 0)
        self.gen_bottom_glayout.setHorizontalSpacing(6)
        self.gen_bottom_glayout.setObjectName("gen_bottom_glayout")
        self.gen_last_upt_title = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.gen_last_upt_title.setFont(font)
        self.gen_last_upt_title.setStyleSheet("color:white;")
        self.gen_last_upt_title.setObjectName("gen_last_upt_title")
        self.gen_bottom_glayout.addWidget(self.gen_last_upt_title, 2, 0, 1, 1)
        self.gen_tot_domain_label = QtWidgets.QLabel(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gen_tot_domain_label.sizePolicy().hasHeightForWidth())
        self.gen_tot_domain_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_tot_domain_label.setFont(font)
        self.gen_tot_domain_label.setStyleSheet("color:#777777;")
        self.gen_tot_domain_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gen_tot_domain_label.setWordWrap(True)
        self.gen_tot_domain_label.setObjectName("gen_tot_domain_label")
        self.gen_bottom_glayout.addWidget(
            self.gen_tot_domain_label, 0, 2, 1, 1)
        self.gen_tot_ip_title = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.gen_tot_ip_title.setFont(font)
        self.gen_tot_ip_title.setStyleSheet("color:white;")
        self.gen_tot_ip_title.setObjectName("gen_tot_ip_title")
        self.gen_bottom_glayout.addWidget(self.gen_tot_ip_title, 1, 0, 1, 1)
        self.gen_colon4 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_colon4.setFont(font)
        self.gen_colon4.setStyleSheet("color:white;")
        self.gen_colon4.setObjectName("gen_colon4")
        self.gen_bottom_glayout.addWidget(self.gen_colon4, 0, 1, 1, 1)
        self.gen_colon5 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_colon5.setFont(font)
        self.gen_colon5.setStyleSheet("color:white;")
        self.gen_colon5.setObjectName("gen_colon5")
        self.gen_bottom_glayout.addWidget(self.gen_colon5, 1, 1, 1, 1)
        self.gen_colon6 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_colon6.setFont(font)
        self.gen_colon6.setStyleSheet("color:white;")
        self.gen_colon6.setObjectName("gen_colon6")
        self.gen_bottom_glayout.addWidget(self.gen_colon6, 2, 1, 1, 1)
        self.gen_tot_domain_title = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.gen_tot_domain_title.setFont(font)
        self.gen_tot_domain_title.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.gen_tot_domain_title.setStyleSheet("color:white;")
        self.gen_tot_domain_title.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gen_tot_domain_title.setObjectName("gen_tot_domain_title")
        self.gen_bottom_glayout.addWidget(
            self.gen_tot_domain_title, 0, 0, 1, 1)
        self.gen_tot_ip_label = QtWidgets.QLabel(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gen_tot_ip_label.sizePolicy().hasHeightForWidth())
        self.gen_tot_ip_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_tot_ip_label.setFont(font)
        self.gen_tot_ip_label.setStyleSheet("color:#777777;")
        self.gen_tot_ip_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gen_tot_ip_label.setWordWrap(True)
        self.gen_tot_ip_label.setObjectName("gen_tot_ip_label")
        self.gen_bottom_glayout.addWidget(self.gen_tot_ip_label, 1, 2, 1, 1)
        self.gen_last_upt_label = QtWidgets.QLabel(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gen_last_upt_label.sizePolicy().hasHeightForWidth())
        self.gen_last_upt_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.gen_last_upt_label.setFont(font)
        self.gen_last_upt_label.setStyleSheet("color:#777777;")
        self.gen_last_upt_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.gen_last_upt_label.setWordWrap(True)
        self.gen_last_upt_label.setObjectName("gen_last_upt_label")
        self.gen_bottom_glayout.addWidget(self.gen_last_upt_label, 2, 2, 1, 1)
        self.gen_mal_inf_title = QtWidgets.QLabel(parent=self.general_page)
        self.gen_mal_inf_title.setGeometry(QtCore.QRect(30, 190, 403, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        self.gen_mal_inf_title.setFont(font)
        self.gen_mal_inf_title.setStyleSheet("color:white;")
        self.gen_mal_inf_title.setObjectName("gen_mal_inf_title")
        self.stackedWidget.addWidget(self.general_page)
        self.mal_data_page = QtWidgets.QWidget()
        self.mal_data_page.setStyleSheet("")
        self.mal_data_page.setObjectName("mal_data_page")
        self.md_detail_title = QtWidgets.QLabel(parent=self.mal_data_page)
        self.md_detail_title.setGeometry(QtCore.QRect(320, 120, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.md_detail_title.setFont(font)
        self.md_detail_title.setStyleSheet("color:white;")
        self.md_detail_title.setObjectName("md_detail_title")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.mal_data_page)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(330, 150, 431, 127))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.md_top_glayout = QtWidgets.QGridLayout(self.formLayoutWidget_3)
        self.md_top_glayout.setContentsMargins(0, 0, 0, 0)
        self.md_top_glayout.setSpacing(6)
        self.md_top_glayout.setObjectName("md_top_glayout")
        self.md_detail_type_label = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_detail_type_label.sizePolicy().hasHeightForWidth())
        self.md_detail_type_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_type_label.setFont(font)
        self.md_detail_type_label.setStyleSheet("color:#777777;")
        self.md_detail_type_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.md_detail_type_label.setText("")
        self.md_detail_type_label.setObjectName("md_detail_type_label")
        self.md_top_glayout.addWidget(self.md_detail_type_label, 1, 2, 1, 1)
        self.md_detail_colon3 = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon3.setFont(font)
        self.md_detail_colon3.setStyleSheet("color:white;")
        self.md_detail_colon3.setObjectName("md_detail_colon3")
        self.md_top_glayout.addWidget(self.md_detail_colon3, 1, 1, 1, 1)
        self.md_detail_date_label = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_detail_date_label.sizePolicy().hasHeightForWidth())
        self.md_detail_date_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_date_label.setFont(font)
        self.md_detail_date_label.setStyleSheet("color:#777777;")
        self.md_detail_date_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.md_detail_date_label.setText("")
        self.md_detail_date_label.setObjectName("md_detail_date_label")
        self.md_top_glayout.addWidget(self.md_detail_date_label, 3, 2, 1, 1)
        self.md_detail_type_title = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_type_title.setFont(font)
        self.md_detail_type_title.setStyleSheet("color:white;")
        self.md_detail_type_title.setObjectName("md_detail_type_title")
        self.md_top_glayout.addWidget(self.md_detail_type_title, 2, 0, 1, 1)
        self.md_detail_colon4 = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon4.setFont(font)
        self.md_detail_colon4.setStyleSheet("color:white;")
        self.md_detail_colon4.setObjectName("md_detail_colon4")
        self.md_top_glayout.addWidget(self.md_detail_colon4, 2, 1, 1, 1)
        self.md_detail_source_label = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_detail_source_label.sizePolicy().hasHeightForWidth())
        self.md_detail_source_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_source_label.setFont(font)
        self.md_detail_source_label.setStyleSheet("color:#777777;")
        self.md_detail_source_label.setFrameShape(
            QtWidgets.QFrame.Shape.NoFrame)
        self.md_detail_source_label.setText("")
        self.md_detail_source_label.setObjectName("md_detail_source_label")
        self.md_top_glayout.addWidget(self.md_detail_source_label, 2, 2, 1, 1)
        self.md_detail_colon6 = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon6.setFont(font)
        self.md_detail_colon6.setStyleSheet("color:white;")
        self.md_detail_colon6.setObjectName("md_detail_colon6")
        self.md_top_glayout.addWidget(self.md_detail_colon6, 4, 1, 1, 1)
        self.md_detail_colon5 = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon5.setFont(font)
        self.md_detail_colon5.setStyleSheet("color:white;")
        self.md_detail_colon5.setObjectName("md_detail_colon5")
        self.md_top_glayout.addWidget(self.md_detail_colon5, 3, 1, 1, 1)
        self.md_detail_date_title = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_date_title.setFont(font)
        self.md_detail_date_title.setStyleSheet("color:white;")
        self.md_detail_date_title.setObjectName("md_detail_date_title")
        self.md_top_glayout.addWidget(self.md_detail_date_title, 3, 0, 1, 1)
        self.md_detail_source_title = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_source_title.setFont(font)
        self.md_detail_source_title.setStyleSheet("color:white;")
        self.md_detail_source_title.setObjectName("md_detail_source_title")
        self.md_top_glayout.addWidget(self.md_detail_source_title, 1, 0, 1, 1)
        self.md_detail_desc_title = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_desc_title.setFont(font)
        self.md_detail_desc_title.setStyleSheet("color:white;")
        self.md_detail_desc_title.setObjectName("md_detail_desc_title")
        self.md_top_glayout.addWidget(self.md_detail_desc_title, 4, 0, 1, 1)
        self.md_detail_url_title = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_url_title.setFont(font)
        self.md_detail_url_title.setStyleSheet("color:white;")
        self.md_detail_url_title.setObjectName("md_detail_url_title")
        self.md_top_glayout.addWidget(self.md_detail_url_title, 0, 0, 1, 1)
        self.md_detail_colon1 = QtWidgets.QLabel(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon1.setFont(font)
        self.md_detail_colon1.setStyleSheet("color:white;")
        self.md_detail_colon1.setObjectName("md_detail_colon1")
        self.md_top_glayout.addWidget(self.md_detail_colon1, 0, 1, 1, 1)
        self.md_detail_url_label = QtWidgets.QLineEdit(
            parent=self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_url_label.setFont(font)
        self.md_detail_url_label.setStyleSheet("color:#777777;")
        self.md_detail_url_label.setText("")
        self.md_detail_url_label.setFrame(False)
        self.md_detail_url_label.setReadOnly(True)
        self.md_detail_url_label.setObjectName("md_detail_url_label")
        self.md_top_glayout.addWidget(self.md_detail_url_label, 0, 2, 1, 1)
        self.md_threat_level_title = QtWidgets.QLabel(
            parent=self.mal_data_page)
        self.md_threat_level_title.setGeometry(QtCore.QRect(380, 60, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.md_threat_level_title.setFont(font)
        self.md_threat_level_title.setStyleSheet("background-color:#393E46;\n"
                                                 "    color: #EEEEEE;")
        self.md_threat_level_title.setFrameShape(
            QtWidgets.QFrame.Shape.NoFrame)
        self.md_threat_level_title.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.md_threat_level_title.setScaledContents(False)
        self.md_threat_level_title.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.md_threat_level_title.setObjectName("md_threat_level_title")
        self.md_source_button = QtWidgets.QPushButton(
            parent=self.mal_data_page)
        self.md_source_button.setEnabled(False)
        self.md_source_button.setGeometry(QtCore.QRect(450, 490, 191, 27))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.md_source_button.setFont(font)
        self.md_source_button.setStyleSheet("QPushButton{\n"
                                            "    background-color:#393E46;\n"
                                            "    color: white;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: #DDDDDD;\n"
                                            "    color: #0f0f0f;\n"
                                            "}\n"
                                            "QPushButton:disabled { \n"
                                            "    background-color: #101112; \n"
                                            "}")
        self.md_source_button.setObjectName("md_source_button")
        self.md_main_title = QtWidgets.QLabel(parent=self.mal_data_page)
        self.md_main_title.setGeometry(QtCore.QRect(30, 30, 188, 24))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_main_title.sizePolicy().hasHeightForWidth())
        self.md_main_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.md_main_title.setFont(font)
        self.md_main_title.setStyleSheet("color:white;")
        self.md_main_title.setObjectName("md_main_title")
        self.md_data_update_button = QtWidgets.QPushButton(
            parent=self.mal_data_page)
        self.md_data_update_button.setGeometry(QtCore.QRect(70, 490, 191, 27))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.md_data_update_button.setFont(font)
        self.md_data_update_button.setStyleSheet("QPushButton{\n"
                                                 "    background-color:#393E46;\n"
                                                 "    color: white;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "    background-color: #DDDDDD;\n"
                                                 "    color: #0f0f0f;\n"
                                                 "}\n"
                                                 "QPushButton:disabled { \n"
                                                 "    background-color: #101112; \n"
                                                 "}")
        self.md_data_update_button.setFlat(False)
        self.md_data_update_button.setObjectName("md_data_update_button")
        self.md_second_hline = QtWidgets.QFrame(parent=self.mal_data_page)
        self.md_second_hline.setGeometry(QtCore.QRect(330, 480, 421, 1))
        self.md_second_hline.setStyleSheet("background-color:#393E46;")
        self.md_second_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.md_second_hline.setLineWidth(0)
        self.md_second_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.md_second_hline.setObjectName("md_second_hline")
        self.md_mal_data_list = QtWidgets.QListWidget(
            parent=self.mal_data_page)
        self.md_mal_data_list.setGeometry(QtCore.QRect(30, 60, 281, 421))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_mal_data_list.sizePolicy().hasHeightForWidth())
        self.md_mal_data_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.md_mal_data_list.setFont(font)
        self.md_mal_data_list.setToolTipDuration(-1)
        self.md_mal_data_list.setStyleSheet(md_styles.mal_data_list_style)
        self.md_mal_data_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.md_mal_data_list.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.md_mal_data_list.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.md_mal_data_list.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.md_mal_data_list.setAutoScroll(True)
        self.md_mal_data_list.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.md_mal_data_list.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.md_mal_data_list.setWordWrap(True)
        self.md_mal_data_list.setSelectionRectVisible(True)
        self.md_mal_data_list.setObjectName("md_mal_data_list")
        self.md_detail_desc_label = QtWidgets.QLabel(parent=self.mal_data_page)
        self.md_detail_desc_label.setGeometry(QtCore.QRect(350, 290, 391, 161))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_detail_desc_label.sizePolicy().hasHeightForWidth())
        self.md_detail_desc_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_desc_label.setFont(font)
        self.md_detail_desc_label.setContextMenuPolicy(
            QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.md_detail_desc_label.setStyleSheet("color:#777777;\n"
                                                "border:none;")
        self.md_detail_desc_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.md_detail_desc_label.setText("")
        self.md_detail_desc_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.md_detail_desc_label.setWordWrap(True)
        self.md_detail_desc_label.setObjectName("md_detail_desc_label")
        self.md_first_hline = QtWidgets.QFrame(parent=self.mal_data_page)
        self.md_first_hline.setGeometry(QtCore.QRect(330, 106, 421, 1))
        self.md_first_hline.setStyleSheet("background-color:#393E46;")
        self.md_first_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.md_first_hline.setLineWidth(0)
        self.md_first_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.md_first_hline.setObjectName("md_first_hline")
        self.stackedWidget.addWidget(self.mal_data_page)
        self.blocked_data_page = QtWidgets.QWidget()
        self.blocked_data_page.setObjectName("blocked_data_page")
        self.bd_blocked_list = QtWidgets.QListWidget(
            parent=self.blocked_data_page)
        self.bd_blocked_list.setGeometry(QtCore.QRect(30, 59, 281, 331))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bd_blocked_list.sizePolicy().hasHeightForWidth())
        self.bd_blocked_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bd_blocked_list.setFont(font)
        self.bd_blocked_list.setStyleSheet(bd_styles.blocked_style)
        self.bd_blocked_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bd_blocked_list.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.bd_blocked_list.setLineWidth(2)
        self.bd_blocked_list.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.bd_blocked_list.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.bd_blocked_list.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.bd_blocked_list.setSelectionRectVisible(True)
        self.bd_blocked_list.setObjectName("bd_blocked_list")
        self.bd_inf_title = QtWidgets.QLabel(parent=self.blocked_data_page)
        self.bd_inf_title.setGeometry(QtCore.QRect(30, 410, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.bd_inf_title.setFont(font)
        self.bd_inf_title.setStyleSheet("color:white;")
        self.bd_inf_title.setObjectName("bd_inf_title")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(
            parent=self.blocked_data_page)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(40, 440, 701, 75))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.bd_left_glayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.bd_left_glayout.setContentsMargins(0, 0, 0, 0)
        self.bd_left_glayout.setObjectName("bd_left_glayout")
        self.bd_op_time_label = QtWidgets.QLabel(
            parent=self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bd_op_time_label.sizePolicy().hasHeightForWidth())
        self.bd_op_time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_op_time_label.setFont(font)
        self.bd_op_time_label.setStyleSheet("color:#777777;")
        self.bd_op_time_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bd_op_time_label.setText("")
        self.bd_op_time_label.setObjectName("bd_op_time_label")
        self.bd_left_glayout.addWidget(self.bd_op_time_label, 1, 2, 1, 1)
        self.bd_url_title = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.bd_url_title.setFont(font)
        self.bd_url_title.setStyleSheet("color:white;")
        self.bd_url_title.setObjectName("bd_url_title")
        self.bd_left_glayout.addWidget(self.bd_url_title, 0, 0, 1, 1)
        self.bd_colon3 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_colon3.setFont(font)
        self.bd_colon3.setStyleSheet("color:white;")
        self.bd_colon3.setObjectName("bd_colon3")
        self.bd_left_glayout.addWidget(self.bd_colon3, 2, 1, 1, 1)
        self.bd_current_stat_title = QtWidgets.QLabel(
            parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.bd_current_stat_title.setFont(font)
        self.bd_current_stat_title.setStyleSheet("color:white;")
        self.bd_current_stat_title.setObjectName("bd_current_stat_title")
        self.bd_left_glayout.addWidget(self.bd_current_stat_title, 2, 0, 1, 1)
        self.bd_op_time_title = QtWidgets.QLabel(
            parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.bd_op_time_title.setFont(font)
        self.bd_op_time_title.setStyleSheet("color:white;")
        self.bd_op_time_title.setObjectName("bd_op_time_title")
        self.bd_left_glayout.addWidget(self.bd_op_time_title, 1, 0, 1, 1)
        self.bd_colon1 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_colon1.setFont(font)
        self.bd_colon1.setStyleSheet("color:white;")
        self.bd_colon1.setObjectName("bd_colon1")
        self.bd_left_glayout.addWidget(self.bd_colon1, 0, 1, 1, 1)
        self.bd_colon2 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_colon2.setFont(font)
        self.bd_colon2.setStyleSheet("color:white;")
        self.bd_colon2.setObjectName("bd_colon2")
        self.bd_left_glayout.addWidget(self.bd_colon2, 1, 1, 1, 1)
        self.bd_current_stat_label = QtWidgets.QLabel(
            parent=self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bd_current_stat_label.sizePolicy().hasHeightForWidth())
        self.bd_current_stat_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_current_stat_label.setFont(font)
        self.bd_current_stat_label.setStyleSheet("color:#777777;")
        self.bd_current_stat_label.setFrameShape(
            QtWidgets.QFrame.Shape.NoFrame)
        self.bd_current_stat_label.setText("")
        self.bd_current_stat_label.setObjectName("bd_current_stat_label")
        self.bd_left_glayout.addWidget(self.bd_current_stat_label, 2, 2, 1, 1)
        self.bd_url_label = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_url_label.setFont(font)
        self.bd_url_label.setStyleSheet("color:#777777;")
        self.bd_url_label.setFrame(False)
        self.bd_url_label.setReadOnly(True)
        self.bd_url_label.setObjectName("bd_url_label")
        self.bd_left_glayout.addWidget(self.bd_url_label, 0, 2, 1, 1)
        self.bd_blocked_list_title = QtWidgets.QLabel(
            parent=self.blocked_data_page)
        self.bd_blocked_list_title.setGeometry(QtCore.QRect(30, 30, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.bd_blocked_list_title.setFont(font)
        self.bd_blocked_list_title.setStyleSheet("color:white;")
        self.bd_blocked_list_title.setObjectName("bd_blocked_list_title")
        self.bd_unblocked_list_title = QtWidgets.QLabel(
            parent=self.blocked_data_page)
        self.bd_unblocked_list_title.setGeometry(
            QtCore.QRect(457, 30, 153, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.bd_unblocked_list_title.setFont(font)
        self.bd_unblocked_list_title.setStyleSheet("color:white;")
        self.bd_unblocked_list_title.setObjectName("bd_unblocked_list_title")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(
            parent=self.blocked_data_page)
        self.verticalLayoutWidget_3.setGeometry(
            QtCore.QRect(340, 130, 91, 176))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.bd_buttons_vlayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.bd_buttons_vlayout.setContentsMargins(0, 0, 0, 0)
        self.bd_buttons_vlayout.setObjectName("bd_buttons_vlayout")
        self.bd_unblock_sel_data_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_unblock_sel_data_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_unblock_sel_data_button.setFont(font)
        self.bd_unblock_sel_data_button.setStyleSheet("QPushButton{\n"
                                                      "    background-color:#393E46;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    background-color: #DDDDDD;\n"
                                                      "}\n"
                                                      "QPushButton:disabled { \n"
                                                      "    background-color: #101112; \n"
                                                      "}")
        self.bd_unblock_sel_data_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(single_right_icon_path),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_unblock_sel_data_button.setIcon(icon)
        self.bd_unblock_sel_data_button.setFlat(False)
        self.bd_unblock_sel_data_button.setObjectName(
            "bd_unblock_sel_data_button")
        self.bd_buttons_vlayout.addWidget(self.bd_unblock_sel_data_button)
        self.bd_unblock_all_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_unblock_all_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_unblock_all_button.setFont(font)
        self.bd_unblock_all_button.setStyleSheet("QPushButton{\n"
                                                 "    background-color:#393E46;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "    background-color: #DDDDDD;\n"
                                                 "}\n"
                                                 "QPushButton:disabled { \n"
                                                 "    background-color: #101112; \n"
                                                 "}")
        self.bd_unblock_all_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(double_right_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_unblock_all_button.setIcon(icon1)
        self.bd_unblock_all_button.setFlat(False)
        self.bd_unblock_all_button.setObjectName("bd_unblock_all_button")
        self.bd_buttons_vlayout.addWidget(self.bd_unblock_all_button)
        self.bd_block_sel_data_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_block_sel_data_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_block_sel_data_button.setFont(font)
        self.bd_block_sel_data_button.setStyleSheet("QPushButton{\n"
                                                    "    background-color:#393E46;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    background-color: #DDDDDD;\n"
                                                    "}\n"
                                                    "QPushButton:disabled { \n"
                                                    "    background-color: #101112; \n"
                                                    "}")
        self.bd_block_sel_data_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(single_left_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_block_sel_data_button.setIcon(icon2)
        self.bd_block_sel_data_button.setFlat(False)
        self.bd_block_sel_data_button.setObjectName("bd_block_sel_data_button")
        self.bd_buttons_vlayout.addWidget(self.bd_block_sel_data_button)
        self.bd_block_all_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_block_all_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_block_all_button.setFont(font)
        self.bd_block_all_button.setStyleSheet("QPushButton{\n"
                                               "    background-color:#393E46;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #DDDDDD;\n"
                                               "}\n"
                                               "QPushButton:disabled { \n"
                                               "    background-color: #101112; \n"
                                               "}")
        self.bd_block_all_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(double_left_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_block_all_button.setIcon(icon3)
        self.bd_block_all_button.setFlat(False)
        self.bd_block_all_button.setObjectName("bd_block_all_button")
        self.bd_buttons_vlayout.addWidget(self.bd_block_all_button)
        self.bd_add_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_add_button.setFont(font)
        self.bd_add_button.setStyleSheet("QPushButton{\n"
                                         "    background-color:#393E46;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "    background-color: #DDDDDD;\n"
                                         "}\n"
                                         "QPushButton:disabled { \n"
                                         "    background-color: #101112; \n"
                                         "}")
        self.bd_add_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(add_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_add_button.setIcon(icon4)
        self.bd_add_button.setFlat(False)
        self.bd_add_button.setObjectName("bd_add_button")
        self.bd_buttons_vlayout.addWidget(self.bd_add_button)
        self.bd_delete_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_delete_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_delete_button.setFont(font)
        self.bd_delete_button.setStyleSheet("QPushButton{\n"
                                            "    background-color:#393E46;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: #DDDDDD;\n"
                                            "}\n"
                                            "QPushButton:disabled { \n"
                                            "    background-color: #101112; \n"
                                            "}")
        self.bd_delete_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(trash_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_delete_button.setIcon(icon5)
        self.bd_delete_button.setFlat(False)
        self.bd_delete_button.setObjectName("bd_delete_button")
        self.bd_buttons_vlayout.addWidget(self.bd_delete_button)
        self.bd_unblocked_list = QtWidgets.QListWidget(
            parent=self.blocked_data_page)
        self.bd_unblocked_list.setGeometry(QtCore.QRect(457, 59, 281, 331))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bd_unblocked_list.sizePolicy().hasHeightForWidth())
        self.bd_unblocked_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bd_unblocked_list.setFont(font)
        self.bd_unblocked_list.setStyleSheet(bd_styles.unblocked_list_style)
        self.bd_unblocked_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bd_unblocked_list.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.bd_unblocked_list.setLineWidth(10)
        self.bd_unblocked_list.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.bd_unblocked_list.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.bd_unblocked_list.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.bd_unblocked_list.setSelectionRectVisible(True)
        self.bd_unblocked_list.setObjectName("bd_unblocked_list")
        self.bd_first_hline = QtWidgets.QFrame(parent=self.blocked_data_page)
        self.bd_first_hline.setGeometry(QtCore.QRect(48, 400, 672, 1))
        self.bd_first_hline.setStyleSheet("background-color:#393E46;")
        self.bd_first_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bd_first_hline.setLineWidth(0)
        self.bd_first_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.bd_first_hline.setObjectName("bd_first_hline")
        self.stackedWidget.addWidget(self.blocked_data_page)
        self.feedback_page = QtWidgets.QWidget()
        self.feedback_page.setObjectName("feedback_page")
        self.fb_email_text = QtWidgets.QPlainTextEdit(
            parent=self.feedback_page)
        self.fb_email_text.setGeometry(QtCore.QRect(30, 60, 661, 25))
        self.fb_email_text.setStyleSheet("background-color:#393E46;\n"
                                         "color:white;")
        self.fb_email_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fb_email_text.setObjectName("fb_email_text")
        self.fb_email_title = QtWidgets.QLabel(parent=self.feedback_page)
        self.fb_email_title.setGeometry(QtCore.QRect(30, 35, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fb_email_title.setFont(font)
        self.fb_email_title.setStyleSheet("color:white;")
        self.fb_email_title.setObjectName("fb_email_title")
        self.fb_subject_text = QtWidgets.QPlainTextEdit(
            parent=self.feedback_page)
        self.fb_subject_text.setGeometry(QtCore.QRect(30, 130, 661, 25))
        self.fb_subject_text.setStyleSheet("background-color:#393E46;\n"
                                           "color:white;")
        self.fb_subject_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fb_subject_text.setObjectName("fb_subject_text")
        self.fb_subject_title = QtWidgets.QLabel(parent=self.feedback_page)
        self.fb_subject_title.setGeometry(QtCore.QRect(30, 105, 49, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fb_subject_title.setFont(font)
        self.fb_subject_title.setStyleSheet("color:white;")
        self.fb_subject_title.setObjectName("fb_subject_title")
        self.fb_desc_title = QtWidgets.QLabel(parent=self.feedback_page)
        self.fb_desc_title.setGeometry(QtCore.QRect(30, 175, 75, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fb_desc_title.setFont(font)
        self.fb_desc_title.setStyleSheet("color:white;")
        self.fb_desc_title.setObjectName("fb_desc_title")
        self.fb_desc_text = QtWidgets.QPlainTextEdit(parent=self.feedback_page)
        self.fb_desc_text.setGeometry(QtCore.QRect(30, 200, 661, 221))
        self.fb_desc_text.setStyleSheet("background-color:#393E46;\n"
                                        "color:white;")
        self.fb_desc_text.setObjectName("fb_desc_text")
        self.fb_submit_fb_button = QtWidgets.QPushButton(
            parent=self.feedback_page)
        self.fb_submit_fb_button.setGeometry(QtCore.QRect(30, 470, 181, 26))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.fb_submit_fb_button.setFont(font)
        self.fb_submit_fb_button.setStyleSheet("QPushButton{\n"
                                               "    background-color:#393E46;\n"
                                               "    color: white;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #DDDDDD;\n"
                                               "    color: #0f0f0f;\n"
                                               "}\n"
                                               "QPushButton:disabled { \n"
                                               "    background-color: #101112; \n"
                                               "}")
        self.fb_submit_fb_button.setFlat(False)
        self.fb_submit_fb_button.setObjectName("fb_submit_fb_button")
        self.stackedWidget.addWidget(self.feedback_page)
        self.about_page = QtWidgets.QWidget()
        self.about_page.setStyleSheet("")
        self.about_page.setObjectName("about_page")
        self.ab_github_button = QtWidgets.QPushButton(parent=self.about_page)
        self.ab_github_button.setGeometry(QtCore.QRect(540, 470, 191, 27))
        self.ab_github_button.setStyleSheet("QPushButton{\n"
                                            "    background-color:#393E46;\n"
                                            "    color: white;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: #DDDDDD;\n"
                                            "    color: #0f0f0f;\n"
                                            "}\n"
                                            "QPushButton:disabled { \n"
                                            "    background-color: #101112; \n"
                                            "}")
        self.ab_github_button.setObjectName("ab_github_button")
        self.ab_first_desc_text = QtWidgets.QPlainTextEdit(
            parent=self.about_page)
        self.ab_first_desc_text.setGeometry(QtCore.QRect(40, 80, 671, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ab_first_desc_text.setFont(font)
        self.ab_first_desc_text.setStyleSheet("background-color:#0f0f0f;\n"
                                              "color:white;\n"
                                              "border:none;")
        self.ab_first_desc_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ab_first_desc_text.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ab_first_desc_text.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.ab_first_desc_text.setReadOnly(True)
        self.ab_first_desc_text.setPlaceholderText("")
        self.ab_first_desc_text.setObjectName("ab_first_desc_text")
        self.ab_main_title = QtWidgets.QLabel(parent=self.about_page)
        self.ab_main_title.setGeometry(QtCore.QRect(30, 40, 124, 36))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(False)
        self.ab_main_title.setFont(font)
        self.ab_main_title.setStyleSheet("color:white;")
        self.ab_main_title.setObjectName("ab_main_title")
        self.ab_second_title = QtWidgets.QLabel(parent=self.about_page)
        self.ab_second_title.setGeometry(QtCore.QRect(30, 180, 229, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.ab_second_title.setFont(font)
        self.ab_second_title.setStyleSheet("color:white;")
        self.ab_second_title.setObjectName("ab_second_title")
        self.ab_second_text = QtWidgets.QPlainTextEdit(parent=self.about_page)
        self.ab_second_text.setGeometry(QtCore.QRect(40, 220, 671, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ab_second_text.setFont(font)
        self.ab_second_text.setStyleSheet("background-color:#0f0f0f;\n"
                                          "color:white;\n"
                                          "border:none;")
        self.ab_second_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ab_second_text.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ab_second_text.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.ab_second_text.setReadOnly(True)
        self.ab_second_text.setPlaceholderText("")
        self.ab_second_text.setObjectName("ab_second_text")
        self.ab_first_hline = QtWidgets.QFrame(parent=self.about_page)
        self.ab_first_hline.setGeometry(QtCore.QRect(48, 350, 672, 1))
        self.ab_first_hline.setStyleSheet("background-color:#393E46;")
        self.ab_first_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ab_first_hline.setLineWidth(0)
        self.ab_first_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.ab_first_hline.setObjectName("ab_first_hline")
        self.stackedWidget.addWidget(self.about_page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 9)
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("MainWindow")
        self.menu_gen_button.setText("General")
        self.menu_md_button.setText("Malicious Data")
        self.menu_bd_button.setText("Blocked Data")
        self.menu_fb_button.setText("Feedback")
        self.menu_ab_button.setText("About")
        self.menu_version_label.setText("Version 2023.10.1")
        self.gen_apply_button.setText("Apply Changes")
        self.gen_ip_title.setText("Public IP")
        self.gen_ip_label.setText("255.255.255.255")
        self.gen_colon3.setText(":")
        self.gen_adapter_title.setText("Current Adapter")
        self.gen_colon1.setText(":")
        self.gen_information_title.setText("General Information")
        self.gen_last_upt_title.setText("Last Update Time")
        self.gen_tot_domain_label.setText("256")
        self.gen_tot_ip_title.setText("Total Number of Malicious IPS")
        self.gen_colon4.setText(":")
        self.gen_colon5.setText(":")
        self.gen_colon6.setText(":")
        self.gen_tot_domain_title.setText("Total Number of Malicious Domains")
        self.gen_tot_ip_label.setText("128")
        self.gen_last_upt_label.setText("2023-10-07 11:08")
        self.gen_mal_inf_title.setText("Received Malicious Data Information")
        self.md_detail_title.setText("Other Information")
        self.md_detail_colon3.setText(":")
        self.md_detail_type_title.setText("Type")
        self.md_detail_colon4.setText(":")
        self.md_detail_colon6.setText(":")
        self.md_detail_colon5.setText(":")
        self.md_detail_date_title.setText("Date")
        self.md_detail_source_title.setText("Source        ")
        self.md_detail_desc_title.setText("Description")
        self.md_detail_url_title.setText("URL             ")
        self.md_detail_colon1.setText(":")
        self.md_threat_level_title.setText("THREAT LEVEL")
        self.md_source_button.setText("USOM Source")
        self.md_main_title.setText("Received Malicious Data")
        self.md_data_update_button.setText("Update Data")
        self.md_mal_data_list.setSortingEnabled(True)
        self.bd_blocked_list.setSortingEnabled(True)
        self.bd_inf_title.setText("Other Information")
        self.bd_url_title.setText("URL")
        self.bd_colon3.setText(":")
        self.bd_current_stat_title.setText("Current Status")
        self.bd_op_time_title.setText("Operation Time")
        self.bd_colon1.setText(":")
        self.bd_colon2.setText(":")
        self.bd_blocked_list_title.setText("Blocked Data List")
        self.bd_unblocked_list_title.setText("Unblocked Data List")
        self.bd_unblocked_list.setSortingEnabled(True)
        self.fb_email_title.setText("Email address")
        self.fb_subject_text.setPlaceholderText("Briefly describe the issue.")
        self.fb_subject_title.setText("Subject")
        self.fb_desc_title.setText("Description")
        self.fb_desc_text.setPlaceholderText(
            "Describe the issue/improvement in as much detail as you can. Include steps to replicate if relevant.")
        self.fb_submit_fb_button.setText("Submit feedback")
        self.ab_github_button.setText("GitHub")
        self.ab_first_desc_text.setPlainText("Surfsentry is a Windows application developed to protect users against malicious websites. It retrieves a list of malicious links from USOM (Ulusal Siber Olaylara Müdahale Merkezi - National Cyber Incident Response Center) and writes them to the hosts file. This ensures a secure internet experience for users.\n"
                                             "\n"
                                             "")
        self.ab_main_title.setText("SurfSentry")
        self.ab_second_title.setText("Blocking CNC Server IPs")
        self.ab_second_text.setPlainText(
            "Surfsentry not only blocks domain connections by writing them to the hosts file, but also identifies IP addresses associated with Command and Control (CNC) servers provided by USOM. It adds firewall rules to block communication with these IPs, providing an additional layer of protection against malicious activity.")

        self.stackedWidget.setCurrentIndex(0)
        self.md_mal_data_list.setCurrentRow(-1)

        self.fb_email_text.textChanged.connect(self.checkPlainTextEdits)
        self.fb_subject_text.textChanged.connect(self.checkPlainTextEdits)
        self.fb_desc_text.textChanged.connect(self.checkPlainTextEdits)
        self.fb_submit_fb_button.setEnabled(False)

        self.md_mal_data_list.itemSelectionChanged.connect(
            lambda: self.fillMalDetails(self.md_mal_data_list.selectedItems()))

        self.bd_blocked_list.itemSelectionChanged.connect(
            lambda: self.fillBlockedDetail(self.bd_blocked_list.selectedItems(), "blocked_list"))

        self.bd_unblocked_list.itemSelectionChanged.connect(
            lambda: self.fillBlockedDetail(self.bd_unblocked_list.selectedItems(), "unblocked_list"))

        self.bd_unblock_all_button.clicked.connect(
            lambda: blocking_operations.block_unblock(selected_blocked_item_detail=None, sender="unblock_all_button", my_loading_ui=self.my_loading_ui, my_information_ui=self.my_information_ui, fillBlockedList=self.fillBlockedList))
        self.bd_block_all_button.clicked.connect(
            lambda: blocking_operations.block_unblock(selected_blocked_item_detail=None, sender="block_all_button", my_loading_ui=self.my_loading_ui, my_information_ui=self.my_information_ui, fillBlockedList=self.fillBlockedList))

        self.md_data_update_button.clicked.connect(
            lambda: self.my_update_data_worker.start())

        self.fb_submit_fb_button.clicked.connect(lambda: methods.send_email_feedback(
            email_address=self.fb_email_text, subject=self.fb_subject_text, description=self.fb_desc_text))

        self.stackedWidget.setCurrentWidget(self.general_page)
        self.menu_gen_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.general_page))
        self.menu_ab_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.about_page))
        self.menu_md_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.mal_data_page))
        self.menu_bd_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.blocked_data_page))
        self.menu_fb_button.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.feedback_page))
        self.ab_github_button.clicked.connect(
            lambda: methods.openCustomWebPage("https://github.com/lMonshor/SurfSentry"))
        QtCore.QMetaObject.connectSlotsByName(self)

    def checkPlainTextEdits(self):
        if not self.fb_email_text.toPlainText() or not self.fb_subject_text.toPlainText() or not self.fb_desc_text.toPlainText():
            self.fb_submit_fb_button.setDisabled(True)
        else:
            self.fb_submit_fb_button.setDisabled(False)

    def fillMalList(self):
        try:
            self.md_mal_data_list.clear()
            mal_urls = db_operations.get_data_by_column_name(
                column_name="url", table_name="malicious_data")
            for row in mal_urls:
                mal_url = QtWidgets.QListWidgetItem(str(row[0]))
                self.md_mal_data_list.addItem(mal_url)
                self.md_mal_data_list.addItem(mal_url)
        except Exception as e:
            print(f"Error fillMalList: {e}")

    def fillMalDetails(self, sel_mal_items):
        try:
            if sel_mal_items:
                sel_mal_item = sel_mal_items[0]
                sel_mal_item_detail = db_operations.get_one_data_detail(
                    column_name="*", condition_column='url', condition_value=sel_mal_item.text(), table_name='malicious_data')
                self.md_source_button.setEnabled(True)
                self.md_source_button.disconnect()
                self.md_source_button.clicked.connect(
                    lambda: methods.openCustomWebPage(sel_mal_item_detail[9]))

                self.md_detail_url_label.setText(sel_mal_item_detail[3])
                self.md_detail_type_label.setText(sel_mal_item_detail[4])
                self.md_detail_desc_label.setText(sel_mal_item_detail[5])
                if sel_mal_item_detail[6] <= 3:
                    self.md_mal_data_list.setStyleSheet(
                        md_styles.low_level_style)
                    self.md_threat_level_title.setText("LOW")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #23B7E5;color:white;")
                elif 4 <= sel_mal_item_detail[6] <= 7:
                    self.md_mal_data_list.setStyleSheet(
                        md_styles.medium_level_style)
                    self.md_threat_level_title.setText("MEDIUM")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #FF902B;color:white;")
                else:
                    self.md_mal_data_list.setStyleSheet(
                        md_styles.high_level_style)
                    self.md_threat_level_title.setText("HIGH")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #F05050;color:white;")
                self.md_detail_source_label.setText(sel_mal_item_detail[7])
                self.md_detail_date_label.setText(sel_mal_item_detail[8])
        except Exception as e:
            print(f"Error fillMalDetails: {e}")

    def fillBlockedList(self):
        try:
            self.bd_blocked_list.clear()
            self.bd_unblocked_list.clear()
            self.bd_blocked_list.clearSelection()
            self.bd_unblocked_list.clearSelection()

            blocked_data = db_operations.get_data_by_column_name(
                column_name="url,current_status", table_name="blocked_data")
            for row in blocked_data:
                blocked_current_state = row[1]
                blocked_url = QtWidgets.QListWidgetItem(str(row[0]))
                if blocked_current_state == "blocked":
                    self.bd_blocked_list.addItem(blocked_url)
                elif blocked_current_state == "unblocked":
                    self.bd_unblocked_list.addItem(blocked_url)
            if self.bd_blocked_list.count() == 0:
                self.bd_block_all_button.setEnabled(True)
                self.bd_unblock_all_button.setEnabled(False)
            elif self.bd_unblocked_list.count() == 0:
                self.bd_unblock_all_button.setEnabled(True)
                self.bd_block_all_button.setEnabled(False)
            elif self.bd_unblocked_list.count() == 0 and self.bd_blocked_list.count() == 0:
                self.bd_unblock_all_button.setEnabled(False)
                self.bd_block_all_button.setEnabled(False)
            else:
                self.bd_unblock_all_button.setEnabled(True)
                self.bd_block_all_button.setEnabled(True)
        except Exception as e:
            print(f"Error fillBlockedList: {e}")

    def fillBlockedDetail(self, selected_blocked_item, sender):
        try:
            if selected_blocked_item:
                selected_blocked_item = selected_blocked_item[0]

                selected_blocked_item_detail = db_operations.custom_query(
                    f'select url, data_type, operation_time, current_status from blocked_data where url = "{selected_blocked_item.text()}"')[0]

                if sender == "blocked_list":
                    self.bd_unblock_sel_data_button.disconnect()
                    self.bd_unblocked_list.clearSelection()
                    self.bd_unblock_sel_data_button.setEnabled(True)
                    self.bd_block_sel_data_button.setEnabled(False)
                    self.bd_unblock_sel_data_button.clicked.connect(
                        lambda: blocking_operations.block_unblock(selected_blocked_item_detail=selected_blocked_item_detail, sender="unblock_button", my_loading_ui=self.my_loading_ui, my_information_ui=self.my_information_ui, fillBlockedList=self.fillBlockedList))
                elif sender == "unblocked_list":
                    self.bd_block_sel_data_button.disconnect()
                    self.bd_blocked_list.clearSelection()
                    self.bd_unblock_sel_data_button.setEnabled(False)
                    self.bd_block_sel_data_button.setEnabled(True)
                    self.bd_block_sel_data_button.clicked.connect(
                        lambda: blocking_operations.block_unblock(selected_blocked_item_detail=selected_blocked_item_detail, sender="block_button", my_loading_ui=self.my_loading_ui, my_information_ui=self.my_information_ui, fillBlockedList=self.fillBlockedList))

                self.bd_url_label.setText(
                    selected_blocked_item_detail[0])
                self.bd_op_time_label.setText(
                    selected_blocked_item_detail[2])
                self.bd_current_stat_label.setText(
                    selected_blocked_item_detail[3])
                if selected_blocked_item_detail[3] == "blocked":
                    self.bd_blocked_list.setStyleSheet(bd_styles.blocked_style)
                    self.bd_current_stat_label.setStyleSheet(
                        "color:#23B7E5;")
                elif selected_blocked_item_detail[3] == "unblocked":
                    self.bd_unblocked_list.setStyleSheet(
                        bd_styles.unblocked_style)
                    self.bd_current_stat_label.setStyleSheet(
                        "color:#F05050;")
            else:
                self.bd_unblock_sel_data_button.setEnabled(False)
                self.bd_block_sel_data_button.setEnabled(False)
        except Exception as e:
            print(f"Error fillBlockedDetail: {e}")
