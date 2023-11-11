from PyQt6 import QtCore, QtGui, QtWidgets
from styles.menu_widget_sytle import menu_button_style


class MenuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(171,529)
        self.setStyleSheet("background-color:#393E46;")
    
        self.menu_button_vlayout_widget = QtWidgets.QWidget(parent=self)
        self.menu_button_vlayout_widget.setGeometry(
            QtCore.QRect(0, 30, 171, 241))
        self.menu_button_vlayout = QtWidgets.QVBoxLayout(
            self.menu_button_vlayout_widget)
        self.menu_button_vlayout.setContentsMargins(0, 0, 0, 0)
        self.menu_button_vlayout.setSpacing(0)
        
        self.menu_gen_button = QtWidgets.QRadioButton(
            parent=self.menu_button_vlayout_widget)
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
        self.menu_gen_button.setStyleSheet(menu_button_style.menu_button_style)
        self.menu_gen_button.setChecked(True)
        self.menu_button_vlayout.addWidget(self.menu_gen_button)
        
        self.menu_md_button = QtWidgets.QRadioButton(
            parent=self.menu_button_vlayout_widget)
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
        self.menu_md_button.setStyleSheet(menu_button_style.menu_button_style)
        self.menu_md_button.setChecked(False)
        self.menu_button_vlayout.addWidget(self.menu_md_button)
        
        self.menu_bd_button = QtWidgets.QRadioButton(
            parent=self.menu_button_vlayout_widget)
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
        self.menu_bd_button.setStyleSheet(menu_button_style.menu_button_style)
        self.menu_bd_button.setChecked(False)
        self.menu_button_vlayout.addWidget(self.menu_bd_button)
        
        self.menu_fb_button = QtWidgets.QRadioButton(
            parent=self.menu_button_vlayout_widget)
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
        self.menu_fb_button.setStyleSheet(menu_button_style.menu_button_style)
        self.menu_fb_button.setChecked(False)
        self.menu_button_vlayout.addWidget(self.menu_fb_button)
        
        self.menu_ab_button = QtWidgets.QRadioButton(
            parent=self.menu_button_vlayout_widget)
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
        self.menu_ab_button.setStyleSheet(menu_button_style.menu_button_style)
        self.menu_ab_button.setChecked(False)
        self.menu_button_vlayout.addWidget(self.menu_ab_button)
        
        self.menu_version_label = QtWidgets.QLabel(parent=self)
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
        
        self.menu_gen_button.setText("General")
        self.menu_md_button.setText("Malicious Data")
        self.menu_bd_button.setText("Blocked Data")
        self.menu_fb_button.setText("Feedback")
        self.menu_ab_button.setText("About")
        self.menu_version_label.setText("Version 2023.10.1")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = MenuWidget()
    main_window.show()

    sys.exit(app.exec())
