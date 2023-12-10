import sys
from PyQt6 import QtWidgets
from ui.preferences_ui import preferences_ui
from ui.loading_ui import loading_ui
from ui.settings_ui import settings_ui
from ui.tray_app_ui import tray_app_ui
from ui.popup_ui import popup_ui
from features import workers

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    my_loading_ui = loading_ui.UiLoading()

    my_update_data_worker = workers.UpdateDataWorker(
        my_loading_ui=my_loading_ui)

    my_loading_ui.show()

    my_tray_app_ui = tray_app_ui.UiTrayApp()

    my_pref_ui = preferences_ui.UiPreferences()

    my_settings_ui = settings_ui.UiSettings(my_pref_ui=my_pref_ui, app=app)

    my_popup_ui = popup_ui.UiPopup(my_tray_app_ui=my_tray_app_ui,
                                   my_settings_ui=my_settings_ui)

    my_tray_app_ui.my_popup_ui = my_popup_ui

    my_update_data_worker.finished.connect(
        lambda: my_tray_app_ui.setVisible(True))
    my_update_data_worker.finished.connect(my_update_data_worker.wait)
    my_update_data_worker.finished.connect(my_update_data_worker.quit)
    my_update_data_worker.finished.connect(
        my_pref_ui.my_stacked_widget.my_mal_data_page.fill_lists)
    my_update_data_worker.finished.connect(
        my_pref_ui.my_stacked_widget.my_blocked_data_page.fill_lists)
    my_update_data_worker.finished.connect(my_loading_ui.deleteLater)
    my_update_data_worker.start()

    sys.exit(app.exec())
