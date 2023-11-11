from PyQt6 import QtCore, QtGui, QtWidgets
from ui.preferences_ui.stacked_widget import stacked_widget
from ui.preferences_ui.menu_widget import menu_widget


class uiPreferences(QtWidgets.QMainWindow):
    def __init__(self, my_loading_ui):
        self.my_loading_ui = my_loading_ui
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(940, 528)

        self.setAutoFillBackground(True)

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setStyleSheet("background-color:#393E46;")
        self.main_hlayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.main_hlayout.setContentsMargins(0, 0, 0, 0)
        self.main_hlayout.setSpacing(0)

        self.my_menu_widget = menu_widget.MenuWidget()
        self.my_stacked_widget = stacked_widget.StackedWidget(my_menu_widget=self.my_menu_widget)

        self.main_hlayout.addWidget(self.my_menu_widget)
        self.main_hlayout.addWidget(self.my_stacked_widget)
        self.main_hlayout.setStretch(0, 2)
        self.main_hlayout.setStretch(1, 9)

        self.setWindowTitle("MainWindow")
        self.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])

    main_window = uiPreferences()
    main_window.show()

    sys.exit(app.exec())
