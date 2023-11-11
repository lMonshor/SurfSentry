from PyQt6 import QtCore, QtGui, QtWidgets
from styles import bd_styles
from styles.stacked_widget_style import stacked_widget_button_style
from features import blocking_operations
from db import db_operations
import os

single_right_icon_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\..\\..\\assets', 'single_right_logo.png')
double_right_icon_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\..\\..\\assets', 'double_right_logo.png')
single_left_icon_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\..\\..\\assets', 'single_left_logo.png')
double_left_icon_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\..\\..\\assets', 'double_left_logo.png')
add_icon_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\..\\..\\assets', 'add_logo.png')
trash_icon_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '..\\..\\..\\..\\assets', 'trash_logo.png')

class BlockedDataPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.bd_blocked_list = QtWidgets.QListWidget(
            parent=self)
        self.bd_blocked_list.setGeometry(QtCore.QRect(30, 59, 281, 331))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bd_blocked_list.sizePolicy().hasHeightForWidth())
        self.bd_blocked_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bd_blocked_list.setFont(font)
        self.bd_blocked_list.setStyleSheet(bd_styles.blocked_style)
        self.bd_blocked_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bd_blocked_list.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.bd_blocked_list.setLineWidth(2)
        self.bd_blocked_list.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.bd_blocked_list.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.bd_blocked_list.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.bd_blocked_list.setSelectionRectVisible(True)
        self.bd_inf_title = QtWidgets.QLabel(parent=self)
        self.bd_inf_title.setGeometry(QtCore.QRect(30, 410, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.bd_inf_title.setFont(font)
        self.bd_inf_title.setStyleSheet("color:white;")
        self.bd_inf_glayout_widget = QtWidgets.QWidget(
            parent=self)
        self.bd_inf_glayout_widget.setGeometry(QtCore.QRect(40, 440, 701, 75))
        self.bd_inf_glayout = QtWidgets.QGridLayout(self.bd_inf_glayout_widget)
        self.bd_inf_glayout.setContentsMargins(0, 0, 0, 0)
        self.bd_op_time_label = QtWidgets.QLabel(
            parent=self.bd_inf_glayout_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bd_op_time_label.sizePolicy().hasHeightForWidth())
        self.bd_op_time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_op_time_label.setFont(font)
        self.bd_op_time_label.setStyleSheet("color:#777777;")
        self.bd_op_time_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bd_op_time_label.setText("")
        self.bd_inf_glayout.addWidget(self.bd_op_time_label, 1, 2, 1, 1)
        self.bd_url_title = QtWidgets.QLabel(parent=self.bd_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.bd_url_title.setFont(font)
        self.bd_url_title.setStyleSheet("color:white;")
        self.bd_inf_glayout.addWidget(self.bd_url_title, 0, 0, 1, 1)
        self.bd_colon3 = QtWidgets.QLabel(parent=self.bd_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_colon3.setFont(font)
        self.bd_colon3.setStyleSheet("color:white;")
        self.bd_inf_glayout.addWidget(self.bd_colon3, 2, 1, 1, 1)
        self.bd_current_stat_title = QtWidgets.QLabel(
            parent=self.bd_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.bd_current_stat_title.setFont(font)
        self.bd_current_stat_title.setStyleSheet("color:white;")
        self.bd_inf_glayout.addWidget(self.bd_current_stat_title, 2, 0, 1, 1)
        self.bd_op_time_title = QtWidgets.QLabel(
            parent=self.bd_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        self.bd_op_time_title.setFont(font)
        self.bd_op_time_title.setStyleSheet("color:white;")
        self.bd_inf_glayout.addWidget(self.bd_op_time_title, 1, 0, 1, 1)
        self.bd_colon1 = QtWidgets.QLabel(parent=self.bd_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_colon1.setFont(font)
        self.bd_colon1.setStyleSheet("color:white;")
        self.bd_inf_glayout.addWidget(self.bd_colon1, 0, 1, 1, 1)
        self.bd_colon2 = QtWidgets.QLabel(parent=self.bd_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_colon2.setFont(font)
        self.bd_colon2.setStyleSheet("color:white;")
        self.bd_inf_glayout.addWidget(self.bd_colon2, 1, 1, 1, 1)
        self.bd_current_stat_label = QtWidgets.QLabel(
            parent=self.bd_inf_glayout_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bd_current_stat_label.sizePolicy().hasHeightForWidth())
        self.bd_current_stat_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_current_stat_label.setFont(font)
        self.bd_current_stat_label.setStyleSheet("color:#777777;")
        self.bd_current_stat_label.setFrameShape(
            QtWidgets.QFrame.Shape.NoFrame)
        self.bd_current_stat_label.setText("")
        self.bd_inf_glayout.addWidget(self.bd_current_stat_label, 2, 2, 1, 1)
        self.bd_url_label = QtWidgets.QLineEdit(parent=self.bd_inf_glayout_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.bd_url_label.setFont(font)
        self.bd_url_label.setStyleSheet("color:#777777;")
        self.bd_url_label.setFrame(False)
        self.bd_url_label.setReadOnly(True)
        self.bd_inf_glayout.addWidget(self.bd_url_label, 0, 2, 1, 1)
        self.bd_blocked_list_title = QtWidgets.QLabel(
            parent=self)
        self.bd_blocked_list_title.setGeometry(QtCore.QRect(30, 30, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.bd_blocked_list_title.setFont(font)
        self.bd_blocked_list_title.setStyleSheet("color:white;")
        self.bd_unblocked_list_title = QtWidgets.QLabel(
            parent=self)
        self.bd_unblocked_list_title.setGeometry(
            QtCore.QRect(457, 30, 153, 24))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        self.bd_unblocked_list_title.setFont(font)
        self.bd_unblocked_list_title.setStyleSheet("color:white;")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(
            parent=self)
        self.verticalLayoutWidget_3.setGeometry(
            QtCore.QRect(340, 130, 91, 176))
        self.bd_buttons_vlayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.bd_buttons_vlayout.setContentsMargins(0, 0, 0, 0)
        self.bd_unblock_sel_data_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_unblock_sel_data_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_unblock_sel_data_button.setFont(font)
        self.bd_unblock_sel_data_button.setStyleSheet(stacked_widget_button_style.button_style)
        self.bd_unblock_sel_data_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(single_right_icon_path),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_unblock_sel_data_button.setIcon(icon)
        self.bd_unblock_sel_data_button.setFlat(False)
        self.bd_buttons_vlayout.addWidget(self.bd_unblock_sel_data_button)
        self.bd_unblock_all_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_unblock_all_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_unblock_all_button.setFont(font)
        self.bd_unblock_all_button.setStyleSheet(stacked_widget_button_style.button_style)
        self.bd_unblock_all_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(double_right_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_unblock_all_button.setIcon(icon1)
        self.bd_unblock_all_button.setFlat(False)
        self.bd_buttons_vlayout.addWidget(self.bd_unblock_all_button)
        self.bd_block_sel_data_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_block_sel_data_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_block_sel_data_button.setFont(font)
        self.bd_block_sel_data_button.setStyleSheet(stacked_widget_button_style.button_style)
        self.bd_block_sel_data_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(single_left_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_block_sel_data_button.setIcon(icon2)
        self.bd_block_sel_data_button.setFlat(False)
        self.bd_buttons_vlayout.addWidget(self.bd_block_sel_data_button)
        self.bd_block_all_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_block_all_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_block_all_button.setFont(font)
        self.bd_block_all_button.setStyleSheet(stacked_widget_button_style.button_style)
        self.bd_block_all_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(double_left_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_block_all_button.setIcon(icon3)
        self.bd_block_all_button.setFlat(False)
        self.bd_buttons_vlayout.addWidget(self.bd_block_all_button)
        self.bd_add_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_add_button.setFont(font)
        self.bd_add_button.setStyleSheet(stacked_widget_button_style.button_style)
        self.bd_add_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(add_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_add_button.setIcon(icon4)
        self.bd_add_button.setFlat(False)
        self.bd_buttons_vlayout.addWidget(self.bd_add_button)
        self.bd_delete_button = QtWidgets.QPushButton(
            parent=self.verticalLayoutWidget_3)
        self.bd_delete_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.bd_delete_button.setFont(font)
        self.bd_delete_button.setStyleSheet(stacked_widget_button_style.button_style)
        self.bd_delete_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(trash_icon_path),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bd_delete_button.setIcon(icon5)
        self.bd_delete_button.setFlat(False)
        self.bd_buttons_vlayout.addWidget(self.bd_delete_button)
        self.bd_unblocked_list = QtWidgets.QListWidget(
            parent=self)
        self.bd_unblocked_list.setGeometry(QtCore.QRect(457, 59, 281, 331))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bd_unblocked_list.sizePolicy().hasHeightForWidth())
        self.bd_unblocked_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bd_unblocked_list.setFont(font)
        self.bd_unblocked_list.setStyleSheet(bd_styles.unblocked_list_style)
        self.bd_unblocked_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bd_unblocked_list.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.bd_unblocked_list.setLineWidth(10)
        self.bd_unblocked_list.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.bd_unblocked_list.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.bd_unblocked_list.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.bd_unblocked_list.setSelectionRectVisible(True)
        self.bd_first_hline = QtWidgets.QFrame(parent=self)
        self.bd_first_hline.setGeometry(QtCore.QRect(48, 400, 672, 1))
        self.bd_first_hline.setStyleSheet("background-color:#393E46;")
        self.bd_first_hline.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bd_first_hline.setLineWidth(0)
        self.bd_first_hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.bd_blocked_list.setSortingEnabled(True)
        self.bd_inf_title.setText("Other Information")
        self.bd_url_title.setText("URL")
        self.bd_colon3.setText(":")
        self.bd_current_stat_title.setText("Current Status")
        self.bd_op_time_title.setText("Operation Time")
        self.bd_colon1.setText(":")
        self.bd_colon2.setText(":")
        self.bd_blocked_list_title.setText("Blocked Data List")
        self.bd_unblocked_list_title.setText("Unblocked Data List")
        self.bd_unblocked_list.setSortingEnabled(True)
        
        self.bd_blocked_list.itemSelectionChanged.connect(
            lambda: self.fillBlockedDetail(self.bd_blocked_list.selectedItems(), "blocked_list"))

        self.bd_unblocked_list.itemSelectionChanged.connect(
            lambda: self.fillBlockedDetail(self.bd_unblocked_list.selectedItems(), "unblocked_list"))

        self.bd_unblock_all_button.clicked.connect(
            lambda: blocking_operations.block_unblock(control_toggle_button=None, selected_blocked_item_detail=None, sender="unblock_all_button", fillBlockedList=self.fillBlockedList))
        
        self.bd_block_all_button.clicked.connect(
            lambda: blocking_operations.block_unblock(control_toggle_button=None, selected_blocked_item_detail=None, sender="block_all_button", fillBlockedList=self.fillBlockedList))
        
        
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
                    self.bd_blocked_list.setStyleSheet(bd_styles.blocked_style)
                    self.bd_current_stat_label.setStyleSheet(
                        "color:#23B7E5;")
                elif selected_blocked_item_detail[3] == "unblocked":
                    self.bd_unblocked_list.setStyleSheet(
                        bd_styles.unblocked_style)
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