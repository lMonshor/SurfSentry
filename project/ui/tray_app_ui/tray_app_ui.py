from PyQt6 import QtCore, QtGui, QtWidgets
import os
class uiTrayApp(QtWidgets.QSystemTrayIcon):
    def __init__(self):
        self.my_widget_ui = None
        super().__init__()
        self.initUI()

    def initUI(self):
        tary_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\..\\assets', 'icon_passive.png')

        self.setIcon(QtGui.QIcon(tary_icon_path))
        self.setVisible(False)
        self.activated.connect(self.showWidget_ui)
        
    def showWidget_ui(self):
        tray_pos = self.geometry().topRight()
        desktop = QtGui.QGuiApplication.primaryScreen()
        screen_rect = desktop.availableGeometry()
        window_x = int(tray_pos.x() - (self.my_widget_ui.width() / 2))
        window_y = int(screen_rect.height() - self.my_widget_ui.height())
        self.my_widget_ui.setGeometry(window_x, window_y-3,
                                    self.my_widget_ui.width(), self.my_widget_ui.height())
        self.my_widget_ui.show()
