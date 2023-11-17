from PyQt6 import QtCore, QtGui, QtWidgets
from db import db_operations
from ui.components import qlabel_generator, qpushbutton_generator, qframe_line_generator, qtreewidget_generator, qlayout_qwidget_generator
from styles.components_styles import qfonts_styles, qlabels_styles, qtreewidget_styles
from styles.ui_styles import default_styles
from features import helper_methods, workers
from ui.loading_ui import loading_ui
from ui.information_ui import information_ui


class MalDataPageWidget(QtWidgets.QWidget):

    def __init__(self, my_blocked_data_page):
        self.my_blocked_data_page = my_blocked_data_page
        super().__init__()

        self.initUI()

    def initUI(self):
        self.md_mal_data_tree = qtreewidget_generator.create_tree_widget(
            parent=self,
            geometry=(QtCore.QRect(30, 30, 281, 421)),
            headerlabel="Received Malicious Data")

        self.qtreew_style = qtreewidget_styles.create_qtreew_style()
        self.l_qtreew_style = qtreewidget_styles.create_qtreew_style("low")
        self.m_qtreew_style = qtreewidget_styles.create_qtreew_style("medium")
        self.h_qtreew_style = qtreewidget_styles.create_qtreew_style("high")

        self.md_threat_level_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(380, 30, 311, 31)),
            font=qfonts_styles.threat_font,
            color=qlabels_styles.title_color,
            text="THREAT LEVEL"
        )
        self.md_threat_level_title.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.md_threat_level_title.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.md_threat_level_title.setStyleSheet(
            qlabels_styles.md_threat_level_title)
        self.md_threat_level_title.setFixedWidth(311)

        self.md_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(330, 70, 421, 1))
        )

        self.md_detail_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(320, 90, 141, 24)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Other Information"
        )

        self.md_inf_glayout_widget, self.md_inf_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(330, 120, 421, 127)))

        self.md_detail_url_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="URL")

        self.md_detail_url_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            copyable=True)

        self.md_detail_source_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Source")

        self.md_detail_source_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color)

        self.md_detail_type_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Type")

        self.md_detail_type_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color)

        self.md_detail_date_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Date")

        self.md_detail_date_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color)

        self.md_detail_desc_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Description")

        self.md_detail_desc_label = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            wordwrap=True,
            copyable=True)
        self.md_detail_desc_label.setGeometry(
            QtCore.QRect(350, 260, 391, 161)),
        self.md_detail_desc_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)

        self.md_second_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(330, 450, 421, 1)))

        self.md_data_update_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(70, 471, 191, 27)),
            text="Update Data",
            on_click=(self.updateData))

        self.md_source_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(450, 471, 191, 27)),
            text="USOM Source")
        self.md_source_button.setEnabled(False)

        self.md_detail_colon1 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.md_detail_colon2 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.md_detail_colon3 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.md_detail_colon4 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")
        self.md_detail_colon5 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.md_inf_glayout.addWidget(self.md_detail_url_title, 0, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon1, 0, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_url_label, 0, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_source_title, 1, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon2, 1, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_source_label, 1, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_type_title, 2, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon3, 2, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_type_label, 2, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_date_title, 3, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon4, 3, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_date_label, 3, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_desc_title, 4, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_detail_colon5, 4, 1, 1, 1)

        self.md_mal_data_tree.itemSelectionChanged.connect(
            lambda: self.fillMalDetails(self.md_mal_data_tree.selectedItems()))

    def fillMalList(self):

        self.md_mal_data_tree.clear()
        self.md_mal_data_tree.clearSelection()
        mal_data = db_operations.get_data_by_column_name(
            column_name="url,data_type", table_name="malicious_data")
        category_items = {}
        for row in mal_data:
            url, data_type = row[0], row[1]

            if data_type not in category_items:
                if data_type == "ip":
                    category_item = QtWidgets.QTreeWidgetItem(
                        self.md_mal_data_tree, ["Malicious IPs"])
                else:
                    category_item = QtWidgets.QTreeWidgetItem(
                        self.md_mal_data_tree, ["Malicious Domains"])
                category_items[data_type] = category_item

            QtWidgets.QTreeWidgetItem(
                category_items[data_type], [url])

        self.md_mal_data_tree.sortItems(
            0,  QtCore.Qt.SortOrder.AscendingOrder)

    def fillMalDetails(self, sel_mal_items):
        if sel_mal_items:
            sel_mal_item = sel_mal_items[0]
            if sel_mal_item.parent() is not None:
                sel_mal_item_detail = db_operations.get_one_data_detail(
                    column_name="*", condition_column='url', condition_value=sel_mal_item.text(0), table_name='malicious_data')
                self.md_source_button.setEnabled(True)
                self.md_source_button.disconnect()
                self.md_source_button.clicked.connect(
                    lambda: helper_methods.open_custom_page(sel_mal_item_detail[9]))

                self.md_detail_url_label.setText(sel_mal_item_detail[3])
                self.md_detail_type_label.setText(sel_mal_item_detail[4])
                self.md_detail_desc_label.setText(sel_mal_item_detail[5])
                if sel_mal_item_detail[6] <= 3:
                    self.md_mal_data_tree.setStyleSheet(
                        self.l_qtreew_style)
                    self.md_threat_level_title.setText("LOW")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #23B7E5;color:white;")
                elif 4 <= sel_mal_item_detail[6] <= 7:
                    self.md_mal_data_tree.setStyleSheet(
                        self.m_qtreew_style)
                    self.md_threat_level_title.setText("MEDIUM")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #FF902B;color:white;")
                else:
                    self.md_mal_data_tree.setStyleSheet(
                        self.h_qtreew_style)
                    self.md_threat_level_title.setText("HIGH")
                    self.md_threat_level_title.setStyleSheet(
                        "background-color: #F05050;color:white;")
                self.md_detail_source_label.setText(sel_mal_item_detail[7])
                self.md_detail_date_label.setText(sel_mal_item_detail[8])
            else:
                self.md_mal_data_tree.setStyleSheet(self.qtreew_style)
                self.clear_all_details()
    
    def clear_all_details(self):
        self.md_detail_url_label.clear()
        self.md_detail_source_label.clear()
        self.md_detail_type_label.clear()
        self.md_detail_date_label.clear()
        self.md_detail_desc_label.clear()
        
    def updateData(self):
        my_loading_ui = loading_ui.UiLoading()
        my_loading_ui.show()
        my_update_data_worker = workers.UpdateDataWorker(
            my_loading_ui=my_loading_ui)
        my_update_data_worker.finished.connect(my_update_data_worker.wait)
        my_update_data_worker.finished.connect(my_update_data_worker.quit)
        my_update_data_worker.finished.connect(self.fillMalList)
        my_update_data_worker.finished.connect(
            self.my_blocked_data_page.fillBlockedList)
        my_update_data_worker.finished.connect(my_loading_ui.deleteLater)
        my_update_data_worker.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main_window = MalDataPageWidget()
    main_window.show()

    app.exec()
