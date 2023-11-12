from PyQt6 import QtCore, QtGui, QtWidgets
from ui.components import qpushbutton_generator, qlabel_generator
from styles.preferences_ui_styles.stacked_widget_styles import stacked_buttons_style
from features import helper_methods


class FeedbackPageWidget(QtWidgets.QWidget):
    TITLE_FONT = QtGui.QFont('Calibri', 12)

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.fb_email_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 35, 90, 20)),
            font=self.TITLE_FONT,
            text="Email address"
        )

        self.fb_email_text = self.create_text_edit(
            self, QtCore.QRect(30, 60, 661, 25))

        self.fb_subject_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 105, 49, 20)),
            font=self.TITLE_FONT,
            text="Subject"
        )

        self.fb_subject_text = self.create_text_edit(
            self, QtCore.QRect(30, 130, 661, 25), "Briefly describe the issue.")

        self.fb_desc_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 175, 75, 20)),
            font=self.TITLE_FONT,
            text="Description"
        )

        self.fb_desc_text = self.create_text_edit(self, QtCore.QRect(
            30, 200, 661, 221), "Describe the issue/improvement in as much detail as you can. Include steps to replicate if relevant.")
        
        self.fb_submit_fb_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(30, 470, 181, 26)),
            text="Submit feedback",
            on_click=self.submit_feedback)
        self.fb_submit_fb_button.setEnabled(False)

        self.fb_email_text.textChanged.connect(self.check_plain_text_edits)
        self.fb_subject_text.textChanged.connect(self.check_plain_text_edits)
        self.fb_desc_text.textChanged.connect(self.check_plain_text_edits)

    def create_text_edit(self, parent, geometry, placeholder_text=None):
        text_edit = QtWidgets.QPlainTextEdit(parent=parent)
        text_edit.setGeometry(geometry)
        text_edit.setStyleSheet("background-color:#393E46;\n color:white;")
        text_edit.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        if placeholder_text:
            text_edit.setPlaceholderText(placeholder_text)

        return text_edit

    def check_plain_text_edits(self):
        if not self.fb_email_text.toPlainText() or not self.fb_subject_text.toPlainText() or not self.fb_desc_text.toPlainText():
            self.fb_submit_fb_button.setDisabled(True)
        else:
            self.fb_submit_fb_button.setDisabled(False)

    def submit_feedback(self):
        helper_methods.send_email_feedback(email_address=self.fb_email_text,
                                           subject=self.fb_subject_text,
                                           description=self.fb_desc_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = FeedbackPageWidget()
    main_window.show()

    sys.exit(app.exec())
