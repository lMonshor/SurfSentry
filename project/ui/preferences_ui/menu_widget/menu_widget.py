from PyQt6 import QtCore, QtGui, QtWidgets
from ui.components import qlabel_generator,qlayout_qwidget_generator
from ui.components import qradiobutton_generator
from styles.ui_styles import default_styles
from styles.components_styles import qfonts_styles, qlabels_styles

class MenuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(default_styles.light_style)

        self.menu_button_vlayout_widget, self.menu_button_vlayout = qlayout_qwidget_generator.create_vlayout_widget(
            parent=self,geometry=(QtCore.QRect(0, 30, 171, 241)))

        self.menu_gen_button = qradiobutton_generator.create_radio_button(
            parent=self.menu_button_vlayout_widget,
            text="General", 
            checked=True)
        
        self.menu_md_button = qradiobutton_generator.create_radio_button(
            parent=self.menu_button_vlayout_widget,
            text="Malicious Data")
        
        self.menu_bd_button = qradiobutton_generator.create_radio_button(
            parent=self.menu_button_vlayout_widget,
            text="Blocked Data")
        
        self.menu_fb_button = qradiobutton_generator.create_radio_button(
            parent=self.menu_button_vlayout_widget,
            text="Feedback")
        
        self.menu_ab_button = qradiobutton_generator.create_radio_button(
            parent=self.menu_button_vlayout_widget,
            text="About")

        self.menu_version_label = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.body_font,
            color=qlabels_styles.label_color,
            geometry=(QtCore.QRect(10, 500, 101, 16)),
            text="Version 2023.10.1")
        self.menu_version_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

        self.menu_button_vlayout.addWidget(self.menu_gen_button)
        self.menu_button_vlayout.addWidget(self.menu_md_button)
        self.menu_button_vlayout.addWidget(self.menu_bd_button)
        self.menu_button_vlayout.addWidget(self.menu_fb_button)
        self.menu_button_vlayout.addWidget(self.menu_ab_button)