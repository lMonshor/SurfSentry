from PyQt6 import QtCore, QtGui, QtWidgets


def create_vlayout_widget(parent, geometry=None):
    layout_widget = QtWidgets.QWidget(parent=parent)
    if geometry:
        layout_widget.setGeometry(geometry)
    layout = QtWidgets.QVBoxLayout(layout_widget)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    return layout_widget, layout


def create_hlayout_widget(parent, geometry):
    layout_widget = QtWidgets.QWidget(parent=parent)
    layout_widget.setGeometry(geometry)
    layout = QtWidgets.QHBoxLayout(layout_widget)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    return layout_widget, layout


def create_glayout_widget(parent, geometry):
    layout_widget = QtWidgets.QWidget(parent=parent)
    layout_widget.setGeometry(geometry)
    layout = QtWidgets.QGridLayout(layout_widget)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setHorizontalSpacing(4)
    layout.setVerticalSpacing(3)
    layout.setColumnStretch(0, 0)
    layout.setColumnStretch(1, 0)
    layout.setColumnStretch(2, 1)
    return layout_widget, layout
