from PyQt6 import QtCore, QtWidgets
from styles.components_styles import qtreewidget_styles


def create_tree_widget(parent, geometry, headerlabel):
    tree_widget = QtWidgets.QTreeWidget(parent=parent)
    tree_widget.setGeometry(geometry)
    tree_widget.setHeaderLabels([headerlabel])
    tree_widget_style = qtreewidget_styles.create_qtreew_style()
    tree_widget.setStyleSheet(tree_widget_style)
    
    return tree_widget