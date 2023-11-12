from PyQt6 import QtCore, QtGui, QtWidgets
from ui.components import qpushbutton_generator, qlabel_generator
from ui.toggle_button_ui import toggle_button_ui
from features import blocking_operations, redirect_operations
from styles.widget_ui_styles import widget_buttons_style
import os


class UiWidget(QtWidgets.QWidget):
    CONTROL_TITLE_FONT = QtGui.QFont("Calibri", 20)
    CONTROL_DESC_FONT = QtGui.QFont("Calibri", 16)
    CONTROL_WIDGET_STYLE = "background-color: #0f0f0f"
    BOTTOM_WIDGET_STYLE = "background-color: #393E46"

    def __init__(self, my_tray_app_ui, my_menu_ui, my_pref_ui):
        self.my_tray_app_ui = my_tray_app_ui
        self.my_menu_ui = my_menu_ui
        self.my_pref_ui = my_pref_ui
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(326, 426)
        self.setWindowFlags(QtCore.Qt.WindowType.Popup |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)

        self.createControlWidget()
        self.createBottomWidget()

    def createControlWidget(self):
        self.control_widget = QtWidgets.QWidget(self)
        self.control_widget.setGeometry(QtCore.QRect(0, 0, 326, 380))
        self.control_widget.setStyleSheet(self.CONTROL_WIDGET_STYLE)

        self.control_logo = qlabel_generator.create_label(
            parent=self.control_widget, geometry=(
                QtCore.QRect(73, 50, 180, 84,)),
            text='',
            icon_name='control_logo')

        self.control_toggle_button = self.createToggleButton(88, 155, 140, 70)

        self.control_status_title_label = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(88, 240, 150, 33)),
            font=self.CONTROL_TITLE_FONT,
            text='Disconnected')
        self.control_status_title_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

        self.control_status_desc_label = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(40, 270, 246, 28)),
            font=self.CONTROL_DESC_FONT,
            text='Your Internet is not secure')
        self.control_status_desc_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

    def createBottomWidget(self):
        self.bottom_widget = QtWidgets.QWidget(parent=self)
        self.bottom_widget.setGeometry(QtCore.QRect(0, 380, 326, 46))
        self.bottom_widget.setStyleSheet(self.BOTTOM_WIDGET_STYLE)

        self.bottom_logo = qlabel_generator.create_label(
            parent=self.bottom_widget, geometry=(QtCore.QRect(10, 8, 140, 30)),
            text='',
            icon_name='bottom_logo')

        self.bottom_settings_button = qpushbutton_generator.create_button(
            parent=self.bottom_widget,
            geometry=(QtCore.QRect(286, 8, 30, 30)),
            text='', icon_name='bottom_settings',
            on_click=self.open_menu_ui_at_click_pos)
        self.bottom_settings_button.setStyleSheet(widget_buttons_style.button_style)
        self.bottom_settings_button.setIconSize(QtCore.QSize(24, 24))
        
        self.bottom_bug_button = qpushbutton_generator.create_button(
            parent=self.bottom_widget,
            geometry=(QtCore.QRect(250, 8, 30, 30)),
            text='', icon_name='bottom_bug',
            on_click=None)
        self.bottom_bug_button.setStyleSheet(widget_buttons_style.button_style)
        self.bottom_bug_button.setIconSize(QtCore.QSize(24, 24))

    def createToggleButton(self, x, y, width, height):
        toggle_button = toggle_button_ui.CustomToggleSwitch()
        toggle_button.setParent(self.control_widget)
        toggle_button.setGeometry(QtCore.QRect(x, y, width, height))
        toggle_button.toggleChanged.connect(self.switch_changed)
        return toggle_button

    def open_menu_ui_at_click_pos(self):
        click_pos = QtGui.QCursor.pos()
        menu_width = self.my_menu_ui.width()
        menu_height = self.my_menu_ui.height()
        menu_pos = click_pos - QtCore.QPoint(menu_width, menu_height)
        self.my_menu_ui.setGeometry(
            menu_pos.x(), menu_pos.y(), menu_width, menu_height)
        self.my_menu_ui.show()

    def switch_changed(self):
        self.control_toggle_button.setEnabled(False)

        if self.control_toggle_button.toggled:
            sender = "switch_opened"
            self.my_tray_app_ui.setIcon(QtGui.QIcon(
                os.path.join(self.ASSETS_PATH, self.ICONS['active_icon'])))
            redirect_operations.start_server()
        else:
            sender = "switch_closed"
            self.my_tray_app_ui.setIcon(QtGui.QIcon(os.path.join(
                self.ASSETS_PATH, self.ICONS['passive_icon'])))
            redirect_operations.stop_server()

        self.perform_blocking_operations(sender)

    def perform_blocking_operations(self, sender):
        blocking_operations.block_unblock(
            control_toggle_button=self.control_toggle_button,
            selected_blocked_item_detail=None,
            sender=sender,
            fillBlockedList=self.my_pref_ui.my_stacked_widget.my_blocked_data_page.fillBlockedList)
