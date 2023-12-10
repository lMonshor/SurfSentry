from PyQt6 import QtCore, QtGui, QtWidgets
from ui.components import qlabel_generator, qlabel_logo_generator, qpushbutton_logo_generator, component_hcenterer
from features import redirect_operations
from styles.components_styles import qpushbuttons_styles, qfonts_styles, qlabels_styles
from styles.ui_styles import default_styles
from ui.components import toggle_button_generator
from features import workers


class UiPopup(QtWidgets.QWidget):
    def __init__(self, my_tray_app_ui, my_settings_ui):
        self.my_tray_app_ui = my_tray_app_ui
        self.my_settings_ui = my_settings_ui
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(326, 426)
        self.setWindowFlags(QtCore.Qt.WindowType.Popup |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)

        self.popup_ctrl_widget = QtWidgets.QWidget(self)
        self.popup_ctrl_widget.setGeometry(QtCore.QRect(0, 0, 326, 380))
        self.popup_ctrl_widget.setStyleSheet(default_styles.dark_style)

        self.popup_control_logo = qlabel_logo_generator.create_logo_label(
            parent=self.popup_ctrl_widget, geometry=(
                QtCore.QRect(0, 50, 180, 84,)),
            icon_name='control_logo')
        component_hcenterer.center_component_horizontally(
            component=self.popup_control_logo
        )

        self.popup_ctrl_toggle_button = toggle_button_generator.create_toggle_button(
            parent=self.popup_ctrl_widget,
            geometry=(QtCore.QRect(0, 160, 130, 60)),
            toggle_changed=self.switch_changed)
        component_hcenterer.center_component_horizontally(
            component=self.popup_ctrl_toggle_button
        )

        self.popup_ctrl_status_title = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(88, 235, 1, 1)),
            font=qfonts_styles.headline_font,
            color=qlabels_styles.title_color,
            text='Disconnected')

        self.popup_ctrl_status_desc = qlabel_generator.create_label(
            parent=self,
            geometry=(QtCore.QRect(60, 270, 1, 1)),
            font=qfonts_styles.title_font,
            color=qlabels_styles.title_color,
            text='Your Internet is not Secure')

        self.popup_bottom_widget = QtWidgets.QWidget(parent=self)
        self.popup_bottom_widget.setGeometry(QtCore.QRect(0, 380, 326, 46))
        self.popup_bottom_widget.setStyleSheet(default_styles.light_style)

        self.popup_bottom_logo = qlabel_logo_generator.create_logo_label(
            parent=self.popup_bottom_widget, geometry=(
                QtCore.QRect(10, 8, 140, 30)),
            icon_name='bottom_logo')

        self.popup_bottom_bug_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.popup_bottom_widget,
            geometry=(QtCore.QRect(250, 8, 30, 30)),
            icon_name='bottom_bug',
            on_click=None)
        self.popup_bottom_bug_button.setStyleSheet(
            qpushbuttons_styles.popup_ui_button_style)
        self.popup_bottom_bug_button.setIconSize(QtCore.QSize(24, 24))

        self.popup_bottom_settings_button = qpushbutton_logo_generator.create_logo_button(
            parent=self.popup_bottom_widget,
            geometry=(QtCore.QRect(286, 8, 30, 30)),
            icon_name='bottom_settings',
            on_click=self.open_settings_ui_at_click_pos)
        self.popup_bottom_settings_button.setStyleSheet(
            qpushbuttons_styles.popup_ui_button_style)
        self.popup_bottom_settings_button.setIconSize(QtCore.QSize(24, 24))

    def open_settings_ui_at_click_pos(self):
        click_pos = QtGui.QCursor.pos()
        setting_width = self.my_settings_ui.width()
        settings_height = self.my_settings_ui.height()
        settings_pos = click_pos - \
            QtCore.QPoint(setting_width, settings_height)
        self.my_settings_ui.setGeometry(
            settings_pos.x(), settings_pos.y(), setting_width, settings_height)
        self.my_settings_ui.show()

    def switch_changed(self):
        self.popup_ctrl_toggle_button.setEnabled(False)

        if self.popup_ctrl_toggle_button.toggled:
            component_hcenterer.center_component_horizontally(
                component=self.popup_ctrl_status_title,
                text="Connecting...")
            component_hcenterer.center_component_horizontally(
                component=self.popup_ctrl_status_desc,
                text="Protection is Starting...")
            sender = "switch_opened"

        else:
            component_hcenterer.center_component_horizontally(
                component=self.popup_ctrl_status_title,
                text="Disconnecting...")
            component_hcenterer.center_component_horizontally(
                component=self.popup_ctrl_status_desc,
                text="Protection is Stopping...")
            sender = "switch_closed"

        self.create_worker(sender)

    def create_worker(self, sender):
        my_blocking_op_worker = workers.BlockingOperationsWorker(
            sender=sender)

        if sender == "switch_opened":
            my_blocking_op_worker.finished.connect(
                lambda:
                self.popup_ctrl_status_title.setStyleSheet(qlabels_styles.popup_title_opened_color))
            my_blocking_op_worker.finished.connect(
                lambda:
                component_hcenterer.center_component_horizontally(
                    component=self.popup_ctrl_status_title,
                    text="Connected"))
            my_blocking_op_worker.finished.connect(
                lambda:
                component_hcenterer.center_component_horizontally(
                    component=self.popup_ctrl_status_desc,
                    text="Your Internet is Secure"))
            my_blocking_op_worker.finished.connect(
                self.my_tray_app_ui.set_icon_active)
            my_blocking_op_worker.finished.connect(
                redirect_operations.start_server)

        else:
            my_blocking_op_worker.finished.connect(
                lambda:
                self.popup_ctrl_status_title.setStyleSheet(qlabels_styles.title_color))
            my_blocking_op_worker.finished.connect(
                lambda:
                component_hcenterer.center_component_horizontally(
                    component=self.popup_ctrl_status_title,
                    text="Disconnected"))
            my_blocking_op_worker.finished.connect(
                lambda:
                component_hcenterer.center_component_horizontally(
                    component=self.popup_ctrl_status_desc,
                    text="Your Internet is not Secure"))
            my_blocking_op_worker.finished.connect(
                self.my_tray_app_ui.set_icon_passive)
            my_blocking_op_worker.finished.connect(
                redirect_operations.stop_server)

        my_blocking_op_worker.finished.connect(
            lambda: self.popup_ctrl_toggle_button.setEnabled(True))
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.wait)
        my_blocking_op_worker.finished.connect(my_blocking_op_worker.quit)

        my_blocking_op_worker.start()
