from PyQt6 import QtCore, QtGui, QtWidgets
from styles.components_styles import qfonts_styles, qlabels_styles, qtreewidget_styles
from styles.ui_styles import default_styles
from features import blocking_operations, workers
from ui.components import qtreewidget_generator, qlabel_generator, qlayout_qwidget_generator, qpushbutton_generator, qframe_line_generator, qpushbutton_logo_generator
from db import db_operations
from ui.loading_ui import loading_ui

import os


class BlockedDataPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(default_styles.dark_style)

        self.qtreew_style = qtreewidget_styles.create_qtreew_style()
        self.b_qtreew_style = qtreewidget_styles.create_qtreew_style("blocked")
        self.u_qtreew_style = qtreewidget_styles.create_qtreew_style(
            "unblocked")

        self.bd_blocked_tree = qtreewidget_generator.create_tree_widget(
            parent=self,
            geometry=(QtCore.QRect(30, 30, 281, 360)),
            headerlabel="Blocked Data List")

        self.bd_buttons_vlayout_widget, self.bd_buttons_vlayout = qlayout_qwidget_generator.create_vlayout_widget(
            parent=self,
            geometry=(QtCore.QRect(341, 150, 86, 166)))

        self.bd_block_sel_data_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='single_left')
        self.bd_block_sel_data_button.setEnabled(False)

        self.bd_block_all_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='double_left')
        self.bd_block_all_button.setEnabled(False)

        self.bd_unblock_sel_data_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='single_right')
        self.bd_unblock_sel_data_button.setEnabled(False)

        self.bd_unblock_all_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='double_right')
        self.bd_unblock_all_button.setEnabled(False)

        self.bd_add_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='add')
        self.bd_add_button.setEnabled(False)

        self.bd_remove_sel_data_item = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='trash')
        self.bd_remove_sel_data_item.setEnabled(False)

        self.bd_unblocked_tree = qtreewidget_generator.create_tree_widget(
            parent=self,
            geometry=(QtCore.QRect(457, 30, 281, 360)),
            headerlabel="Unblocked Data List")

        self.bd_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(48, 400, 672, 1))

        )

        self.bd_inf_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 410, 141, 24)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Other Information")

        self.bd_inf_glayout_widget, self.bd_inf_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(40, 440, 670, 75))
        )

        self.bd_url_title = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="URL")

        self.bd_url_label = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,
            copyable=True)

        self.bd_op_time_title = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Operation Time")

        self.bd_op_time_label = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,)

        self.bd_current_stat_title = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Current Status")

        self.bd_current_stat_label = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.label_color,)

        self.bd_colon1 = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")
        self.bd_colon2 = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")
        self.bd_colon3 = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text=":")

        self.bd_buttons_vlayout.addWidget(self.bd_block_sel_data_button)
        self.bd_buttons_vlayout.addWidget(self.bd_block_all_button)
        self.bd_buttons_vlayout.addWidget(self.bd_unblock_sel_data_button)
        self.bd_buttons_vlayout.addWidget(self.bd_unblock_all_button)
        self.bd_buttons_vlayout.addWidget(self.bd_add_button)
        self.bd_buttons_vlayout.addWidget(self.bd_remove_sel_data_item)

        self.bd_inf_glayout.addWidget(self.bd_url_label, 0, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon1, 0, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_url_label, 0, 2, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_op_time_title, 1, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon2, 1, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_op_time_label, 1, 2, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_current_stat_title, 2, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon3, 2, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_current_stat_label, 2, 2, 1, 1)

        self.bd_blocked_tree.itemSelectionChanged.connect(
            lambda: self.fillBlockedDetail(
                self.bd_blocked_tree.selectedItems(), "blocked_list"))
        self.bd_unblocked_tree.itemSelectionChanged.connect(
            lambda: self.fillBlockedDetail(
                self.bd_unblocked_tree.selectedItems(), "unblocked_list"))

        self.bd_unblock_all_button.clicked.connect(
            lambda: self.perform_blocking_operations(
                sender="unblock_all_button"))

        self.bd_block_all_button.clicked.connect(
            lambda: self.perform_blocking_operations(
                sender="block_all_button"))

    def fillBlockedList(self):
        self.bd_blocked_tree.clear()
        self.bd_unblocked_tree.clear()
        self.bd_blocked_tree.clearSelection()
        self.bd_unblocked_tree.clearSelection()

        blocked_data_ip = db_operations.custom_query(
            "SELECT url, current_status FROM blocked_data WHERE data_type='ip' ORDER BY url ASC")

        blocked_data_domain = db_operations.custom_query(
            "SELECT url,current_status FROM blocked_data where data_type='domain' ORDER BY url ASC")

        if blocked_data_ip:
            for row in blocked_data_ip:
                url, current_status = row[0], row[1]

                if current_status == "blocked":
                    QtWidgets.QTreeWidgetItem(
                        self.bd_blocked_tree, [url])
                else:
                    QtWidgets.QTreeWidgetItem(
                        self.bd_unblocked_tree, [url])

        if blocked_data_domain:
            for row in blocked_data_domain:
                url, current_status = row[0], row[1]

                if current_status == "blocked":
                    QtWidgets.QTreeWidgetItem(
                        self.bd_blocked_tree, [url])
                else:
                    QtWidgets.QTreeWidgetItem(
                        self.bd_unblocked_tree, [url])

        self.set_buttons_status()

    def set_buttons_status(self):
        if self.bd_blocked_tree.topLevelItemCount() == 0:
            self.bd_block_all_button.setEnabled(True)
            self.bd_unblock_all_button.setEnabled(False)
        elif self.bd_unblocked_tree.topLevelItemCount() == 0:
            self.bd_unblock_all_button.setEnabled(True)
            self.bd_block_all_button.setEnabled(False)
        elif self.bd_unblocked_tree.topLevelItemCount() == 0 and self.bd_blocked_tree.topLevelItemCount() == 0:
            self.bd_unblock_all_button.setEnabled(False)
            self.bd_block_all_button.setEnabled(False)
        else:
            self.bd_unblock_all_button.setEnabled(True)
            self.bd_block_all_button.setEnabled(True)

    def fillBlockedDetail(self, sel_blocked_item, sender):
        if sel_blocked_item:
            sel_blocked_item = sel_blocked_item[0]

            sel_blocked_item_detail = db_operations.get_one_data_detail(
                column_name="*", condition_column='url', condition_value=sel_blocked_item.text(0), table_name='blocked_data')

            if sender == "blocked_list":
                self.bd_unblock_sel_data_button.disconnect()
                self.bd_unblocked_tree.clearSelection()
                self.bd_unblock_sel_data_button.setEnabled(True)
                self.bd_block_sel_data_button.setEnabled(False)
                self.bd_unblock_sel_data_button.clicked.connect(
                    lambda: self.perform_blocking_operations(
                        item=sel_blocked_item_detail,
                        sender="unblock_button"))

            elif sender == "unblocked_list":
                self.bd_block_sel_data_button.disconnect()
                self.bd_blocked_tree.clearSelection()
                self.bd_unblock_sel_data_button.setEnabled(False)
                self.bd_block_sel_data_button.setEnabled(True)
                self.bd_block_sel_data_button.clicked.connect(
                    lambda: self.perform_blocking_operations(
                        item=sel_blocked_item_detail,
                        sender="block_button"))

            self.bd_url_label.setText(
                sel_blocked_item_detail[1])
            self.bd_op_time_label.setText(
                sel_blocked_item_detail[3])
            self.bd_current_stat_label.setText(
                sel_blocked_item_detail[4])
            if sel_blocked_item_detail[4] == "blocked":
                self.bd_blocked_tree.setStyleSheet(self.b_qtreew_style)
                self.bd_current_stat_label.setStyleSheet(
                    "color:#23B7E5;")
            elif sel_blocked_item_detail[4] == "unblocked":
                self.bd_unblocked_tree.setStyleSheet(self.u_qtreew_style)
                self.bd_current_stat_label.setStyleSheet(
                    "color:#F05050;")

    def clear_all_details(self):
        self.bd_url_label.clear()
        self.bd_op_time_label.clear()
        self.bd_current_stat_label.clear()

    def perform_blocking_operations(self, sender, item=None):
        try:
            my_blocking_op_worker = workers.BlockingOperationWorker(
                item=item,
                sender=sender)

            if sender.find("all") != -1:
                my_loading_ui = loading_ui.UiLoading()
                my_loading_ui.show()
                my_blocking_op_worker.finished.connect(
                    lambda: my_loading_ui.deleteLater())

            my_blocking_op_worker.finished.connect(self.fillBlockedList)
            my_blocking_op_worker.finished.connect(my_blocking_op_worker.wait)
            my_blocking_op_worker.finished.connect(my_blocking_op_worker.quit)

            my_blocking_op_worker.start()
        except Exception as e:
            print(f"Error perform_blocking_operations(bd): {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = BlockedDataPageWidget()
    main_window.show()
    main_window.fillBlockedList()
    sys.exit(app.exec())
