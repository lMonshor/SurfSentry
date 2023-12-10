from PyQt6 import QtCore, QtWidgets
from styles.components_styles import qtextedits_styles


def create_text_edit(parent, geometry=None, placeholder_text=None, style=None):
    text_edit = QtWidgets.QPlainTextEdit(parent=parent)
    
    def custom_keyPressEvent(event):
        if event.key() == QtCore.Qt.Key.Key_Tab:
            event.ignore()
        else:
            QtWidgets.QPlainTextEdit.keyPressEvent(text_edit, event)

    text_edit.keyPressEvent = custom_keyPressEvent
    
    if geometry:
        text_edit.setGeometry(geometry)

    text_edit.setStyleSheet(style)
    text_edit.setVerticalScrollBarPolicy(
        QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    if placeholder_text:
        text_edit.setPlaceholderText(placeholder_text)
    return text_edit
