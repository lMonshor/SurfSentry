from PyQt6 import QtCore, QtGui, QtWidgets
from styles.components_styles import qpushbuttons_styles
import os

ASSETS_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\assets')

ICONS = {
    'bottom_settings': 'bottom_settings_button.png',
    'bottom_bug': 'bottom_bug_button.png',
    'single_right': 'single_right_logo.png',
    'double_right': 'double_right_logo.png',
    'single_left': 'single_left_logo.png',
    'double_left': 'double_left_logo.png',
    'add': 'add_logo.png',
    'trash': 'trash_logo.png',

}


def create_logo_button(parent, icon_name, on_click=None, geometry=None):
    button = QtWidgets.QPushButton(parent=parent)
    button.setStyleSheet(qpushbuttons_styles.pages_button_style)
    button.setText('')
    button_icon = QtGui.QIcon()
    button_icon.addPixmap(QtGui.QPixmap(os.path.join(ASSETS_PATH, ICONS[icon_name])),
                          QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    button.setIcon(button_icon)
    if geometry:
        button.setGeometry(geometry)
    if on_click:
        button.clicked.connect(on_click)
    return button
