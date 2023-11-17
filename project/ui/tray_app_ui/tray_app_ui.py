from PyQt6 import QtCore, QtGui, QtWidgets
import os

class UiTrayApp(QtWidgets.QSystemTrayIcon):
    ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\..\\assets')

    def __init__(self):
        self.passive_icon_path = os.path.join(self.ASSETS_PATH, 'icon_passive.png')
        self.active_icon_path = os.path.join(self.ASSETS_PATH, 'icon_active.png')
        self.my_popup_ui = None
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.set_icon_passive()
        self.setVisible(False)
        self.activated.connect(self.show_popup_ui_at_tray_position)

    def show_popup_ui_at_tray_position(self):
        tray_pos = self.geometry().topRight()
        desktop = QtGui.QGuiApplication.primaryScreen()
        screen_rect = desktop.availableGeometry()
        window_x = int(tray_pos.x() - (self.my_popup_ui.width() / 2))
        window_y = int(screen_rect.height() - self.my_popup_ui.height())
        self.my_popup_ui.setGeometry(window_x, window_y-3,
                                      self.my_popup_ui.width(), self.my_popup_ui.height())
        self.my_popup_ui.show()

    def set_icon_active(self):
        self.setIcon(QtGui.QIcon(self.active_icon_path))
        
    def set_icon_passive(self):
        self.setIcon(QtGui.QIcon(self.passive_icon_path))