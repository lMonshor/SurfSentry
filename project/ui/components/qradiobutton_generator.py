from PyQt6 import QtCore, QtGui, QtWidgets
from styles.components_styles import qradiobuttons_styles, qfonts_styles

def create_radio_button(parent, text, checked=False, geometry=None):
    radio_button = QtWidgets.QRadioButton(parent=parent)
    radio_button.setSizePolicy(QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred))
    radio_button.setStyleSheet(qradiobuttons_styles.menu_widget_qradio_style)
    radio_button.setFont(qfonts_styles.subtitle_font)
    radio_button.setChecked(checked)
    radio_button.setText(text)
    if geometry:
        radio_button.setGeometry(geometry)
    return radio_button