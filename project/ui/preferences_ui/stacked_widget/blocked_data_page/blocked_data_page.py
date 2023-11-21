from PyQt6 import QtCore, QtGui, QtWidgets
from styles.components_styles import qfonts_styles, qlabels_styles, qtreewidget_styles
from styles.ui_styles import default_styles
from features import blocking_operations, workers
from ui.components import qtreewidget_generator, qlabel_generator, qlayout_qwidget_generator, qpushbutton_generator, qframe_line_generator, qpushbutton_logo_generator
from db import db_operations
from ui.loading_ui import loading_ui
from ui.preferences_ui.stacked_widget.blocked_data_page.input_dialog_ui import input_dialog_ui

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

        self.bd_block_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='single_left')
        self.bd_block_button.setEnabled(False)

        self.bd_block_all_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='double_left')
        self.bd_block_all_button.setEnabled(False)

        self.bd_unblock_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='single_right')
        self.bd_unblock_button.setEnabled(False)

        self.bd_unblock_all_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='double_right')
        self.bd_unblock_all_button.setEnabled(False)

        self.bd_add_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='add',
            on_click=self.add_data)

        self.bd_remove_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='trash')
        self.bd_remove_button.setEnabled(False)

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

        self.bd_address_title = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=qfonts_styles.subtitle_font,
            color=qlabels_styles.title_color,
            text="Address")

        self.bd_address_label = qlabel_generator.create_label(
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

        self.bd_buttons_vlayout.addWidget(self.bd_block_button)
        self.bd_buttons_vlayout.addWidget(self.bd_block_all_button)
        self.bd_buttons_vlayout.addWidget(self.bd_unblock_button)
        self.bd_buttons_vlayout.addWidget(self.bd_unblock_all_button)
        self.bd_buttons_vlayout.addWidget(self.bd_add_button)
        self.bd_buttons_vlayout.addWidget(self.bd_remove_button)

        self.bd_inf_glayout.addWidget(self.bd_address_label, 0, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon1, 0, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_address_label, 0, 2, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_op_time_title, 1, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon2, 1, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_op_time_label, 1, 2, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_current_stat_title, 2, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon3, 2, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_current_stat_label, 2, 2, 1, 1)

        self.bd_blocked_tree.itemSelectionChanged.connect(
            lambda: self.fill_blocked_details(
                self.bd_blocked_tree.selectedItems(), "blocked_list"))

        self.bd_unblocked_tree.itemSelectionChanged.connect(
            lambda: self.fill_blocked_details(
                self.bd_unblocked_tree.selectedItems(), "unblocked_list"))

        self.bd_unblock_all_button.clicked.connect(
            lambda: self.perform_blocking_operations(
                sender="unblock_all_button"))

        self.bd_block_all_button.clicked.connect(
            lambda: self.perform_blocking_operations(
                sender="block_all_button"))

    def fill_blocked_list(self):
        self.bd_blocked_tree.clear()
        self.bd_unblocked_tree.clear()
        self.bd_blocked_tree.clearSelection()
        self.bd_unblocked_tree.clearSelection()

        ip_addresses = db_operations.get_data_by_specified_condition(
            column_name='address,current_status',
            condition_column='data_type',
            condition_value='"ip" ORDER BY address ASC')

        domain_addresses = db_operations.get_data_by_specified_condition(
            column_name='address,current_status',
            condition_column='data_type',
            condition_value='"domain" ORDER BY address ASC')

        self.populate_tree_widget(
            ip_addresses, self.bd_blocked_tree, self.bd_unblocked_tree)
        self.populate_tree_widget(
            domain_addresses, self.bd_blocked_tree, self.bd_unblocked_tree)

    def populate_tree_widget(self, addresses, blocked_tree, unblocked_tree):
        if addresses:
            for entry in addresses:
                address, current_status = entry['address'], entry['current_status']
                tree_widget = blocked_tree if current_status == "blocked" else unblocked_tree
                QtWidgets.QTreeWidgetItem(tree_widget, [address])

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

    def fill_blocked_details(self, sel_items, sender):
        if sel_items:
            sel_item = sel_items[0]
            entry = db_operations.get_entry_details(
                column_name='*',
                address=sel_item.text(0))

            if sender == "blocked_list":
                self.bd_unblock_button.disconnect()
                self.bd_unblocked_tree.clearSelection()
                self.bd_unblock_button.setEnabled(True)
                self.bd_block_button.setEnabled(False)
                self.bd_unblock_button.clicked.connect(
                    lambda: self.perform_blocking_operations(
                        entry=entry,
                        sender="unblock_button"))

            elif sender == "unblocked_list":
                self.bd_block_button.disconnect()
                self.bd_blocked_tree.clearSelection()
                self.bd_unblock_button.setEnabled(False)
                self.bd_block_button.setEnabled(True)
                self.bd_block_button.clicked.connect(
                    lambda: self.perform_blocking_operations(
                        entry=entry,
                        sender="block_button"))

            self.bd_address_label.setText(
                entry['address'])
            self.bd_op_time_label.setText(
                entry['operation_time'])
            self.bd_current_stat_label.setText(
                entry['current_status'])
            if entry['current_status'] == "blocked":
                self.bd_blocked_tree.setStyleSheet(self.b_qtreew_style)
                self.bd_current_stat_label.setStyleSheet(
                    "color:#23B7E5;")
            elif entry['current_status'] == "unblocked":
                self.bd_unblocked_tree.setStyleSheet(self.u_qtreew_style)
                self.bd_current_stat_label.setStyleSheet(
                    "color:#F05050;")

    def clear_all_details(self):
        self.bd_address_label.clear()
        self.bd_op_time_label.clear()
        self.bd_current_stat_label.clear()

    def perform_blocking_operations(self, sender, entry=None):
        try:
            my_blocking_op_worker = workers.BlockingOperationsWorker(
                entry=entry,
                sender=sender)

            if sender.find("all") != -1:
                my_loading_ui = loading_ui.UiLoading()
                my_loading_ui.show()
                my_blocking_op_worker.finished.connect(
                    lambda: my_loading_ui.deleteLater())

            my_blocking_op_worker.finished.connect(self.fill_blocked_list)
            my_blocking_op_worker.finished.connect(my_blocking_op_worker.wait)
            my_blocking_op_worker.finished.connect(my_blocking_op_worker.quit)

            my_blocking_op_worker.start()
        except Exception as e:
            print(f"Error perform_blocking_operations(bd): {e}")

    def add_data(self):
        self.my_input_widget = input_dialog_ui.UiInputWidget()
        result = self.my_input_widget.exec()

        if result == QtWidgets.QDialog.DialogCode.Accepted:
            self.user_input = self.my_input_widget.input_line.text()
            self.check_user_input()

    def check_user_input(self):
        self.my_input_widget.hide()
        self.my_loading_ui = loading_ui.UiLoading()

        self.my_loading_ui.show()
        my_check_input_type_worker = workers.CheckInputTypeWorker(
            self.user_input)
        my_check_input_type_worker.finished.connect(self.handle_worker)
        my_check_input_type_worker.finished.connect(self.my_loading_ui.close)
        my_check_input_type_worker.finished.connect(
            my_check_input_type_worker.wait)
        my_check_input_type_worker.finished.connect(
            my_check_input_type_worker.quit)
        my_check_input_type_worker.start()

    def handle_worker(self, input_type):
        if input_type != "unknown":
            self.block_input(self.user_input, input_type)

        else:
            ok = QtWidgets.QMessageBox.warning(
                None, 'Warning', 'Input is not an IP or Domain')
            if ok:
                self.add_data()

    def block_input(self, user_input, input_type):
        entry = [user_input, input_type]
        my_blocking_op_worker = workers.BlockingOperationsWorker(
            entry=entry, sender="add_button")
        my_blocking_op_worker.finished.connect(lambda:
                                               self.show_messagebox())
        my_blocking_op_worker.finished.connect(self.fill_blocked_list)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.wait)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.quit)
        my_blocking_op_worker.start()

    def show_messagebox(self):
        QtWidgets.QMessageBox.information(
            None, 'Add', 'Succesfully Added')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main_window = BlockedDataPageWidget()
    main_window.show()
    main_window.fill_blocked_list()
    app.exec()
