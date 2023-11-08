import sys
from api import usom_api
from db import db_operations
from features import blocking_operations, methods
from PyQt6.QtCore import Qt, QRect, QSize, QPoint, QUrl, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QIcon, QScreen, QGuiApplication, QCursor, QDesktopServices, QColor, QBrush
from ui import tray_app_ui, widget_ui, menu_ui, preferences_ui3, loading_ui2, information_ui2
import subprocess
import smtplib
from email.mime.text import MIMEText
import config


subprocess.run([
    "pyuic6",
    "-x",
    "D:/Personal/Projects/muhendislik_tasarimi_proje/source_codes/project/ui/pref.ui",
    "-o",
    "D:/Personal/Projects/muhendislik_tasarimi_proje/source_codes/project/ui/preferences_ui3.py"
])


class UpdateDataWorker(QThread):
    finished = pyqtSignal()

    def run(self):
        try:
            # updateData()
            blocking_operations.block_all_entries()
            fillMalList()
            fillBlockedList()

            self.finished.emit()
        except Exception as e:
            print(f"Error run(updatedataworker): {e}")


class BlockingOperationWorker(QThread):
    finished = pyqtSignal()

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
                if self.sender == "unblock_all_button":
                    blocking_operations.unblock_all_entries()
                elif self.sender == "block_all_button":
                    blocking_operations.block_all_entries()

            self.finished.emit()
        except Exception as e:
            print(f"Error run(blockingoperationworker): {e}")


def updateData():
    try:
        if not loading_ui.isVisible():
            loading_ui.show()
        usom_api.get_malicious_data(loading_ui)
    except Exception as e:
        print(f"Error updateData: {e}")


def fillMalList():
    try:
        pref_ui.md_mal_data_list.clear()
        mal_urls = db_operations.get_data_by_column_name(
            column_name="url", table_name="malicious_data")
        for row in mal_urls:
            mal_url = QListWidgetItem(str(row[0]))
            pref_ui.md_mal_data_list.addItem(mal_url)
            pref_ui.md_mal_data_list.addItem(mal_url)
    except Exception as e:
        print(f"Error fillMalList: {e}")


def fillMalDetails(sel_mal_items):
    try:
        if sel_mal_items:
            sel_mal_item = sel_mal_items[0]
            global sel_mal_item_detail
            sel_mal_item_detail = db_operations.get_one_data_detail(
                column_name="*", condition_column='url', condition_value=sel_mal_item.text(), table_name='malicious_data')
            pref_ui.md_source_button.setEnabled(True)
            pref_ui.md_source_button.disconnect()
            pref_ui.md_source_button.clicked.connect(openWebPageUsom)

            pref_ui.md_detail_url_label.setText(sel_mal_item_detail[3])
            pref_ui.md_detail_type_label.setText(sel_mal_item_detail[4])
            pref_ui.md_detail_desc_label.setText(sel_mal_item_detail[5])
            if sel_mal_item_detail[6] <= 3:
                pref_ui.md_mal_data_list.setStyleSheet("""QListWidget {
                                outline: 0;
                                background-color: #101112; 
                                color: white; 
                                border: none; 
                                padding: 5px; 
                                border: 1px solid #555555;
                            }

                            QListWidget::item {
                                padding: 3px; 
                            }

                            QListWidget::item:selected {
                                background-color: #23B7E5; 
                                color: white; 
                            }

                            QListWidget::item:hover {
                                background-color: #DDDDDD;
                                color: #0f0f0f;
                            }

                            QScrollBar:vertical {
                                border: 1px solid #555555;
                                background: none;
                                width: 10px;
                                margin: 0px 0px 0px 0px;
                            }

                            QScrollBar::handle:vertical {
                                background: #393E46;
                                min-height: 30px;
                                max-height: 30px;
                                border-radius: 5px;
                            }

                            QScrollBar::add-line:vertical {
                                height: 0px;
                                subcontrol-position: bottom;
                                subcontrol-origin: margin;
                            }

                            QScrollBar::sub-line:vertical {
                                height: 0px;
                                subcontrol-position: top;
                                subcontrol-origin: margin;
                            }

                            QListWidget::viewport {
                                background: #101112;
                            }
                            """)
                pref_ui.md_threat_level_title.setText("LOW")
                pref_ui.md_threat_level_title.setStyleSheet(
                    "background-color: #23B7E5;color:white;")
            elif 4 <= sel_mal_item_detail[6] <= 7:
                pref_ui.md_mal_data_list.setStyleSheet("""QListWidget {
                                outline: 0;
                                background-color: #101112; 
                                color: white; 
                                border: none; 
                                padding: 5px; 
                                border: 1px solid #555555;
                            }

                            QListWidget::item {
                                padding: 3px; 
                            }

                            QListWidget::item:selected {
                                background-color: #FF902B; 
                                color: white; 
                            }

                            QListWidget::item:hover {
                                background-color: #DDDDDD;
                                color: #0f0f0f;
                            }

                            QScrollBar:vertical {
                                border: 1px solid #555555;
                                background: none;
                                width: 10px;
                                margin: 0px 0px 0px 0px;
                            }

                            QScrollBar::handle:vertical {
                                background: #393E46;
                                min-height: 30px;
                                max-height: 30px;
                                border-radius: 5px;
                            }

                            QScrollBar::add-line:vertical {
                                height: 0px;
                                subcontrol-position: bottom;
                                subcontrol-origin: margin;
                            }

                            QScrollBar::sub-line:vertical {
                                height: 0px;
                                subcontrol-position: top;
                                subcontrol-origin: margin;
                            }

                            QListWidget::viewport {
                                background: #101112;
                            }
                            """)
                pref_ui.md_threat_level_title.setText("MEDIUM")
                pref_ui.md_threat_level_title.setStyleSheet(
                    "background-color: #FF902B;color:white;")
            else:
                pref_ui.md_mal_data_list.setStyleSheet("""QListWidget {
                                outline: 0;
                                background-color: #101112; 
                                color: white; 
                                border: none; 
                                padding: 5px; 
                                border: 1px solid #555555;
                            }

                            QListWidget::item {
                                padding: 3px; 
                            }

                            QListWidget::item:selected {
                                background-color: #F05050; 
                                color: white; 
                            }

                            QListWidget::item:hover {
                                background-color: #DDDDDD;
                                color: #0f0f0f;
                            }

                            QScrollBar:vertical {
                                border: 1px solid #555555;
                                background: none;
                                width: 10px;
                                margin: 0px 0px 0px 0px;
                            }

                            QScrollBar::handle:vertical {
                                background: #393E46;
                                min-height: 30px;
                                max-height: 30px;
                                border-radius: 5px;
                            }

                            QScrollBar::add-line:vertical {
                                height: 0px;
                                subcontrol-position: bottom;
                                subcontrol-origin: margin;
                            }

                            QScrollBar::sub-line:vertical {
                                height: 0px;
                                subcontrol-position: top;
                                subcontrol-origin: margin;
                            }

                            QListWidget::viewport {
                                background: #101112;
                            }
                            """)
                pref_ui.md_threat_level_title.setText("HIGH")
                pref_ui.md_threat_level_title.setStyleSheet(
                    "background-color: #F05050;color:white;")
            pref_ui.md_detail_source_label.setText(sel_mal_item_detail[7])
            pref_ui.md_detail_date_label.setText(sel_mal_item_detail[8])
    except Exception as e:
        print(f"Error fillMalDetails: {e}")


def fillBlockedList():
    try:
        pref_ui.bd_blocked_list.clear()
        pref_ui.bd_unblocked_list.clear()
        pref_ui.bd_blocked_list.clearSelection()
        pref_ui.bd_unblocked_list.clearSelection()

        blocked_data = db_operations.get_data_by_column_name(
            column_name="url,current_status", table_name="blocked_data")
        for row in blocked_data:
            blocked_current_state = row[1]
            blocked_url = QListWidgetItem(str(row[0]))
            if blocked_current_state == "blocked":
                pref_ui.bd_blocked_list.addItem(blocked_url)
            elif blocked_current_state == "unblocked":
                pref_ui.bd_unblocked_list.addItem(blocked_url)
        if pref_ui.bd_blocked_list.count() == 0:
            pref_ui.bd_block_all_button.setEnabled(True)
            pref_ui.bd_unblock_all_button.setEnabled(False)
        elif pref_ui.bd_unblocked_list.count() == 0:
            pref_ui.bd_unblock_all_button.setEnabled(True)
            pref_ui.bd_block_all_button.setEnabled(False)
        elif pref_ui.bd_unblocked_list.count() == 0 and pref_ui.bd_blocked_list.count() == 0:
            pref_ui.bd_unblock_all_button.setEnabled(False)
            pref_ui.bd_block_all_button.setEnabled(False)
        else:
            pref_ui.bd_unblock_all_button.setEnabled(True)
            pref_ui.bd_block_all_button.setEnabled(True)
    except Exception as e:
        print(f"Error fillBlockedList: {e}")


def fillBlockedDetail(selected_blocked_item, sender):
    try:
        if selected_blocked_item:
            selected_blocked_item = selected_blocked_item[0]

            selected_blocked_item_detail = db_operations.custom_query(
                f'select url, data_type, operation_time, current_status from blocked_data where url = "{selected_blocked_item.text()}"')[0]

            if sender == "blocked_list":
                pref_ui.bd_unblock_sel_data_button.disconnect()
                pref_ui.bd_unblocked_list.clearSelection()
                pref_ui.bd_unblock_sel_data_button.setEnabled(True)
                pref_ui.bd_block_sel_data_button.setEnabled(False)
                pref_ui.bd_unblock_sel_data_button.clicked.connect(
                    lambda: block_unblock(selected_blocked_item_detail, "unblock_button"))
            elif sender == "unblocked_list":
                pref_ui.bd_block_sel_data_button.disconnect()
                pref_ui.bd_blocked_list.clearSelection()
                pref_ui.bd_unblock_sel_data_button.setEnabled(False)
                pref_ui.bd_block_sel_data_button.setEnabled(True)
                pref_ui.bd_block_sel_data_button.clicked.connect(
                    lambda: block_unblock(selected_blocked_item_detail, "block_button"))

            pref_ui.bd_url_label.setText(
                selected_blocked_item_detail[0])
            pref_ui.bd_op_time_label.setText(
                selected_blocked_item_detail[2])
            pref_ui.bd_current_stat_label.setText(
                selected_blocked_item_detail[3])
            if selected_blocked_item_detail[3] == "blocked":
                pref_ui.bd_blocked_list.setStyleSheet("""QListWidget {
                                outline: 0;
                                background-color: #101112; 
                                color: white; 
                                border: none; 
                                padding: 5px; 
                                border: 1px solid #555555;
                            }

                            QListWidget::item {
                                padding: 3px; 
                            }

                            QListWidget::item:selected {
                                background-color: #23B7E5; 
                                color: white; 
                            }

                            QListWidget::item:hover {
                                background-color: #DDDDDD;
                                color: #0f0f0f;
                            }

                            QScrollBar:vertical {
                                border: 1px solid #555555;
                                background: none;
                                width: 10px;
                                margin: 0px 0px 0px 0px;
                            }

                            QScrollBar::handle:vertical {
                                background: #393E46;
                                min-height: 30px;
                                max-height: 30px;
                                border-radius: 5px;
                            }

                            QScrollBar::add-line:vertical {
                                height: 0px;
                                subcontrol-position: bottom;
                                subcontrol-origin: margin;
                            }

                            QScrollBar::sub-line:vertical {
                                height: 0px;
                                subcontrol-position: top;
                                subcontrol-origin: margin;
                            }

                            QListWidget::viewport {
                                background: #101112;
                            }
                            """)
                pref_ui.bd_current_stat_label.setStyleSheet(
                    "color:#23B7E5;")
            elif selected_blocked_item_detail[3] == "unblocked":
                pref_ui.bd_unblocked_list.setStyleSheet("""QListWidget {
                                outline: 0;
                                background-color: #101112; 
                                color: white; 
                                border: none; 
                                padding: 5px; 
                                border: 1px solid #555555;
                            }

                            QListWidget::item {
                                padding: 3px; 
                            }

                            QListWidget::item:selected {
                                background-color: #F05050; 
                                color: white; 
                            }

                            QListWidget::item:hover {
                                background-color: #DDDDDD;
                                color: #0f0f0f;
                            }

                            QScrollBar:vertical {
                                border: 1px solid #555555;
                                background: none;
                                width: 10px;
                                margin: 0px 0px 0px 0px;
                            }

                            QScrollBar::handle:vertical {
                                background: #393E46;
                                min-height: 30px;
                                max-height: 30px;
                                border-radius: 5px;
                            }

                            QScrollBar::add-line:vertical {
                                height: 0px;
                                subcontrol-position: bottom;
                                subcontrol-origin: margin;
                            }

                            QScrollBar::sub-line:vertical {
                                height: 0px;
                                subcontrol-position: top;
                                subcontrol-origin: margin;
                            }

                            QListWidget::viewport {
                                background: #101112;
                            }
                            """)
                pref_ui.bd_current_stat_label.setStyleSheet(
                    "color:#F05050;")
        else:
            pref_ui.bd_unblock_sel_data_button.setEnabled(False)
            pref_ui.bd_block_sel_data_button.setEnabled(False)
    except Exception as e:
        print(f"Error fillBlockedDetail: {e}")


def block_unblock(selected_blocked_item_detail, sender):
    try:
        if not loading_ui.isVisible():
            loading_ui.show()

        my_blocking_op_worker = BlockingOperationWorker(
            selected_blocked_item_detail, sender)
        my_blocking_op_worker.finished.connect(loading_ui.hide)
        my_blocking_op_worker.finished.connect(information_ui.show)
        my_blocking_op_worker.finished.connect(fillBlockedList)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.wait)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.quit)
        my_blocking_op_worker.start()
    except Exception as e:
        print(f"Error block_unblock: {e}")


def openWebPageUsom():
    try:
        url = QUrl(sel_mal_item_detail[9])
        QDesktopServices.openUrl(url)
    except Exception as e:
        print(f"Error openWebPageUsom: {e}")


def openCustomWebPage(link):
    try:
        url = QUrl(link)
        QDesktopServices.openUrl(url)
        pref_ui.md_source_button.disconnect()
    except Exception as e:
        print(f"Error openCustomWebPage: {e}")


def send_email_feedback(email_address, subject, description):
    sender = config.email
    receiver = config.receiver_email
    password = config.password

    message = f"Email Address: {email_address}\nSubject: {
        subject}\nDescription: {description}"

    msg = MIMEText(message)
    msg['Subject'] = "Feedback"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, receiver, msg.as_string())

    print("Message sent!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loading_ui = loading_ui2.uiLoading()
    information_ui = information_ui2.uiInformation()
    loading_ui.show()
    my_update_data_worker = UpdateDataWorker()

    my_tray_app_ui = tray_app_ui.uiTrayApp()
    my_widget_ui = widget_ui.uiWidget()
    my_menu_ui = menu_ui.uiMenu()

    my_pref_ui = QMainWindow()
    pref_ui = preferences_ui3.Ui_MainWindow()
    pref_ui.setupUi(my_pref_ui)
    my_tray_app_ui.my_widget_ui = my_widget_ui
    my_widget_ui.my_tray_app_ui = my_tray_app_ui
    my_widget_ui.my_menu_ui = my_menu_ui
    my_menu_ui.my_pref_ui = my_pref_ui

    pref_ui.md_mal_data_list.itemSelectionChanged.connect(
        lambda: fillMalDetails(pref_ui.md_mal_data_list.selectedItems()))

    pref_ui.bd_blocked_list.itemSelectionChanged.connect(
        lambda: fillBlockedDetail(pref_ui.bd_blocked_list.selectedItems(), "blocked_list"))

    pref_ui.bd_unblocked_list.itemSelectionChanged.connect(
        lambda: fillBlockedDetail(pref_ui.bd_unblocked_list.selectedItems(), "unblocked_list"))

    pref_ui.bd_unblock_all_button.clicked.connect(
        lambda: block_unblock(selected_blocked_item_detail=None, sender="unblock_all_button"))
    pref_ui.bd_block_all_button.clicked.connect(
        lambda: block_unblock(selected_blocked_item_detail=None, sender="block_all_button"))

    pref_ui.md_data_update_button.clicked.connect(my_update_data_worker.start)

    pref_ui.fb_submit_fb_button.clicked.connect(lambda: send_email_feedback(
        pref_ui.fb_email_text.toPlainText(), pref_ui.fb_sbject_text.toPlainText(), pref_ui.fb_desc_text.toPlainText()))

    pref_ui.stackedWidget.setCurrentWidget(pref_ui.general_page)
    pref_ui.menu_gen_button.clicked.connect(
        lambda: pref_ui.stackedWidget.setCurrentWidget(pref_ui.general_page))
    pref_ui.menu_ab_button.clicked.connect(
        lambda: pref_ui.stackedWidget.setCurrentWidget(pref_ui.about_page))
    pref_ui.menu_md_button.clicked.connect(
        lambda: pref_ui.stackedWidget.setCurrentWidget(pref_ui.mal_data_page))
    pref_ui.menu_bd_button.clicked.connect(
        lambda: pref_ui.stackedWidget.setCurrentWidget(pref_ui.blocked_data_page))
    pref_ui.menu_fb_button.clicked.connect(
        lambda: pref_ui.stackedWidget.setCurrentWidget(pref_ui.feedback_page))
    pref_ui.ab_github_button.clicked.connect(
        lambda: openCustomWebPage("https://github.com/lMonshor/SurfSentry"))

    my_update_data_worker.finished.connect(loading_ui.hide)
    my_update_data_worker.finished.connect(information_ui.show)
    my_update_data_worker.finished.connect(
        lambda: my_tray_app_ui.setVisible(True))
    my_update_data_worker.finished.connect(my_update_data_worker.wait)
    my_update_data_worker.finished.connect(my_update_data_worker.quit)
    my_update_data_worker.start()

    app.exec()
