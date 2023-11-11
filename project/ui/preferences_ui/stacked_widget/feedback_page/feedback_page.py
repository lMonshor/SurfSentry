from PyQt6 import QtCore, QtGui, QtWidgets
from styles import bd_styles
from styles.stacked_widget_style import stacked_widget_button_style
from features import methods

class FeedbackPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.fb_email_text = QtWidgets.QPlainTextEdit(
            parent=self)
        self.fb_email_text.setGeometry(QtCore.QRect(30, 60, 661, 25))
        self.fb_email_text.setStyleSheet("background-color:#393E46;\n"
                                         "color:white;")
        self.fb_email_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fb_email_title = QtWidgets.QLabel(parent=self)
        self.fb_email_title.setGeometry(QtCore.QRect(30, 35, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fb_email_title.setFont(font)
        self.fb_email_title.setStyleSheet("color:white;")
        self.fb_subject_text = QtWidgets.QPlainTextEdit(
            parent=self)
        self.fb_subject_text.setGeometry(QtCore.QRect(30, 130, 661, 25))
        self.fb_subject_text.setStyleSheet("background-color:#393E46;\n"
                                           "color:white;")
        self.fb_subject_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fb_subject_title = QtWidgets.QLabel(parent=self)
        self.fb_subject_title.setGeometry(QtCore.QRect(30, 105, 49, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fb_subject_title.setFont(font)
        self.fb_subject_title.setStyleSheet("color:white;")
        self.fb_desc_title = QtWidgets.QLabel(parent=self)
        self.fb_desc_title.setGeometry(QtCore.QRect(30, 175, 75, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fb_desc_title.setFont(font)
        self.fb_desc_title.setStyleSheet("color:white;")
        self.fb_desc_text = QtWidgets.QPlainTextEdit(parent=self)
        self.fb_desc_text.setGeometry(QtCore.QRect(30, 200, 661, 221))
        self.fb_desc_text.setStyleSheet("background-color:#393E46;\n"
                                        "color:white;")
        self.fb_submit_fb_button = QtWidgets.QPushButton(
            parent=self)
        self.fb_submit_fb_button.setGeometry(QtCore.QRect(30, 470, 181, 26))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.fb_submit_fb_button.setFont(font)
        self.fb_submit_fb_button.setStyleSheet(stacked_widget_button_style.button_style)
        self.fb_submit_fb_button.setFlat(False)
        self.fb_email_title.setText("Email address")
        self.fb_subject_text.setPlaceholderText("Briefly describe the issue.")
        self.fb_subject_title.setText("Subject")
        self.fb_desc_title.setText("Description")
        self.fb_desc_text.setPlaceholderText(
            "Describe the issue/improvement in as much detail as you can. Include steps to replicate if relevant.")
        self.fb_submit_fb_button.setText("Submit feedback")
        
        self.fb_email_text.textChanged.connect(self.checkPlainTextEdits)
        self.fb_subject_text.textChanged.connect(self.checkPlainTextEdits)
        self.fb_desc_text.textChanged.connect(self.checkPlainTextEdits)
        self.fb_submit_fb_button.setEnabled(False)
        
        self.fb_submit_fb_button.clicked.connect(lambda: methods.send_email_feedback(
            email_address=self.fb_email_text, subject=self.fb_subject_text, description=self.fb_desc_text))
        
        
    def checkPlainTextEdits(self):
        if not self.fb_email_text.toPlainText() or not self.fb_subject_text.toPlainText() or not self.fb_desc_text.toPlainText():
            self.fb_submit_fb_button.setDisabled(True)
        else:
            self.fb_submit_fb_button.setDisabled(False)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = FeedbackPageWidget()
    main_window.show()

    sys.exit(app.exec())