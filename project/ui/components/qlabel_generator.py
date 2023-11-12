from PyQt6 import QtCore, QtGui, QtWidgets
import os

ASSETS_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\assets')
ICONS = {
    'control_logo': 'control_logo.png',
    'bottom_logo': 'bottom_logo.png',
}


def create_label(parent,  text='', geometry=None,font=None, color='white', icon_name=None):
    label = QtWidgets.QLabel(parent=parent)
    if geometry:
        label.setGeometry(geometry)
    label.setStyleSheet(f"color: {color};")
    label.setText(text)
    label.setWordWrap(True)
    if font is not None:
        label.setFont(font)
    if text == ":":
        label.setFixedWidth(5)
    if icon_name:
        label.setPixmap(QtGui.QPixmap(os.path.join(
            ASSETS_PATH, ICONS[icon_name])))
        label.setScaledContents(True)
    return label
