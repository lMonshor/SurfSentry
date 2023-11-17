from PyQt6 import QtCore, QtWidgets


def create_label(parent, font, text='', geometry=None, color=None, wordwrap=False, copyable=False):
    label = QtWidgets.QLabel(parent=parent)
    if geometry:
        label.setGeometry(geometry)

    
    label.setWordWrap(wordwrap)
    label.setStyleSheet(color)
    label.setFont(font)
    if copyable:
        label.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
    
    if text != '':
        label.setText(text)
        label.adjustSize()
    return label
