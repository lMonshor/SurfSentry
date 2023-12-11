from PyQt6 import QtCore, QtGui, QtWidgets
from ui.preferences_ui.stacked_widget import stacked_widget
from ui.preferences_ui.menu_widget import menu_widget
from ui.components import qlayout_qwidget_generator
from styles.ui_styles import default_styles


class UiPreferences(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(940, 528)
        self.setWindowTitle(default_styles.window_title)
        self.setWindowIcon(QtGui.QIcon(default_styles.window_icon))

        self.central_widget, self.main_hlayout = qlayout_qwidget_generator.create_hlayout_widget(
            parent=self,
            geometry=(QtCore.QRect(0, 0, 940, 528)))
        self.central_widget.setStyleSheet(default_styles.light_style)

        self.my_menu_widget = menu_widget.MenuWidget()
        self.my_stacked_widget = stacked_widget.StackedWidget(
            my_menu_widget=self.my_menu_widget)

        self.main_hlayout.addWidget(self.my_menu_widget)
        self.main_hlayout.addWidget(self.my_stacked_widget)
        self.main_hlayout.setStretch(0,2)
        self.main_hlayout.setStretch(1,9)

        self.setCentralWidget(self.central_widget)
        
    def closeEvent(self, event):
        self.hide()
        event.ignore()
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = UiPreferences()
    main_window.show()

    sys.exit(app.exec())
