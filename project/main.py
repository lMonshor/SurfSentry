import sys
from PyQt6 import QtWidgets
from ui.preferences_ui import preferences_ui
from ui.loading_ui import loading_ui
from ui.menu_ui import menu_ui
from ui.information_ui import information_ui
from ui.tray_app_ui import tray_app_ui
from ui.widget_ui import widget_ui
from features import workers

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    my_loading_ui = loading_ui.uiLoading()

    my_update_data_worker = workers.UpdateDataWorker(
        my_loading_ui=my_loading_ui)

    my_information_ui = information_ui.uiInformation()

    my_loading_ui.show()

    my_tray_app_ui = tray_app_ui.UiTrayApp()

    my_pref_ui = preferences_ui.uiPreferences(my_loading_ui=my_loading_ui)

    my_menu_ui = menu_ui.UiMenu(my_pref_ui=my_pref_ui)

    my_widget_ui = widget_ui.UiWidget(my_tray_app_ui=my_tray_app_ui,
                                      my_menu_ui=my_menu_ui, my_pref_ui=my_pref_ui)

    my_tray_app_ui.my_widget_ui = my_widget_ui

    my_update_data_worker.finished.connect(
        lambda: my_tray_app_ui.setVisible(True))
    my_update_data_worker.finished.connect(my_update_data_worker.wait)
    my_update_data_worker.finished.connect(my_update_data_worker.quit)
    my_update_data_worker.finished.connect(
        my_pref_ui.my_stacked_widget.my_mal_data_page.fillMalList)
    my_update_data_worker.finished.connect(
        my_pref_ui.my_stacked_widget.my_blocked_data_page.fillBlockedList)
    my_update_data_worker.finished.connect(my_loading_ui.deleteLater)
    my_update_data_worker.finished.connect(my_information_ui.show)
    my_update_data_worker.start()

    app.exec()
