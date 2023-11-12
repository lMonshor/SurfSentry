from PyQt6 import QtWidgets, QtGui, QtCore

def create_frame_line(parent,geometry):
        line = QtWidgets.QFrame(parent=parent)
        line.setGeometry(geometry)
        line.setStyleSheet(f"background-color: #393E46;")
        line.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        line.setLineWidth(0)
        line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        return line