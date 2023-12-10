from PyQt6 import QtCore, QtGui
from db import db_operations
from features import blocking_operations, data_filtering_operations
from api import usom_api
import socket


class UpdateDataWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self,  my_loading_ui):
        self.my_loading_ui = my_loading_ui
        super().__init__()

    def run(self):
        try:
            db_operations.create_db()
            db_operations.clear_old_data()
            usom_api.get_malicious_data(loading_ui=self.my_loading_ui)
            blocking_operations.manage_all_entries(action='fill',condition_value='unblocked')

        except Exception as e:
            print(f"Error run(UpdateDataWorker): {e}")
        finally:
            self.finished.emit()


class BlockingOperationsWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self, sender, entry=None):
        self.entry = entry
        self.sender = sender
        super().__init__()

    def run(self):
        try:
            if self.entry is not None:
                
                if self.sender == "unblock_button" or self.sender == 'remove_button':
                    blocking_operations.manage_entry(
                        entry=self.entry,
                        action='remove')
                
                elif self.sender == "block_button" or self.sender == "add_button":
                    blocking_operations.manage_entry(
                        entry=self.entry,
                        action='add')
            else:
                if self.sender == "unblock_all_button":
                    blocking_operations.manage_all_entries(
                        action='clear',
                        condition_value='blocked'
                    )
                
                elif self.sender == "block_all_button":
                    blocking_operations.manage_all_entries(
                        action='fill',
                        condition_value='unblocked'
                    )
                
                elif self.sender == self.sender == "switch_opened":
                    blocking_operations.manage_all_entries(
                        action='block',
                        condition_value='blocked'
                    )
                
                elif self.sender == "switch_closed":
                    blocking_operations.manage_all_entries(
                        action='unblock',
                        condition_value='blocked'
                    )

        except Exception as e:
            print(f"Error run(BlockingOperationsWorker): {e}")
        finally:
            self.finished.emit()


class CheckInputTypeWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)

    def __init__(self, user_input):
        self.user_input = user_input
        super().__init__()

    def run(self):
        try:
            socket.inet_pton(socket.AF_INET, self.user_input)
            input_type = "ip"
        except socket.error:
            try:
                socket.inet_pton(socket.AF_INET6, self.user_input)
                input_type = "ipv6"
            except socket.error:
                try:
                    socket.gethostbyname(self.user_input)
                    input_type = "domain"
                except socket.error:
                    input_type = "unknown"

        except Exception as e:
            print(f"Error run(CheckTypeWorker): {e}")
        finally:
            self.finished.emit(input_type)