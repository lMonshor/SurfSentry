from PyQt6 import QtCore, QtWidgets
from db import db_operations
from ui.components import qlabel_generator, qpushbutton_generator, qframe_line_generator, qtreewidget_generator, qlayout_qwidget_generator
from styles.components_styles import qfonts_styles, qlabels_styles, qtreewidget_styles
from features import helper_methods, workers
from ui.loading_ui import loading_ui
from styles.ui_styles import default_styles


class MalDataPageWidget(QtWidgets.QWidget):

    def __init__(self, my_blocked_data_page, my_general_page):
        self.my_blocked_data_page = my_blocked_data_page
        self.my_general_page = my_general_page
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setStyleSheet(default_styles.dark_style)
        self.md_tree = qtreewidget_generator.create_tree_widget(
            parent=self,
            geometry=(QtCore.QRect(30, 30, 281, 421)),
            headerlabel="Received Malicious Data")

        self.qtreew_style = qtreewidget_styles.create_qtreew_style()
        self.l_qtreew_style = qtreewidget_styles.create_qtreew_style("low")
        self.m_qtreew_style = qtreewidget_styles.create_qtreew_style("medium")
        self.h_qtreew_style = qtreewidget_styles.create_qtreew_style("high")

        self.md_severity_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(380, 30, 311, 31)),
            font=qfonts_styles.threat_font,
            color=qlabels_styles.title_color,
            text='Not avaliable'
        )
        self.md_severity_title.setFrameShadow(
            QtWidgets.QFrame.Shadow.Plain)
        self.md_severity_title.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.md_severity_title.setStyleSheet(
            qlabels_styles.md_threat_title_style)
        self.md_severity_title.setFixedWidth(311)

        self.md_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(330, 70, 421, 1))
        )

        self.md_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(320, 90, 141, 24)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Other Information"
        )

        self.md_inf_glayout_widget, self.md_inf_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(330, 120, 421, 127)))

        self.md_address_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Address")

        self.md_address = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            copyable=True)

        self.md_source_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Source")

        self.md_source_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color)

        self.md_type_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Type")

        self.md_type_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color)

        self.md_date_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Date")

        self.md_date_label = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color)

        self.md_desc_title = qlabel_generator.create_label(
            parent=self.md_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Description")

        self.md_desc_label = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            wordwrap=True,
            copyable=True)
        self.md_desc_label.setGeometry(
            QtCore.QRect(350, 260, 391, 161)),
        self.md_desc_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)

        self.md_second_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(330, 450, 421, 1)))

        self.md_data_update_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(70, 471, 191, 27)),
            text="Update Data",
            on_click=(self.create_worker))

        self.md_source_button = qpushbutton_generator.create_button(
            parent=self,
            geometry=(QtCore.QRect(450, 471, 191, 27)),
            text="USOM Source")
        self.md_source_button.setEnabled(False)

        self.md_colon1 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.md_colon2 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.md_colon3 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.md_colon4 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")
        self.md_colon5 = qlabel_generator.create_label(
            parent=self,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.md_inf_glayout.addWidget(self.md_address_title, 0, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_colon1, 0, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_address, 0, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_source_title, 1, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_colon2, 1, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_source_label, 1, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_type_title, 2, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_colon3, 2, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_type_label, 2, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_date_title, 3, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_colon4, 3, 1, 1, 1)
        self.md_inf_glayout.addWidget(self.md_date_label, 3, 2, 1, 1)
        self.md_inf_glayout.addWidget(self.md_desc_title, 4, 0, 1, 1)
        self.md_inf_glayout.addWidget(self.md_colon5, 4, 1, 1, 1)

        self.md_tree.itemSelectionChanged.connect(
            lambda: self.fill_details(self.md_tree.selectedItems()))

    def fill_lists(self):
        self.md_tree.clear()

        data = db_operations.get_data_by_column_name(
            column_name="address,data_type")
        category_items = {}

        if data:
            for entry in data:

                if entry['data_type'] not in category_items:
                    if entry['data_type'] == "ip":
                        category_item = QtWidgets.QTreeWidgetItem(
                            self.md_tree, ["Malicious IPs"])
                    else:
                        category_item = QtWidgets.QTreeWidgetItem(
                            self.md_tree, ["Malicious Domains"])
                    category_items[entry['data_type']] = category_item

                QtWidgets.QTreeWidgetItem(
                    category_items[entry['data_type']], [entry['address']])

            self.md_tree.sortItems(
                0,  QtCore.Qt.SortOrder.AscendingOrder)
        
        self.my_general_page.fill_fields()

    def fill_details(self, sel_items):
        self.clear_all_details()
        if sel_items:
            sel_item = sel_items[0]
            if sel_item.parent() is not None:
                entry = db_operations.get_entry_details(
                    column_name='*',
                    address=sel_item.text(0))

                if entry:
                    self.md_source_button.setEnabled(True)
                    self.md_source_button.disconnect()
                    self.md_source_button.clicked.connect(
                        lambda: helper_methods.open_custom_page(entry['link']))
                    self.md_address.setText(entry['address'])
                    self.md_type_label.setText(entry['mal_type'])
                    self.md_desc_label.setText(entry['desc'])

                    if entry['severity'] <= 3:
                        self.md_tree.setStyleSheet(
                            self.l_qtreew_style)
                        self.md_severity_title.setText("LOW")
                        self.md_severity_title.setStyleSheet(
                            qlabels_styles.md_threat_title_low_style)

                    elif 4 <= entry['severity'] <= 7:
                        self.md_tree.setStyleSheet(
                            self.m_qtreew_style)
                        self.md_severity_title.setText("MEDIUM")
                        self.md_severity_title.setStyleSheet(
                            qlabels_styles.md_threat_title_medium_style)

                    else:
                        self.md_tree.setStyleSheet(
                            self.h_qtreew_style)
                        self.md_severity_title.setText("HIGH")
                        self.md_severity_title.setStyleSheet(
                            qlabels_styles.md_threat_title_high_style)

                    self.md_source_label.setText(entry['source'])
                    self.md_date_label.setText(entry['data_date'])

        else:
            self.md_tree.setStyleSheet(self.qtreew_style)

    def clear_all_details(self):
        self.md_address.clear()
        self.md_source_label.clear()
        self.md_type_label.clear()
        self.md_date_label.clear()
        self.md_desc_label.clear()
        self.md_severity_title.setText('Not avaliable')
        self.md_severity_title.setStyleSheet(
            qlabels_styles.md_threat_title_style)

    def create_worker(self):
        my_loading_ui = loading_ui.UiLoading()
        my_loading_ui.show()
        my_update_data_worker = workers.UpdateDataWorker(
            my_loading_ui=my_loading_ui)
        my_update_data_worker.finished.connect(my_update_data_worker.wait)
        my_update_data_worker.finished.connect(my_update_data_worker.quit)
        my_update_data_worker.finished.connect(self.fill_lists)
        my_update_data_worker.finished.connect(my_loading_ui.deleteLater)
        my_update_data_worker.finished.connect(
            self.my_blocked_data_page.fill_lists)
        my_update_data_worker.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main_window = MalDataPageWidget()
    main_window.fill_lists()
    main_window.show()

    app.exec()
