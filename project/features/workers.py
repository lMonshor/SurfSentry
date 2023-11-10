from PyQt6 import QtCore, QtGui
from db import db_operations
from features import blocking_operations
from api import usom_api


class UpdateDataWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self,  my_loading_ui):
        self.my_loading_ui = my_loading_ui
        super().__init__()

    def run(self):
        try:
            db_operations.create_tables()
            db_operations.clear_table_by_table_name('malicious_data')
            db_operations.custom_query(
                'DELETE FROM blocked_data WHERE current_status = "unblocked"')
            usom_api.get_malicious_data(self.my_loading_ui)
            blocking_operations.unblock_all_entries()
        except Exception as e:
            print(f"Error run(UpdateDataWorker): {e}")
        finally:
            self.finished.emit()


class BlockingOperationWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self, selected_blocked_item_detail, sender):
        self.selected_blocked_item_detail = selected_blocked_item_detail
        self.sender = sender
        super().__init__()

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
        except Exception as e:
            print(f"Error run(BlockingOperationWorker): {e}")
        finally:
            self.finished.emit()
