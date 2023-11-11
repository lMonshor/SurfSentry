from PyQt6 import QtCore, QtGui, QtWidgets
from styles import md_styles
from styles.stacked_widget_style import stacked_widget_button_style
from db import db_operations
from features import methods, workers
from ui.loading_ui import loading_ui
from ui.information_ui import information_ui


class MalDataPageWidget(QtWidgets.QWidget):
    def __init__(self,my_blocked_data_page):
        self.my_blocked_data_page = my_blocked_data_page
        super().__init__()

        self.initUI()

    def initUI(self):
        self.md_detail_title = QtWidgets.QLabel(parent=self)
        self.md_detail_title.setGeometry(QtCore.QRect(320, 120, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.md_detail_title.setFont(font)
        self.md_detail_title.setStyleSheet("color:white;")
        self.md_inf_glayout_widget = QtWidgets.QWidget(parent=self)
        self.md_inf_glayout_widget.setGeometry(
            QtCore.QRect(330, 150, 431, 127))
        self.md_inf_glayout = QtWidgets.QGridLayout(self.md_inf_glayout_widget)
        self.md_inf_glayout.setContentsMargins(0, 0, 0, 0)
        self.md_inf_glayout.setSpacing(6)
        self.md_detail_type_label = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_detail_type_label.sizePolicy().hasHeightForWidth())
        self.md_detail_type_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_type_label.setFont(font)
        self.md_detail_type_label.setStyleSheet("color:#777777;")
        self.md_detail_type_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.md_detail_type_label.setText("")
        self.md_inf_glayout.addWidget(self.md_detail_type_label, 1, 2, 1, 1)
        self.md_detail_colon3 = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon3.setFont(font)
        self.md_detail_colon3.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_colon3, 1, 1, 1, 1)
        self.md_detail_date_label = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_detail_date_label.sizePolicy().hasHeightForWidth())
        self.md_detail_date_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_date_label.setFont(font)
        self.md_detail_date_label.setStyleSheet("color:#777777;")
        self.md_detail_date_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.md_detail_date_label.setText("")
        self.md_inf_glayout.addWidget(self.md_detail_date_label, 3, 2, 1, 1)
        self.md_detail_type_title = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_type_title.setFont(font)
        self.md_detail_type_title.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_type_title, 2, 0, 1, 1)
        self.md_detail_colon4 = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon4.setFont(font)
        self.md_detail_colon4.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_colon4, 2, 1, 1, 1)
        self.md_detail_source_label = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_detail_source_label.sizePolicy().hasHeightForWidth())
        self.md_detail_source_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_source_label.setFont(font)
        self.md_detail_source_label.setStyleSheet("color:#777777;")
        self.md_detail_source_label.setFrameShape(
            QtWidgets.QFrame.Shape.NoFrame)
        self.md_detail_source_label.setText("")
        self.md_inf_glayout.addWidget(self.md_detail_source_label, 2, 2, 1, 1)
        self.md_detail_colon6 = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon6.setFont(font)
        self.md_detail_colon6.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_colon6, 4, 1, 1, 1)
        self.md_detail_colon5 = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon5.setFont(font)
        self.md_detail_colon5.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_colon5, 3, 1, 1, 1)
        self.md_detail_date_title = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_date_title.setFont(font)
        self.md_detail_date_title.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_date_title, 3, 0, 1, 1)
        self.md_detail_source_title = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_source_title.setFont(font)
        self.md_detail_source_title.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_source_title, 1, 0, 1, 1)
        self.md_detail_desc_title = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_desc_title.setFont(font)
        self.md_detail_desc_title.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_desc_title, 4, 0, 1, 1)
        self.md_detail_url_title = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.md_detail_url_title.setFont(font)
        self.md_detail_url_title.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_url_title, 0, 0, 1, 1)
        self.md_detail_colon1 = QtWidgets.QLabel(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_colon1.setFont(font)
        self.md_detail_colon1.setStyleSheet("color:white;")
        self.md_inf_glayout.addWidget(self.md_detail_colon1, 0, 1, 1, 1)
        self.md_detail_url_label = QtWidgets.QLineEdit(
            parent=self.md_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_url_label.setFont(font)
        self.md_detail_url_label.setStyleSheet("color:#777777;")
        self.md_detail_url_label.setText("")
        self.md_detail_url_label.setFrame(False)
        self.md_detail_url_label.setReadOnly(True)
        self.md_inf_glayout.addWidget(self.md_detail_url_label, 0, 2, 1, 1)
        self.md_threat_level_title = QtWidgets.QLabel(
            parent=self)
        self.md_threat_level_title.setGeometry(QtCore.QRect(380, 60, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.md_threat_level_title.setFont(font)
        self.md_threat_level_title.setStyleSheet("background-color:#393E46;\n"
                                                 "    color: #EEEEEE;")
        self.md_threat_level_title.setFrameShape(
            QtWidgets.QFrame.Shape.NoFrame)
        self.md_threat_level_title.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.md_threat_level_title.setScaledContents(False)
        self.md_threat_level_title.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.md_source_button = QtWidgets.QPushButton(
            parent=self)
        self.md_source_button.setEnabled(False)
        self.md_source_button.setGeometry(QtCore.QRect(450, 490, 191, 27))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.md_source_button.setFont(font)
        self.md_source_button.setStyleSheet(
            stacked_widget_button_style.button_style)
        self.md_main_title = QtWidgets.QLabel(parent=self)
        self.md_main_title.setGeometry(QtCore.QRect(30, 30, 188, 24))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_main_title.sizePolicy().hasHeightForWidth())
        self.md_main_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.md_main_title.setFont(font)
        self.md_main_title.setStyleSheet("color:white;")
        self.md_data_update_button = QtWidgets.QPushButton(
            parent=self)
        self.md_data_update_button.setGeometry(QtCore.QRect(70, 490, 191, 27))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.md_data_update_button.setFont(font)
        self.md_data_update_button.setStyleSheet(
            stacked_widget_button_style.button_style)
        self.md_data_update_button.setFlat(False)
        self.md_second_hline = QtWidgets.QFrame(parent=self)
        self.md_second_hline.setGeometry(QtCore.QRect(330, 480, 421, 1))
        self.md_second_hline.setStyleSheet("background-color:#393E46;")
        self.md_second_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.md_second_hline.setLineWidth(0)
        self.md_second_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.md_mal_data_list = QtWidgets.QListWidget(
            parent=self)
        self.md_mal_data_list.setGeometry(QtCore.QRect(30, 60, 281, 421))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_mal_data_list.sizePolicy().hasHeightForWidth())
        self.md_mal_data_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.md_mal_data_list.setFont(font)
        self.md_mal_data_list.setToolTipDuration(-1)
        self.md_mal_data_list.setStyleSheet(md_styles.mal_data_list_style)
        self.md_mal_data_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.md_mal_data_list.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.md_mal_data_list.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.md_mal_data_list.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.md_mal_data_list.setAutoScroll(True)
        self.md_mal_data_list.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.md_mal_data_list.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.md_mal_data_list.setWordWrap(True)
        self.md_mal_data_list.setSelectionRectVisible(True)
        self.md_detail_desc_label = QtWidgets.QLabel(parent=self)
        self.md_detail_desc_label.setGeometry(QtCore.QRect(350, 290, 391, 161))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.md_detail_desc_label.sizePolicy().hasHeightForWidth())
        self.md_detail_desc_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.md_detail_desc_label.setFont(font)
        self.md_detail_desc_label.setContextMenuPolicy(
            QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.md_detail_desc_label.setStyleSheet("color:#777777;\n"
                                                "border:none;")
        self.md_detail_desc_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.md_detail_desc_label.setText("")
        self.md_detail_desc_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.md_detail_desc_label.setWordWrap(True)
        self.md_first_hline = QtWidgets.QFrame(parent=self)
        self.md_first_hline.setGeometry(QtCore.QRect(330, 106, 421, 1))
        self.md_first_hline.setStyleSheet("background-color:#393E46;")
        self.md_first_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.md_first_hline.setLineWidth(0)
        self.md_first_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)

        self.md_detail_title.setText("Other Information")
        self.md_detail_colon3.setText(":")
        self.md_detail_type_title.setText("Type")
        self.md_detail_colon4.setText(":")
        self.md_detail_colon6.setText(":")
        self.md_detail_colon5.setText(":")
        self.md_detail_date_title.setText("Date")
        self.md_detail_source_title.setText("Source        ")
        self.md_detail_desc_title.setText("Description")
        self.md_detail_url_title.setText("URL             ")
        self.md_detail_colon1.setText(":")
        self.md_threat_level_title.setText("THREAT LEVEL")
        self.md_source_button.setText("USOM Source")
        self.md_main_title.setText("Received Malicious Data")
        self.md_data_update_button.setText("Update Data")
        self.md_mal_data_list.setSortingEnabled(True)

        self.md_mal_data_list.itemSelectionChanged.connect(
            lambda: self.fillMalDetails(self.md_mal_data_list.selectedItems()))

        self.md_data_update_button.clicked.connect(self.updateData)

    def fillMalList(self):
        try:
            self.md_mal_data_list.clear()
            self.md_mal_data_list.clearSelection()
            mal_urls = db_operations.get_data_by_column_name(
                column_name="url", table_name="malicious_data")
            for row in mal_urls:
                mal_url = QtWidgets.QListWidgetItem(str(row[0]))
                self.md_mal_data_list.addItem(mal_url)
                self.md_mal_data_list.addItem(mal_url)
        except Exception as e:
            print(f"Error fillMalList: {e}")

    def fillMalDetails(self, sel_mal_items):
        try:
            if sel_mal_items:
                sel_mal_item = sel_mal_items[0]
                sel_mal_item_detail = db_operations.get_one_data_detail(
                    column_name="*", condition_column='url', condition_value=sel_mal_item.text(), table_name='malicious_data')
                self.md_source_button.setEnabled(True)
                self.md_source_button.disconnect()
                self.md_source_button.clicked.connect(
                    lambda: methods.openCustomWebPage(sel_mal_item_detail[9]))

                self.md_detail_url_label.setText(sel_mal_item_detail[3])
                self.md_detail_type_label.setText(sel_mal_item_detail[4])
                self.md_detail_desc_label.setText(sel_mal_item_detail[5])
                if sel_mal_item_detail[6] <= 3:
                    self.md_mal_data_list.setStyleSheet(
                        md_styles.low_level_style)
                    self.md_threat_level_title.setText("LOW")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #23B7E5;color:white;")
                elif 4 <= sel_mal_item_detail[6] <= 7:
                    self.md_mal_data_list.setStyleSheet(
                        md_styles.medium_level_style)
                    self.md_threat_level_title.setText("MEDIUM")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #FF902B;color:white;")
                else:
                    self.md_mal_data_list.setStyleSheet(
                        md_styles.high_level_style)
                    self.md_threat_level_title.setText("HIGH")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #F05050;color:white;")
                self.md_detail_source_label.setText(sel_mal_item_detail[7])
                self.md_detail_date_label.setText(sel_mal_item_detail[8])
        except Exception as e:
            print(f"Error fillMalDetails: {e}")

    def updateData(self):
        my_loading_ui = loading_ui.uiLoading()
        my_loading_ui.show()
        my_information_ui = information_ui.uiInformation()
        my_update_data_worker = workers.UpdateDataWorker(
            my_loading_ui=my_loading_ui)
        my_update_data_worker.finished.connect(my_update_data_worker.wait)
        my_update_data_worker.finished.connect(my_update_data_worker.quit)
        my_update_data_worker.finished.connect(self.fillMalList)
        my_update_data_worker.finished.connect(self.my_blocked_data_page.fillBlockedList)
        my_update_data_worker.finished.connect(my_loading_ui.deleteLater)
        my_update_data_worker.finished.connect(lambda: my_information_ui.show())
        my_update_data_worker.start()



