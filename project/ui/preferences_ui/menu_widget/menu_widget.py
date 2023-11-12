from PyQt6 import QtCore, QtGui, QtWidgets
from ui.components import qlabel_generator,qlayout_qwidget_generator
from styles.preferences_ui_styles.menu_widget_sytles import menu_buttons_style

class MenuWidget(QtWidgets.QWidget):
    BUTTON_FONT = QtGui.QFont("Calibri", 12)
    MENU_WIDGET_STYLE = "background-color:#393E46;"
    MENU_VERSION_STYLE = "#777777"
    MENU_VERSION_FONT = QtGui.QFont("Calibri", 10)
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(171, 529)
        self.setStyleSheet(self.MENU_WIDGET_STYLE)

        self.menu_button_vlayout_widget, self.menu_button_vlayout = qlayout_qwidget_generator.create_vlayout_widget(
            parent=self,geometry=(QtCore.QRect(0, 30, 171, 241)))

        self.menu_gen_button = self.create_radio_button("General", checked=True)
        self.menu_md_button = self.create_radio_button("Malicious Data")
        self.menu_bd_button = self.create_radio_button("Blocked Data")
        self.menu_fb_button = self.create_radio_button("Feedback")
        self.menu_ab_button = self.create_radio_button("About")

        self.menu_version_label = QtWidgets.QLabel(parent=self)


        self.menu_version_label = qlabel_generator.create_label(
            parent=self,
            color=self.MENU_VERSION_STYLE,
            font=self.MENU_VERSION_FONT,
            geometry=(QtCore.QRect(10, 500, 101, 16)),
            text="Version 2023.10.1")
        self.menu_version_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

        self.menu_button_vlayout.addWidget(self.menu_gen_button)
        self.menu_button_vlayout.addWidget(self.menu_md_button)
        self.menu_button_vlayout.addWidget(self.menu_bd_button)
        self.menu_button_vlayout.addWidget(self.menu_fb_button)
        self.menu_button_vlayout.addWidget(self.menu_ab_button)

    def create_radio_button(self, text, checked=False):
        radio_button = QtWidgets.QRadioButton(parent=self.menu_button_vlayout_widget)
        radio_button.setSizePolicy(QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred))
        radio_button.setFont(self.BUTTON_FONT)
        radio_button.setStyleSheet(menu_buttons_style.button_style)
        radio_button.setChecked(checked)
        radio_button.setText(text)
        return radio_button

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = MenuWidget()
    main_window.show()

    sys.exit(app.exec())
