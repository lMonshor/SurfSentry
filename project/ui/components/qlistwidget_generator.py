from PyQt6 import QtCore, QtWidgets
from styles.components_styles import qlistwidgets_styles


def create_list_widget(parent, geometry):
    list_widget = QtWidgets.QListWidget(parent=parent)
    list_widget.setGeometry(geometry)
    list_widget.setSizePolicy(QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred))
    list_widget.setStyleSheet(qlistwidgets_styles.default_qlistw_style)
    list_widget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
    list_widget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
    list_widget.setLineWidth(2)
    list_widget.setHorizontalScrollBarPolicy(
        QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    list_widget.setVerticalScrollMode(
        QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
    list_widget.setHorizontalScrollMode(
        QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
    list_widget.setSelectionRectVisible(True)

    return list_widget
