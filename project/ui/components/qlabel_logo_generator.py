from PyQt6 import QtCore, QtGui, QtWidgets
import os

ASSETS_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\assets')
ICONS = {
    'control_logo': 'control_logo.png',
    'bottom_logo': 'bottom_logo.png',
}


def create_logo_label(parent, icon_name,  geometry=None):
    label = QtWidgets.QLabel(parent=parent)
    if geometry:
        label.setGeometry(geometry)
    label.setText('')
    label.setPixmap(QtGui.QPixmap(os.path.join(
        ASSETS_PATH, ICONS[icon_name])))
    label.setScaledContents(True)
    return label
