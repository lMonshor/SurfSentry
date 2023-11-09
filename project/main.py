import sys
from PyQt6 import QtWidgets
from ui import tray_app_ui, widget_ui, menu_ui, preferences_ui, loading_ui, information_ui
from features import workers

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    my_loading_ui = loading_ui.uiLoading()

    my_information_ui = information_ui.uiInformation()

    my_loading_ui.show()

    my_tray_app_ui = tray_app_ui.uiTrayApp()

    my_widget_ui = widget_ui.uiWidget()

    my_menu_ui = menu_ui.uiMenu()

    my_pref_ui = preferences_ui.uiPreferences()

    my_update_data_worker = workers.UpdateDataWorker(my_pref_ui, my_loading_ui)

    my_tray_app_ui.my_widget_ui = my_widget_ui

    my_widget_ui.my_tray_app_ui = my_tray_app_ui
    my_widget_ui.my_menu_ui = my_menu_ui
    my_widget_ui.my_loading_ui = my_loading_ui
    my_widget_ui.my_information_ui = my_information_ui
    my_widget_ui.fillBlockedList = my_pref_ui.fillBlockedList

    my_menu_ui.my_pref_ui = my_pref_ui

    my_pref_ui.my_update_data_worker = my_update_data_worker
    my_pref_ui.my_loading_ui = my_loading_ui
    my_pref_ui.my_information_ui = my_information_ui

    my_update_data_worker.finished.connect(my_loading_ui.hide)
    my_update_data_worker.finished.connect(my_information_ui.show)
    my_update_data_worker.finished.connect(
        lambda: my_tray_app_ui.setVisible(True))
    my_update_data_worker.finished.connect(my_update_data_worker.wait)
    my_update_data_worker.finished.connect(my_update_data_worker.quit)
    my_update_data_worker.start()
    app.exec()
