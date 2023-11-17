from PyQt6 import QtWidgets, QtGui, QtCore
from ui.components import qpushbutton_generator, qlabel_generator, qframe_line_generator
from styles.components_styles import qfonts_styles, qlabels_styles
from features import helper_methods


class AboutPageWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ab_main_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 40, 124, 36)),
            font=qfonts_styles.headline_font,
            color=qlabels_styles.title_color,
            text="SurfSentry")

        self.ab_top_desc_label = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(40, 85, 671, 91)),
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Surfsentry is a Windows application developed to protect users against malicious websites. "
            "It retrieves a list of malicious links from USOM (Ulusal Siber Olaylara Müdahale Merkezi - National Cyber Incident Response Center) "
            "and writes them to the hosts file. This ensures a secure internet experience for users.",
            wordwrap=True)

        self.ab_bottom_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 180, 229, 30)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Blocking CNC Server IPs")

        self.ab_bottom_desc_label = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(40, 220, 671, 91)),
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Surfsentry not only blocks domain connections by writing them to the hosts file, "
            "but also identifies IP addresses associated with Command and Control (CNC) servers provided by USOM. "
            "It adds firewall rules to block communication with these IPs, providing an additional layer of protection against malicious activity.",
            wordwrap=True)

        self.ab_github_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(540, 470, 191, 27)),
            text="GitHub",
            on_click=(lambda: helper_methods.open_custom_page("https://github.com/lMonshor/SurfSentry")))

        self.ab_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(48, 335, 672, 1)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = AboutPageWidget()
    main_window.show()

    sys.exit(app.exec())
