from PyQt6 import QtWidgets
from ui.preferences_ui.stacked_widget.about_page import about_page
from ui.preferences_ui.stacked_widget.blocked_data_page import blocked_data_page
from ui.preferences_ui.stacked_widget.feedback_page import feedback_page
from ui.preferences_ui.stacked_widget.general_page import general_page
from ui.preferences_ui.stacked_widget.mal_data_page import mal_data_page
from styles.ui_styles import default_styles


class StackedWidget(QtWidgets.QStackedWidget):
    def __init__(self, my_menu_widget):
        self.my_menu_widget = my_menu_widget
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setEnabled(True)
        self.setStyleSheet(default_styles.dark_style)

        self.my_general_page = general_page.GeneralPageWidget()
        self.my_blocked_data_page = blocked_data_page.BlockedDataPageWidget()
        self.my_mal_data_page = mal_data_page.MalDataPageWidget()
        self.my_feedback_page = feedback_page.FeedbackPageWidget()
        self.my_about_page = about_page.AboutPageWidget()

        self.addWidget(self.my_general_page)

        self.addWidget(self.my_mal_data_page)

        self.addWidget(self.my_blocked_data_page)

        self.addWidget(self.my_feedback_page)

        self.addWidget(self.my_about_page)

        self.setCurrentIndex(0)

        self.setCurrentWidget(self.my_general_page)
        
        self.my_menu_widget.menu_gen_button.clicked.connect(
            lambda: self.setCurrentWidget(self.my_general_page))
        self.my_menu_widget.menu_ab_button.clicked.connect(
            lambda: self.setCurrentWidget(self.my_about_page))
        self.my_menu_widget.menu_md_button.clicked.connect(
            lambda: self.setCurrentWidget(self.my_mal_data_page))
        self.my_menu_widget.menu_bd_button.clicked.connect(
            lambda: self.setCurrentWidget(self.my_blocked_data_page))
        self.my_menu_widget.menu_fb_button.clicked.connect(
            lambda: self.setCurrentWidget(self.my_feedback_page))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = StackedWidget()
    main_window.show()

    sys.exit(app.exec())