from PyQt6 import QtCore, QtWidgets, QtGui
from ui.components import qpushbutton_generator,qlayout_qwidget_generator
from styles.menu_ui_styles import menu_buttons_style


class UiMenu(QtWidgets.QWidget):
    BUTTON_FONT = QtGui.QFont("Calibri", 12)
    MENU_UI_STYLE = "background-color:#0f0f0f;border: 1px solid #393E46;"

    def __init__(self, my_pref_ui,app):
        self.my_pref_ui = my_pref_ui
        self.app = app
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(150, 90)
        self.setStyleSheet(self.MENU_UI_STYLE)
        self.setWindowFlags(QtCore.Qt.WindowType.Popup |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)

        self.menu_button_vlayout_widget, self.menu_button_vlayout = qlayout_qwidget_generator.create_vlayout_widget(
            parent=self,geometry=(QtCore.QRect(0, 0, 150, 90)))

        self.menu_pref_button = qpushbutton_generator.create_button(
            parent=self,
            text="Preferences",
            on_click=self.open_pref_ui)
        self.menu_pref_button.setStyleSheet(menu_buttons_style.button_style)
        self.menu_pref_button.setFixedSize(150, 31)

        self.menu_about_button = qpushbutton_generator.create_button(
            parent=self,
            text="About",
            on_click=None)
        self.menu_about_button.setStyleSheet(menu_buttons_style.button_style)
        self.menu_about_button.setFixedSize(150, 31)

        self.menu_exit_button = qpushbutton_generator.create_button(
            parent=self,
            text="Exit",
            on_click=self.app.quit)
        self.menu_exit_button.setStyleSheet(menu_buttons_style.button_style)
        self.menu_exit_button.setFixedSize(150, 31)

        self.menu_button_vlayout.addWidget(self.menu_pref_button)
        self.menu_button_vlayout.addWidget(self.menu_about_button)
        self.menu_button_vlayout.addWidget(self.menu_exit_button)

    def open_pref_ui(self):
        if not self.my_pref_ui.isVisible():
            self.my_pref_ui.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = UiMenu()
    main_window.show()

    sys.exit(app.exec())
