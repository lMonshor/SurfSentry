from PyQt6 import QtWidgets


def create_line_edit(parent, geometry=None, placeholder_text=None):
    qline = QtWidgets.QLineEdit(parent=parent)
    if geometry:
        qline.setGeometry(geometry)

    qline.setStyleSheet('''
            QLineEdit {
                color: white;
                border: none;
                border-width: thin;
                border-bottom: 1px solid #393E46;
            }
        ''')

    if placeholder_text:
        qline.setPlaceholderText(placeholder_text)

    return qline
