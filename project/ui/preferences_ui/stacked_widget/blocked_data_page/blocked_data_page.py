from PyQt6 import QtCore, QtGui, QtWidgets
from styles.preferences_ui_styles.stacked_widget_styles import stacked_buttons_style, blocked_data_styles
from features import blocking_operations
from ui.components import qlistwidget_generator,qlabel_generator,qlayout_qwidget_generator,qpushbutton_generator,qframe_line_generator
from db import db_operations
import os


class BlockedDataPageWidget(QtWidgets.QWidget):
    TITLE_FONT = QtGui.QFont("Calibri", 14)
    LABEL_FONT = QtGui.QFont("Calibri", 12)
    LABEL_COLOR = "#777777"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #0f0f0f")
        self.bd_blocked_list_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(30, 29, 200, 24)),
            font=self.TITLE_FONT,
            text="Blocked Data List")
        
        self.bd_blocked_list = qlistwidget_generator.create_list_widget(
            parent=self,
            geometry=(QtCore.QRect(30, 59, 281, 331)))
        
        
        self.bd_buttons_vlayout_widget, self.bd_buttons_vlayout = qlayout_qwidget_generator.create_vlayout_widget(
            parent=self,
            geometry=(QtCore.QRect(341, 150, 86, 166)))
        
        self.bd_block_sel_data_button = qpushbutton_generator.create_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='single_left')
        self.bd_block_sel_data_button.setEnabled(False)
        
        self.bd_block_all_button = qpushbutton_generator.create_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='double_left')
        self.bd_block_all_button.setEnabled(False)
        
        self.bd_unblock_sel_data_button = qpushbutton_generator.create_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='single_right')
        self.bd_unblock_sel_data_button.setEnabled(False)
        
        self.bd_unblock_all_button = qpushbutton_generator.create_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='double_right')
        self.bd_unblock_all_button.setEnabled(False)
        
        self.bd_add_button = qpushbutton_generator.create_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='add')
        self.bd_add_button.setEnabled(False)
        
        self.bd_remove_sel_data_item = qpushbutton_generator.create_button(
            parent=self.bd_buttons_vlayout_widget,
            icon_name='trash')
        self.bd_remove_sel_data_item.setEnabled(False)
        
        self.bd_unblocked_list_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(457, 29, 200, 24)),
            font=self.TITLE_FONT,
            text="Unblocked Data List")
        
        self.bd_unblocked_list = qlistwidget_generator.create_list_widget(
            parent=self,
            geometry=(QtCore.QRect(457, 59, 281, 331)))
        
        
        self.bd_first_hline = qframe_line_generator.create_frame_line(
            parent=self,
            geometry=(QtCore.QRect(48, 400, 672, 1))
            
        )
        
        self.bd_inf_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect( 30, 410, 141, 24)),
            font=self.TITLE_FONT,
            text="Other Information")
        
        self.bd_inf_glayout_widget, self.bd_inf_glayout = qlayout_qwidget_generator.create_glayout_widget(
            parent=self,
            geometry=(QtCore.QRect(40, 440, 701, 75))
        )
        
        self.bd_url_title = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
            text="URL")
        
        self.bd_url_label = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR)
        
        self.bd_op_time_title = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
            text="Operation Time")
        
        self.bd_op_time_label = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR)
        
        self.bd_current_stat_title = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
            text="Current Status")
        self.bd_current_stat_title.setFixedWidth(110)
        
        self.bd_current_stat_label = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
            color=self.LABEL_COLOR)
        
        self.bd_colon1 = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
            text=":")
        self.bd_colon2 = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
            text=":")
        self.bd_colon3 = qlabel_generator.create_label(
            parent=self.bd_inf_glayout_widget,
            font=self.LABEL_FONT,
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
        
        self.bd_blocked_list.itemSelectionChanged.connect(lambda: self.fillBlockedDetail(
            self.bd_blocked_list.selectedItems(), "blocked_list"))
        self.bd_unblocked_list.itemSelectionChanged.connect(lambda: self.fillBlockedDetail(
            self.bd_unblocked_list.selectedItems(), "unblocked_list"))
        self.bd_unblock_all_button.clicked.connect(lambda: blocking_operations.block_unblock(
            control_toggle_button=None, selected_blocked_item_detail=None, sender="unblock_all_button", fillBlockedList=self.fillBlockedList))
        self.bd_block_all_button.clicked.connect(lambda: blocking_operations.block_unblock(
            control_toggle_button=None, selected_blocked_item_detail=None, sender="block_all_button", fillBlockedList=self.fillBlockedList))
        

    def fillBlockedList(self):
        try:
            self.bd_blocked_list.clear()
            self.bd_unblocked_list.clear()
            self.bd_blocked_list.clearSelection()
            self.bd_unblocked_list.clearSelection()

            blocked_data = db_operations.get_data_by_column_name(
                column_name="url,current_status", table_name="blocked_data")
            for row in blocked_data:
                blocked_current_state = row[1]
                blocked_url = QtWidgets.QListWidgetItem(str(row[0]))
                if blocked_current_state == "blocked":
                    self.bd_blocked_list.addItem(blocked_url)
                elif blocked_current_state == "unblocked":
                    self.bd_unblocked_list.addItem(blocked_url)
            if self.bd_blocked_list.count() == 0:
                self.bd_block_all_button.setEnabled(True)
                self.bd_unblock_all_button.setEnabled(False)
            elif self.bd_unblocked_list.count() == 0:
                self.bd_unblock_all_button.setEnabled(True)
                self.bd_block_all_button.setEnabled(False)
            elif self.bd_unblocked_list.count() == 0 and self.bd_blocked_list.count() == 0:
                self.bd_unblock_all_button.setEnabled(False)
                self.bd_block_all_button.setEnabled(False)
            else:
                self.bd_unblock_all_button.setEnabled(True)
                self.bd_block_all_button.setEnabled(True)
        except Exception as e:
            print(f"Error fillBlockedList: {e}")

    def fillBlockedDetail(self, selected_blocked_item, sender):
        try:
            if selected_blocked_item:
                selected_blocked_item = selected_blocked_item[0]

                selected_blocked_item_detail = db_operations.custom_query(
                    f'select url, data_type, operation_time, current_status from blocked_data where url = "{selected_blocked_item.text()}"')[0]

                if sender == "blocked_list":
                    self.bd_unblock_sel_data_button.disconnect()
                    self.bd_unblocked_list.clearSelection()
                    self.bd_unblock_sel_data_button.setEnabled(True)
                    self.bd_block_sel_data_button.setEnabled(False)
                    self.bd_unblock_sel_data_button.clicked.connect(
                        lambda: blocking_operations.block_unblock(control_toggle_button=None, selected_blocked_item_detail=selected_blocked_item_detail, sender="unblock_button", fillBlockedList=self.fillBlockedList))
                elif sender == "unblocked_list":
                    self.bd_block_sel_data_button.disconnect()
                    self.bd_blocked_list.clearSelection()
                    self.bd_unblock_sel_data_button.setEnabled(False)
                    self.bd_block_sel_data_button.setEnabled(True)
                    self.bd_block_sel_data_button.clicked.connect(
                        lambda: blocking_operations.block_unblock(control_toggle_button=None, selected_blocked_item_detail=selected_blocked_item_detail, sender="block_button", fillBlockedList=self.fillBlockedList))

                self.bd_url_label.setText(
                    selected_blocked_item_detail[0])
                self.bd_op_time_label.setText(
                    selected_blocked_item_detail[2])
                self.bd_current_stat_label.setText(
                    selected_blocked_item_detail[3])
                if selected_blocked_item_detail[3] == "blocked":
                    self.bd_blocked_list.setStyleSheet(
                        blocked_data_styles.blocked_data_list_style)
                    self.bd_current_stat_label.setStyleSheet(
                        "color:#23B7E5;")
                elif selected_blocked_item_detail[3] == "unblocked":
                    self.bd_unblocked_list.setStyleSheet(
                        blocked_data_styles.unblocked_data_list_style)
                    self.bd_current_stat_label.setStyleSheet(
                        "color:#F05050;")
            else:
                self.bd_unblock_sel_data_button.setEnabled(False)
                self.bd_block_sel_data_button.setEnabled(False)
        except Exception as e:
            print(f"Error fillBlockedDetail: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = BlockedDataPageWidget()
    main_window.show()

    sys.exit(app.exec())
