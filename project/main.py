import subprocess
import sys
subprocess.run([
    "pyuic6",
    "-x",
    "D:/Personal/Projects/muhendislik_tasarimi_proje/source_codes/project/ui/pref.ui",
    "-o",
    "D:/Personal/Projects/muhendislik_tasarimi_proje/source_codes/project/ui/preferences_ui3.py"
])
from PyQt6.QtCore import Qt, QRect, QSize, QPoint,QUrl,QThread,pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow,QListWidget, QListWidgetItem,QTableWidget, QTableWidgetItem,QHeaderView
from PyQt6.QtGui import QIcon, QScreen, QGuiApplication,QCursor,QDesktopServices,QColor
from api import usom_api
from db import db_operations
from features import fw_operations,methods
from ui import tray_app_ui,widget_ui,menu_ui,preferences_ui3,loading_ui2,information_ui2


def updateData():
    if not loading_ui.isVisible():
        loading_ui.show()
    db_operations.create_specified_table("malicious_data")
    mal_data = usom_api.get_malicious_data()
    db_operations.clear_table_by_table_name("malicious_data")
    db_operations.save_to_specified_table(data=mal_data, table_name="malicious_data")

def fillMalUrlsList():
    pref_ui.mal_urls_list.clear()
    mal_urls = db_operations.get_data_by_column_name(column_name="url",table_name="malicious_data")
    for row in mal_urls:
        mal_url = QListWidgetItem(str(row[0]))
        pref_ui.mal_urls_list.addItem(mal_url)
        pref_ui.listWidget.addItem(mal_url)

def fillMalDetails():
    mal_items = pref_ui.mal_urls_list.selectedItems()
    for item in mal_items:
        mal_item = item
    global mal_detail
    mal_detail = db_operations.get_one_data_detail_from_specified_table(column_name="*",condition_column='url',condition_value=mal_item.text(),table_name='malicious_data')
    pref_ui.mal_source_button.setEnabled(True)
    pref_ui.mal_source_button.disconnect()
    pref_ui.mal_source_button.clicked.connect(openWebPageUsom)
    pref_ui.mal_detail_url_label.setText(mal_detail[3])
    pref_ui.mal_detail_resolved_ip_label.setText(mal_detail[4])
    pref_ui.mal_detail_type_label.setText(mal_detail[5])
    pref_ui.mal_detail_desc_label.setText(mal_detail[6])
    if mal_detail[7] <= 3:
        pref_ui.mal_threat_level_title.setText("LOW")
        pref_ui.mal_threat_level_title.setStyleSheet("background-color: #23B7E5;color:white;")
    elif 4 <= mal_detail[7] <= 7:
        pref_ui.mal_threat_level_title.setText("MEDIUM")
        pref_ui.mal_threat_level_title.setStyleSheet("background-color: #FF902B;color:white;")
    else:
        pref_ui.mal_threat_level_title.setText("HIGH")
        pref_ui.mal_threat_level_title.setStyleSheet("background-color: #F05050;color:white;")
    pref_ui.mal_detail_source_label.setText(mal_detail[8])
    pref_ui.mal_detail_date_label.setText(mal_detail[9])


def fillFwDetails(fw_items,sender):
    if sender == "blocked":
        pref_ui.fw_rules_unblocked_list.clearSelection()
    if sender == "unblocked":
        pref_ui.fw_rules_blocked_list.clearSelection()
    if fw_items:
        fw_item = fw_items[0]
        insideMethod(fw_item)
    else:
        pref_ui.fw_rules_unblock_sel_data_button.setEnabled(False)
    
def insideMethod(fw_item):
        pref_ui.fw_rules_unblock_sel_data_button.disconnect()
        fw_detail = db_operations.get_one_data_detail_from_specified_table(column_name="*",condition_column='url',condition_value=fw_item.text(),table_name='fw_rules')
        pref_ui.fw_rules_url_label.setText(fw_detail[1])
        pref_ui.fw_rules_ip_label.setText(fw_detail[2])
        pref_ui.fw_rules_op_time_label.setText(fw_detail[3])
        pref_ui.fw_rules_current_stat_label.setText(fw_detail[4])
        if fw_detail[4] == "blocked":
            pref_ui.fw_rules_unblock_sel_data_button.setEnabled(True)
            pref_ui.fw_rules_current_stat_label.setStyleSheet("color:#23B7E5;")
        else:
            pref_ui.fw_rules_unblock_sel_data_button.setEnabled(False)
            pref_ui.fw_rules_current_stat_label.setStyleSheet("color:#F05050;")
        pref_ui.fw_rules_unblock_sel_data_button.clicked.connect(lambda:unblock_one_item(fw_item))


def fillBlockedUnbockedList():
    pref_ui.fw_rules_blocked_list.clear()
    pref_ui.fw_rules_unblocked_list.clear()
    fw_data = db_operations.get_data_by_column_name(column_name="url,current_status",table_name="fw_rules")
    for row in fw_data:
        fw_current_state = row[1]
        fw_url = QListWidgetItem(str(row[0]))
        if fw_current_state == "blocked":
            pref_ui.fw_rules_blocked_list.addItem(fw_url)
        elif fw_current_state == "unblocked":
            pref_ui.fw_rules_unblocked_list.addItem(fw_url)
        
    

def unblock_one_item(fw_item):
    fw_operations.unblock_one_ip(fw_item.text())
    fillBlockedUnbockedList()
    pref_ui.fw_rules_unblocked_list.clearSelection()
    pref_ui.fw_rules_blocked_list.clearSelection()
    app.processEvents()


def openWebPageUsom():
    url = QUrl(mal_detail[10])
    QDesktopServices.openUrl(url)
    

def openCustomWebPage(link):
    url = QUrl(link)
    QDesktopServices.openUrl(url)
    pref_ui.mal_source_button.disconnect()

class WorkerThread(QThread):
    finished = pyqtSignal()

    def run(self):
        #updateData()
        fillMalUrlsList()
        #fw_operations.block_all_ips()
        #fw_operations.unblock_all_ips()
        fillBlockedUnbockedList()
        
        self.finished.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loading_ui = loading_ui2.uiLoading()
    information_ui = information_ui2.uiInformation()
    loading_ui.show()
    worker_thread = WorkerThread()
    

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

    pref_ui.fw_rules_blocked_list.itemSelectionChanged.connect(lambda:fillFwDetails(pref_ui.fw_rules_blocked_list.selectedItems(),"blocked"))
    pref_ui.fw_rules_unblocked_list.itemSelectionChanged.connect(lambda:fillFwDetails(pref_ui.fw_rules_unblocked_list.selectedItems(),"unblocked"))
    pref_ui.mal_urls_list.itemSelectionChanged.connect(fillMalDetails)
    pref_ui.fw_rules_unblock_all_button.clicked.connect(lambda:fw_operations.unblock_all_ips())

    pref_ui.mal_data_update_button.clicked.connect(worker_thread.start)
    pref_ui.stackedWidget.setCurrentWidget(pref_ui.general_page)
    pref_ui.menu_general_button.clicked.connect(lambda:pref_ui.stackedWidget.setCurrentWidget(pref_ui.general_page))
    pref_ui.menu_about_button.clicked.connect(lambda:pref_ui.stackedWidget.setCurrentWidget(pref_ui.about_me_page))

    pref_ui.menu_mal_data_button.clicked.connect(lambda:pref_ui.stackedWidget.setCurrentWidget(pref_ui.mal_data_page))
    pref_ui.menu_fw_button.clicked.connect(lambda:pref_ui.stackedWidget.setCurrentWidget(pref_ui.fw_rule_page))
    pref_ui.about_github_button.clicked.connect(lambda: openCustomWebPage("https://github.com/lMonshor/SurfSentry"))
    worker_thread.finished.connect(loading_ui.hide)
    worker_thread.finished.connect(lambda:my_tray_app_ui.setVisible(True))
    worker_thread.start()
    app.exec()
    
   
