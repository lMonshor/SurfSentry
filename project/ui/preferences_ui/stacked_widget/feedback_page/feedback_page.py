from PyQt6 import QtCore, QtWidgets
from ui.components import qpushbutton_generator, qlabel_generator, qframe_line_generator, qtextedit_generator
from styles.components_styles import qfonts_styles, qlabels_styles, qtextedits_styles
from features import helper_methods
import re


class FeedbackPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.fb_email_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 30, 90, 20)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Email address"
        )

        self.fb_warning_label = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 84, 661, 20)),
            font=qfonts_styles.body_font,
            color=qlabels_styles.warning_color,
        )

        self.fb_email_text = qtextedit_generator.create_text_edit(
            parent=self,
            style=qtextedits_styles.border_style,
            geometry=(QtCore.QRect(30, 60, 661, 25)))

        self.fb_subject_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 100, 49, 20)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Subject"
        )

        self.fb_subject_text = qtextedit_generator.create_text_edit(
            parent=self,
            geometry=(QtCore.QRect(30, 130, 661, 25)),
            style=qtextedits_styles.border_style,
            placeholder_text="Briefly describe the issue.")

        self.fb_desc_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 170, 75, 20)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Description"
        )

        self.fb_desc_text = qtextedit_generator.create_text_edit(
            parent=self,
            geometry=(QtCore.QRect(30, 200, 661, 221)),
            style=qtextedits_styles.border_style,
            placeholder_text="Describe the issue/improvement in as much detail as you can. Include steps to replicate if relevant.")

        self.gb_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(48, 446, 672, 1))

        )

        self.fb_submit_fb_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(30, 470, 181, 26)),
            text="Submit feedback",
            on_click=self.submit_feedback)
        self.fb_submit_fb_button.setEnabled(False)


        self.fb_email_text.textChanged.connect(self.check_plain_text_edits)

    def check_plain_text_edits(self):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.fb_warning_label.clear()

        if not re.match(email_pattern, self.fb_email_text.toPlainText()):
            self.fb_submit_fb_button.setDisabled(True)
            self.fb_warning_label.setText(
                "Invalid email address. Please enter a valid email.")
            self.fb_warning_label.adjustSize()

        elif not self.fb_subject_text.toPlainText() or not self.fb_desc_text.toPlainText():
            self.fb_submit_fb_button.setDisabled(True)
            self.fb_warning_label.clear()

        else:
            self.fb_submit_fb_button.setDisabled(False)
            self.fb_warning_label.clear()

    def submit_feedback(self):
        helper_methods.send_email_feedback(email_address=self.fb_email_text,
                                           subject=self.fb_subject_text,
                                           description=self.fb_desc_text)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    input_dialog = FeedbackPageWidget()
    input_dialog.show()

    app.exec()