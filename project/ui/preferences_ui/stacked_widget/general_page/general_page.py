from PyQt6 import QtCore, QtGui, QtWidgets
from ui.components import qlayout_qwidget_generator, qpushbutton_generator, qlabel_generator
from styles.preferences_ui_styles.stacked_widget_styles import stacked_buttons_style


class GeneralPageWidget(QtWidgets.QWidget):
    TITLE_FONT = QtGui.QFont("Calibri", 18)
    LABEL_FONT = QtGui.QFont("Calibri", 12)
    LABEL_COLOR = "#777777"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #0f0f0f")
        self.gen_information_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 61, 222, 33)),
            font=self.TITLE_FONT,
            text="General Information")

        self.gen_top_glayout_widget, self.top_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(40, 100, 311, 51)))

        self.gen_ip_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            text="Public IP")

        self.gen_ip_label = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
            text="255.255.255.255")

        self.gen_adapter_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            text="Current Adapter")
        self.gen_adapter_title.setFixedWidth(110)

        self.gen_adapter_cbox = QtWidgets.QComboBox(
            parent=self.gen_top_glayout_widget)

        self.gen_mal_inf_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 190, 403, 33)),
            font=self.TITLE_FONT,
            text="Received Malicious Data Information")

        self.gen_bottom_glayout_widget, self.bottom_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(40, 230, 491, 74)))

        self.gen_tot_domain_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            text="Total Number of Malicious Domains")

        self.gen_tot_domain_label = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
            text="255")

        self.gen_tot_ip_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            text="Total Number of Malicious IPS")

        self.gen_tot_ip_label = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
            text="126")

        self.gen_last_upt_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            text="Last Update Time")

        self.gen_last_upt_label = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
            text="2023-10-07 11:08")

        self.gen_colon1 = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            text=":")
        self.gen_colon2 = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=self.LABEL_FONT,
            text=":")
        self.gen_colon3 = qlabel_generator.create_label(
            parent=self.gen_bottom_glayout_widget,
            font=self.LABEL_FONT,
            text=":")
        self.gen_colon4 = qlabel_generator.create_label(
            parent=self.gen_bottom_glayout_widget,
            font=self.LABEL_FONT,
            text=":")
        self.gen_colon5 = qlabel_generator.create_label(
            parent=self.gen_bottom_glayout_widget,
            font=self.LABEL_FONT,
            text=":")

        self.top_glayout.addWidget(self.gen_ip_title, 0, 0, 1, 1)
        self.top_glayout.addWidget(self.gen_colon1, 0, 1, 1, 1)
        self.top_glayout.addWidget(self.gen_ip_label, 0, 2, 1, 1)
        self.top_glayout.addWidget(self.gen_adapter_title, 1, 0, 1, 1)
        self.top_glayout.addWidget(self.gen_colon2, 1, 1, 1, 1)
        self.top_glayout.addWidget(self.gen_adapter_cbox, 1, 2, 1, 1)

        self.bottom_glayout.addWidget(self.gen_tot_domain_title, 0, 0, 1, 1)
        self.bottom_glayout.addWidget(self.gen_colon3, 0, 1, 1, 1)
        self.bottom_glayout.addWidget(self.gen_tot_domain_label, 0, 2, 1, 1)
        self.bottom_glayout.addWidget(self.gen_tot_ip_title, 1, 0, 1, 1)
        self.bottom_glayout.addWidget(self.gen_colon4, 1, 1, 1, 1)
        self.bottom_glayout.addWidget(self.gen_tot_ip_label, 1, 2, 1, 1)
        self.bottom_glayout.addWidget(self.gen_last_upt_title, 2, 0, 1, 1)
        self.bottom_glayout.addWidget(self.gen_colon5, 2, 1, 1, 1)
        self.bottom_glayout.addWidget(self.gen_last_upt_label, 2, 2, 1, 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = GeneralPageWidget()
    main_window.show()

    sys.exit(app.exec())
