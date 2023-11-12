from PyQt6 import QtCore, QtGui, QtWidgets


def create_vlayout_widget(parent, geometry):
    layout_widget = QtWidgets.QWidget(parent=parent)
    layout_widget.setGeometry(geometry)
    layout = QtWidgets.QGridLayout(layout_widget)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    return layout_widget, layout

def create_glayout_widget(parent,geometry):
    layout_widget = QtWidgets.QWidget(parent=parent)
    layout_widget.setGeometry(geometry)
    layout = QtWidgets.QGridLayout(layout_widget)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setHorizontalSpacing(6)
    return layout_widget, layout