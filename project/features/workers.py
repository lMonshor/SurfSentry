from PyQt6 import QtCore
from db import db_operations
from features import blocking_operations
from api import usom_api


class UpdateDataWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self, my_pref_ui,my_loading_ui):
        super().__init__()
        self.my_pref_ui = my_pref_ui
        self.my_loading_ui = my_loading_ui

    def run(self):
        try:
            db_operations.create_tables()
            if not self.my_loading_ui.isVisible():
                self.my_loading_ui.show()
            usom_api.get_malicious_data(self.my_loading_ui)
            blocking_operations.unblock_all_entries()
            self.my_pref_ui.fillMalList()
            self.my_pref_ui.fillBlockedList()

            self.finished.emit()
        except Exception as e:
            print(f"Error run(updatedataworker): {e}")


class BlockingOperationWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self, selected_blocked_item_detail, sender):
        super().__init__()
        self.selected_blocked_item_detail = selected_blocked_item_detail
        self.sender = sender

    def run(self):
        try:
            if self.selected_blocked_item_detail is not None:
                if self.sender == "unblock_button":
                    blocking_operations.unblock_entry(
                        self.selected_blocked_item_detail)
                elif self.sender == "block_button":
                    blocking_operations.block_entry(
                        self.selected_blocked_item_detail)
            else:
                if self.sender == "unblock_all_button" or self.sender == "switch_closed":
                    blocking_operations.unblock_all_entries()
                elif self.sender == "block_all_button" or self.sender == "switch_opened":
                    blocking_operations.block_all_entries()

            self.finished.emit()
        except Exception as e:
            print(f"Error run(blockingoperationworker): {e}")
