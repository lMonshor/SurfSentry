from PyQt6 import QtCore, QtGui, QtWidgets
from styles.preferences_ui_styles.stacked_widget_styles import stacked_buttons_style,qlistwidget_style,mal_data_styles
from db import db_operations
from ui.components import qlabel_generator,qpushbutton_generator,qframe_line_generator,qlistwidget_generator,qlayout_qwidget_generator
from features import helper_methods, workers
from ui.loading_ui import loading_ui
from ui.information_ui import information_ui


class MalDataPageWidget(QtWidgets.QWidget):
    TITLE_FONT = QtGui.QFont("Calibri", 14)
    LABEL_FONT = QtGui.QFont("Calibri", 12)
    LABEL_COLOR = "#777777"
    THREAT_FONT = QtGui.QFont("Calibri", 14)
    THREAT_FONT.setBold(True)
    def __init__(self,my_blocked_data_page):
        self.my_blocked_data_page = my_blocked_data_page
        super().__init__()

        self.initUI()

    def initUI(self):
        self.md_mal_data_list_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 30, 188, 24)),
            font=self.TITLE_FONT,
            text="Received Malicious Data"
        )
        
        self.md_mal_data_list = qlistwidget_generator.create_list_widget(
            parent=self,
            geometry=(QtCore.QRect(30, 60, 281, 421))
        )
        
        self.md_threat_level_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(380, 60, 311, 31)),
            font=self.THREAT_FONT,
            text="THREAT LEVEL"
        )
        self.md_threat_level_title.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.md_threat_level_title.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.md_threat_level_title.setStyleSheet("""background-color:#393E46;
                                                color: #EEEEEE;""")
        
        
        self.md_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(330, 106, 421, 1))
        )
        
        self.md_detail_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(320, 120, 141, 24)),
            font=self.TITLE_FONT,
            text="Other Information"
        )
        
        self.md_inf_glayout_widget, self.md_inf_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(330, 150, 431, 127)))
        
        
        
        self.md_detail_url_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            text="URL"
        )
        
        self.md_detail_url_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
        )
        
        self.md_detail_source_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            text="Source"
        )
        
        self.md_detail_source_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
        )
        
        self.md_detail_type_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            text="Type"
        )
        
        self.md_detail_type_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
        )
        
        self.md_detail_date_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            text="Date"
        )
        
        self.md_detail_date_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
        )
        
        self.md_detail_desc_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=self.LABEL_FONT,
            text="Description"
        )
        
        self.md_detail_desc_label = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(350, 290, 391, 161)),
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR,
        )
        self.md_detail_desc_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.md_second_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(330, 480, 421, 1))
        )
        
        self.md_data_update_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(70, 490, 191, 27)),
            text="Update Data",
            on_click=(self.updateData)
        )
        
        self.md_source_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(450, 490, 191, 27)),
            text="USOM Source",
        )
        self.md_source_button.setEnabled(False)
        
        self.md_detail_colon1 = qlabel_generator.create_label(
            parent=self,
            font=self.LABEL_FONT,
            text=":"
        )
        self.md_detail_colon2 = qlabel_generator.create_label(
            parent=self,
            font=self.LABEL_FONT,
            text=":"
        )
        self.md_detail_colon3 = qlabel_generator.create_label(
            parent=self,
            font=self.LABEL_FONT,
            text=":"
        )
        self.md_detail_colon4 = qlabel_generator.create_label(
            parent=self,
            font=self.LABEL_FONT,
            text=":"
        )
        self.md_detail_colon5 = qlabel_generator.create_label(
            parent=self,
            font=self.LABEL_FONT,
            text=":"
        )
        
        self.md_detail_desc_title.setFixedWidth(80)
        
        self.md_inf_glayout.addWidget(self.md_detail_url_title,0, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon1,0, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_url_label,0, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_source_title,1, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon2,1, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_source_label,1, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_type_title,2, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon3,2, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_type_label,2, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_date_title,3, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon4,3, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_date_label,3, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_desc_title,4, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon5,4, 1, 1, 1)
        self.md_mal_data_list.itemSelectionChanged.connect(
            lambda: self.fillMalDetails(self.md_mal_data_list.selectedItems()))
        

        
        

    def fillMalList(self):
        try:
            self.md_mal_data_list.clear()
            self.md_mal_data_list.clearSelection()
            mal_urls = db_operations.get_data_by_column_name(
                column_name="url", table_name="malicious_data")
            for row in mal_urls:
                mal_url = QtWidgets.QListWidgetItem(str(row[0]))
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
                    lambda: helper_methods.openCustomWebPage(sel_mal_item_detail[9]))

                self.md_detail_url_label.setText(sel_mal_item_detail[3])
                self.md_detail_type_label.setText(sel_mal_item_detail[4])
                self.md_detail_desc_label.setText(sel_mal_item_detail[5])
                if sel_mal_item_detail[6] <= 3:
                    self.md_mal_data_list.setStyleSheet(
                        mal_data_styles.low_level_style)
                    self.md_threat_level_title.setText("LOW")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #23B7E5;color:white;")
                elif 4 <= sel_mal_item_detail[6] <= 7:
                    self.md_mal_data_list.setStyleSheet(
                        mal_data_styles.medium_level_style)
                    self.md_threat_level_title.setText("MEDIUM")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #FF902B;color:white;")
                else:
                    self.md_mal_data_list.setStyleSheet(
                        mal_data_styles.high_level_style)
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
