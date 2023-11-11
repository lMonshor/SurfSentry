from PyQt6 import QtCore, QtGui, QtWidgets
from styles import bd_styles
from styles.stacked_widget_style import stacked_widget_button_style
from features import methods


class AboutPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.ab_github_button = QtWidgets.QPushButton(parent=self)
        self.ab_github_button.setGeometry(QtCore.QRect(540, 470, 191, 27))
        self.ab_github_button.setStyleSheet(stacked_widget_button_style.button_style)
        self.ab_top_desc_text = QtWidgets.QPlainTextEdit(
            parent=self)
        self.ab_top_desc_text.setGeometry(QtCore.QRect(40, 80, 671, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ab_top_desc_text.setFont(font)
        self.ab_top_desc_text.setStyleSheet("background-color:#0f0f0f;\n"
                                              "color:white;\n"
                                              "border:none;")
        self.ab_top_desc_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ab_top_desc_text.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ab_top_desc_text.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.ab_top_desc_text.setReadOnly(True)
        self.ab_top_desc_text.setPlaceholderText("")
        self.ab_main_title = QtWidgets.QLabel(parent=self)
        self.ab_main_title.setGeometry(QtCore.QRect(30, 40, 124, 36))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(False)
        self.ab_main_title.setFont(font)
        self.ab_main_title.setStyleSheet("color:white;")
        self.ab_bottom_title = QtWidgets.QLabel(parent=self)
        self.ab_bottom_title.setGeometry(QtCore.QRect(30, 180, 229, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.ab_bottom_title.setFont(font)
        self.ab_bottom_title.setStyleSheet("color:white;")
        self.ab_bottom_desc_text = QtWidgets.QPlainTextEdit(parent=self)
        self.ab_bottom_desc_text.setGeometry(QtCore.QRect(40, 220, 671, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ab_bottom_desc_text.setFont(font)
        self.ab_bottom_desc_text.setStyleSheet("background-color:#0f0f0f;\n"
                                          "color:white;\n"
                                          "border:none;")
        self.ab_bottom_desc_text.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ab_bottom_desc_text.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ab_bottom_desc_text.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.ab_bottom_desc_text.setReadOnly(True)
        self.ab_bottom_desc_text.setPlaceholderText("")
        self.ab_first_hline = QtWidgets.QFrame(parent=self)
        self.ab_first_hline.setGeometry(QtCore.QRect(48, 350, 672, 1))
        self.ab_first_hline.setStyleSheet("background-color:#393E46;")
        self.ab_first_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ab_first_hline.setLineWidth(0)
        self.ab_first_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        
        self.ab_github_button.setText("GitHub")
        self.ab_top_desc_text.setPlainText("Surfsentry is a Windows application developed to protect users against malicious websites. It retrieves a list of malicious links from USOM (Ulusal Siber Olaylara Müdahale Merkezi - National Cyber Incident Response Center) and writes them to the hosts file. This ensures a secure internet experience for users.\n"
                                             "\n"
                                             "")
        self.ab_main_title.setText("SurfSentry")
        self.ab_bottom_title.setText("Blocking CNC Server IPs")
        self.ab_bottom_desc_text.setPlainText(
            "Surfsentry not only blocks domain connections by writing them to the hosts file, but also identifies IP addresses associated with Command and Control (CNC) servers provided by USOM. It adds firewall rules to block communication with these IPs, providing an additional layer of protection against malicious activity.")

        self.ab_github_button.clicked.connect(
            lambda: methods.openCustomWebPage("https://github.com/lMonshor/SurfSentry"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = AboutPageWidget()
    main_window.show()

    sys.exit(app.exec())