from PyQt6 import QtCore, QtWidgets
from ui.components import qlayout_qwidget_generator, qlabel_generator, qframe_line_generator
from styles.components_styles import qfonts_styles, qlabels_styles


class GeneralPageWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.gen_information_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 61, 222, 33)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="General Information")

        self.gen_top_glayout_widget, self.top_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(40, 100, 350, 51)))

        self.gen_ip_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Public IP")

        self.gen_ip_label = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            copyable=True,
            text="255.255.255.255")

        self.gen_adapter_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Current Adapter")

        self.gen_adapter_cbox = QtWidgets.QComboBox(
            parent=self.gen_top_glayout_widget)

        self.gen_mal_inf_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 165, 403, 33)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Received Malicious Data Information")

        self.gen_bottom_glayout_widget, self.bottom_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(40, 205, 430, 74)))

        self.gen_tot_domain_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Total Number of Malicious Domains")

        self.gen_tot_domain_label = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            text="255")

        self.gen_tot_ip_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Total Number of Malicious IPS")

        self.gen_tot_ip_label = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            text="126")

        self.gen_last_upt_title = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Last Update Time")

        self.gen_last_upt_label = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            text="2023-10-07 11:08")

        self.gen_colon1 = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text=":")
        self.gen_colon2 = qlabel_generator.create_label(
            parent=self.gen_top_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")
        self.gen_colon3 = qlabel_generator.create_label(
            parent=self.gen_bottom_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")
        self.gen_colon4 = qlabel_generator.create_label(
            parent=self.gen_bottom_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")
        self.gen_colon5 = qlabel_generator.create_label(
            parent=self.gen_bottom_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.gen_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(48, 300, 672, 1)))

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
