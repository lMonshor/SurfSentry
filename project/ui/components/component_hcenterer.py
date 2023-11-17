from PyQt6 import QtCore

def center_component_horizontally(component, text=None):
        if text:
            component.setText(text)
            component.adjustSize()
        parent_width = component.parent().width()

        component_width = component.width()
        component_height = component.height()

        x = (parent_width - component_width) // 2
        y = component.geometry().y()

        component.setGeometry(QtCore.QRect(x, y, component_width, component_height))