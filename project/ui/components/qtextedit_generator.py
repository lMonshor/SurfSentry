from PyQt6 import QtCore, QtGui, QtWidgets


def create_text_edit(parent, geometry, placeholder_text=None):
    text_edit = QtWidgets.QPlainTextEdit(parent=parent)
    text_edit.setGeometry(geometry)
    text_edit.setStyleSheet("background-color:#202123; color:white;")
    text_edit.setVerticalScrollBarPolicy(
        QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    if placeholder_text:
        text_edit.setPlaceholderText(placeholder_text)
    return text_edit
