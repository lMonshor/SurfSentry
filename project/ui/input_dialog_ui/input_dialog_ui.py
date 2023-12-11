from PyQt6 import QtCore, QtWidgets, QtGui
from styles.components_styles import qfonts_styles, qlabels_styles, qtextedits_styles
from styles.ui_styles import default_styles
from features import workers
from ui.components import qlabel_generator, qlayout_qwidget_generator, qtextedit_generator, qpushbutton_generator
from db import db_operations
from features import helper_methods
import re


class UiInputWidget(QtWidgets.QDialog):
    data_processed = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(420, 188)
        self.setStyleSheet(default_styles.dark_style)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.input_title = qlabel_generator.create_label(
            parent=self,
            color=qlabels_styles.title_color,
            font=qfonts_styles.title_font,
            text="Add Data")
        self.input_title.setGeometry(QtCore.QRect(20, 10, 120, 28))

        self.input_fields_glayout_widget, self.input_fields_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(20, 40, 380, 102)))

        self.input_address_text_title = qlabel_generator.create_label(
            parent=self.input_fields_glayout_widget,
            font=qfonts_styles.body_font,
            color=qlabels_styles.title_color,
            text='Address')

        self.input_mal_type_text_title = qlabel_generator.create_label(
            parent=self.input_fields_glayout_widget,
            font=qfonts_styles.body_font,
            color=qlabels_styles.title_color,
            text='Type')

        self.input_desc_text_title = qlabel_generator.create_label(
            parent=self.input_fields_glayout_widget,
            font=qfonts_styles.body_font,
            color=qlabels_styles.title_color,
            text='Description')

        self.input_severity_text_title = qlabel_generator.create_label(
            parent=self.input_fields_glayout_widget,
            font=qfonts_styles.body_font,
            color=qlabels_styles.title_color,
            text='Severity')

        self.input_address_text = qtextedit_generator.create_text_edit(
            parent=self.input_fields_glayout_widget,
            style=qtextedits_styles.borderless_style,
            placeholder_text='example.com or 1.1.1.1'
        )

        self.input_address_text_warning_label = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(110, 142, 150, 20)),
            font=qfonts_styles.body_font,
            color=qlabels_styles.warning_color,
        )

        self.input_mal_type_text = qtextedit_generator.create_text_edit(
            parent=self.input_fields_glayout_widget,
            style=qtextedits_styles.borderless_style,
            placeholder_text='phishing, malware command center or etc.'
        )

        self.input_desc_text = qtextedit_generator.create_text_edit(
            parent=self.input_fields_glayout_widget,
            style=qtextedits_styles.borderless_style,
            placeholder_text='description'
        )

        self.input_severity_text = qtextedit_generator.create_text_edit(
            parent=self.input_fields_glayout_widget,
            style=qtextedits_styles.borderless_style,
            placeholder_text='a number between 1 and 10'
        )

        self.colon1 = qlabel_generator.create_label(
            parent=self.input_fields_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="     ")

        self.colon2 = qlabel_generator.create_label(
            parent=self.input_fields_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="     ")

        self.colon3 = qlabel_generator.create_label(
            parent=self.input_fields_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="     ")

        self.colon4 = qlabel_generator.create_label(
            parent=self.input_fields_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="     ")

        self.input_fields_glayout.addWidget(
            self.input_address_text_title, 0, 0, 1, 1)
        self.input_fields_glayout.addWidget(self.colon1, 0, 1, 1, 1)
        self.input_fields_glayout.addWidget(
            self.input_address_text, 0, 2, 1, 1)
        self.input_fields_glayout.addWidget(
            self.input_mal_type_text_title, 1, 0, 1, 1)
        self.input_fields_glayout.addWidget(self.colon2, 1, 1, 1, 1)
        self.input_fields_glayout.addWidget(
            self.input_mal_type_text, 1, 2, 1, 1)
        self.input_fields_glayout.addWidget(
            self.input_desc_text_title, 2, 0, 1, 1)
        self.input_fields_glayout.addWidget(self.colon3, 2, 1, 1, 1)
        self.input_fields_glayout.addWidget(self.input_desc_text, 2, 2, 1, 1)
        self.input_fields_glayout.addWidget(
            self.input_severity_text_title, 3, 0, 1, 1)
        self.input_fields_glayout.addWidget(self.colon4, 3, 1, 1, 1)
        self.input_fields_glayout.addWidget(
            self.input_severity_text, 3, 2, 1, 1)

        self.input_button_fields_hloayout_widget, self.input_button_fields_hloayout = qlayout_qwidget_generator.create_hlayout_widget(
            parent=self,
            geometry=(QtCore.QRect(2, 160, 417, 30)))

        self.input_add_button = qpushbutton_generator.create_button(
            parent=self,
            enabled=False,
            on_click=self.add_data,
            text="ADD"
        )

        self.input_cancel_button = qpushbutton_generator.create_button(
            parent=self,
            on_click=self.close,
            text="CANCEL"
        )

        self.input_button_fields_hloayout.addWidget(self.input_add_button)
        self.input_button_fields_hloayout.addWidget(self.input_cancel_button)

        self.input_address_text.textChanged.connect(
            self.check_address)

        self.address_type = None

    def check_address(self):
        ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
        domain_pattern = r"\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b"
        self.input_address_text_warning_label.clear()

        address = self.input_address_text.toPlainText()
        is_exist = db_operations.check_address_exists(address=address)

        if not re.match(ip_pattern, address) and not re.match(domain_pattern, address):
            self.input_address_text_warning_label.setText('Invalid address.')
            self.input_add_button.setEnabled(False)

        elif is_exist:
            self.input_address_text_warning_label.setText(
                'Already exist address.')
            self.input_add_button.setEnabled(False)

        else:
            self.input_add_button.setEnabled(True)

        if re.match(ip_pattern, self.input_address_text.toPlainText()):
            self.address_type = 'ip'

        elif re.match(domain_pattern, self.input_address_text.toPlainText()):
            self.address_type = 'domain'

    def add_data(self):
        date = helper_methods.get_current_date()

        entry = {
            'data_id': 'not available',
            'data_type': self.address_type,
            'address': self.input_address_text.toPlainText(),
            'mal_type': self.input_mal_type_text.toPlainText() if self.input_mal_type_text.toPlainText()
            else 'not avaliable',
            'desc': self.input_desc_text.toPlainText() if self.input_desc_text.toPlainText()
            else 'not avaliable',
            'severity': self.input_severity_text.toPlainText() if self.input_severity_text.toPlainText()
            else 'not avaliable',
            'source': 'user added',
            'data_date': date,
            'current_status': 'unblocked',
            'op_time': 'not available',
            'update_date': date,
            'link': 'not avaliable'
        }

        address = entry['address']

        db_operations.save_to_table(entry=entry)

        my_blocking_op_worker = workers.BlockingOperationsWorker(
            entry=entry, sender="add_button")
        my_blocking_op_worker.finished.connect(lambda: self.close())
        my_blocking_op_worker.finished.connect(
            lambda: self.data_processed.emit())

        my_blocking_op_worker.finished.connect(my_blocking_op_worker.wait)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.quit)
        my_blocking_op_worker.start()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])

    input_dialog = UiInputWidget()
    input_dialog.show()

    sys.exit(app.exec())
