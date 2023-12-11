from PyQt6 import QtCore, QtWidgets
from styles.components_styles import qfonts_styles, qlabels_styles, qtreewidget_styles
from styles.ui_styles import default_styles
from features import workers
from ui.components import qtreewidget_generator, qlabel_generator, qlayout_qwidget_generator, qframe_line_generator, qpushbutton_logo_generator
from db import db_operations
from ui.loading_ui import loading_ui
from ui.input_dialog_ui import input_dialog_ui
from ui.loading_ui import loading_ui


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
            icon_name='single_left',
            enabled=False)

        self.bd_block_all_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='double_left',
            enabled=False)

        self.bd_unblock_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='single_right',
            enabled=False)

        self.bd_unblock_all_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='double_right',
            enabled=False)

        self.bd_add_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='add',
            on_click=self.show_input_dialog)

        self.bd_remove_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='trash',
            enabled=False)

        self.bd_unblocked_tree = qtreewidget_generator.create_tree_widget(
            parent=self,
            geometry=(QtCore.QRect(457, 30, 281, 360)),
            headerlabel="Unblocked Data List")

        self.bd_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(48, 400, 672, 1)))

        self.bd_inf_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 410, 141, 24)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text="Other Informations")

        self.bd_inf_glayout_widget, self.bd_inf_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(40, 440, 670, 75)))

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

        self.bd_inf_glayout.addWidget(self.bd_address_title, 0, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon1, 0, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_address_label, 0, 2, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_current_stat_title, 1, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon2, 1, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_current_stat_label, 1, 2, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_op_time_title, 2, 0, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_colon3, 2, 1, 1, 1)
        self.bd_inf_glayout.addWidget(self.bd_op_time_label, 2, 2, 1, 1)

        self.bd_blocked_tree.itemSelectionChanged.connect(
            lambda: self.fill_details(
                self.bd_blocked_tree.selectedItems(), "blocked_list"))

        self.bd_unblocked_tree.itemSelectionChanged.connect(
            lambda: self.fill_details(
                self.bd_unblocked_tree.selectedItems(), "unblocked_list"))

        self.bd_unblock_all_button.clicked.connect(
            lambda: self.create_worker(
                sender="unblock_all_button"))

        self.bd_block_all_button.clicked.connect(
            lambda: self.create_worker(
                sender="block_all_button"))

    def fill_lists(self):
        self.bd_blocked_tree.clear()
        self.bd_unblocked_tree.clear()

        blocked_ips = []
        blocked_domains = []
        unblocked_ips = []
        unblocked_domains = []

        data = db_operations.get_data_by_column_name(
            column_name='address,current_status,data_type')

        if data:
            for entry in data:
                addr = entry['address']
                data_type = entry['data_type']
                current_status = entry['current_status']

                if data_type == 'ip':
                    if current_status == 'blocked':
                        blocked_ips.append(addr)
                    else:
                        unblocked_ips.append(addr)

                else:
                    if current_status == 'blocked':
                        blocked_domains.append(addr)
                    else:
                        unblocked_domains.append(addr)

            blocked_ips.sort()
            blocked_domains.sort()
            unblocked_ips.sort()
            unblocked_domains.sort()

            sorted_blocked_data = blocked_ips + blocked_domains
            sorted_unblocked_data = unblocked_ips + unblocked_domains

            for entry in sorted_blocked_data:
                QtWidgets.QTreeWidgetItem(self.bd_blocked_tree, [entry])
            for entry in sorted_unblocked_data:
                QtWidgets.QTreeWidgetItem(self.bd_unblocked_tree, [entry])

        self.set_button_states()

    def fill_details(self, sel_items, sender):
        self.bd_block_button.setEnabled(False)
        self.bd_unblock_button.setEnabled(False)
        self.bd_remove_button.setEnabled(False)

        self.bd_address_label.clear()
        self.bd_op_time_label.clear()
        self.bd_current_stat_label.clear()

        if sel_items:
            sel_item = sel_items[0]
            entry = db_operations.get_entry_details(
                column_name='*',
                address=sel_item.text(0))

            if entry:

                self.bd_remove_button.disconnect()
                self.bd_remove_button.setEnabled(True)
                self.bd_remove_button.clicked.connect(lambda: self.create_worker(
                    entry=entry,
                    sender='remove_button'
                ))

                if sender == "blocked_list":
                    self.bd_unblock_button.disconnect()
                    self.bd_unblocked_tree.clearSelection()
                    self.bd_unblock_button.setEnabled(True)
                    self.bd_block_button.setEnabled(False)
                    self.bd_unblock_button.clicked.connect(
                        lambda: self.create_worker(
                            entry=entry,
                            sender="unblock_button"))

                elif sender == "unblocked_list":
                    self.bd_block_button.disconnect()
                    self.bd_blocked_tree.clearSelection()
                    self.bd_unblock_button.setEnabled(False)
                    self.bd_block_button.setEnabled(True)
                    self.bd_block_button.clicked.connect(
                        lambda: self.create_worker(
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

    def create_worker(self, sender, entry=None):
        my_blocking_op_worker = workers.BlockingOperationsWorker(
            entry=entry,
            sender=sender)

        if sender.find("all") != -1:
            my_loading_ui = loading_ui.UiLoading()
            my_loading_ui.show()
            my_blocking_op_worker.finished.connect(
                lambda: my_loading_ui.deleteLater())

        if sender == 'remove_button':
            address = entry['address']
            my_blocking_op_worker.finished.connect(
                lambda: db_operations.remove_entry(address=address))

        my_blocking_op_worker.finished.connect(self.fill_lists)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.wait)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.quit)
        my_blocking_op_worker.start()

    def set_button_states(self):
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

    def show_input_dialog(self):
        self.my_input_dialog = input_dialog_ui.UiInputWidget()
        self.my_input_dialog.show()
        self.my_input_dialog.data_processed.connect(self.fill_lists)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main_window = BlockedDataPageWidget()
    main_window.fill_lists()
    main_window.show()

    app.exec()
