from PyQt6 import QtCore, QtGui
from db import db_operations
from features import blocking_operations,data_filtering_operations
from api import usom_api


class UpdateDataWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self,  my_loading_ui):
        self.my_loading_ui = my_loading_ui
        super().__init__()

    def run(self):
        try:
            db_operations.create_tables()
            db_operations.custom_query(
                'DELETE FROM blocked_data WHERE current_status = "unblocked"')
            blocking_operations.unblock_all_entries()
            usom_api.get_malicious_data(loading_ui=self.my_loading_ui)
            
        except Exception as e:
            print(f"Error run(UpdateDataWorker): {e}")
        finally:
            self.finished.emit()


class BlockingOperationWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self, sender, item=None):
        self.item = item
        self.sender = sender
        super().__init__()

    def run(self):
        try:
            if self.item is not None:
                if self.sender == "unblock_button":
                    blocking_operations.unblock_entry(
                        self.item)
                elif self.sender == "block_button":
                    blocking_operations.block_entry(
                        self.item)
            else:
                if self.sender == "unblock_all_button" or self.sender == "switch_closed":
                    blocking_operations.unblock_all_entries()
                elif self.sender == "block_all_button" or self.sender == "switch_opened":
                    blocking_operations.block_all_entries()
        except Exception as e:
            print(f"Error run(BlockingOperationWorker): {e}")
        finally:
            self.finished.emit()
