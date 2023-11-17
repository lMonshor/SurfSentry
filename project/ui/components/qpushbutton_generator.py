from PyQt6 import QtCore, QtGui, QtWidgets
from styles.components_styles import qpushbuttons_styles
import os

def create_button(parent, text='', on_click=None, geometry=None):
    button = QtWidgets.QPushButton(parent=parent)
    button.setStyleSheet(qpushbuttons_styles.pages_button_style)
    button.setText(text)
    if on_click:
        button.clicked.connect(on_click)
    if geometry:
        button.setGeometry(geometry)
    return button

