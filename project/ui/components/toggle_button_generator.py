from ui.popup_ui.toggle_button_widget import toggle_button_widget 

def create_toggle_button(parent, geometry=None, toggle_changed=None):
    toggle_button = toggle_button_widget.CustomToggleSwitch()
    toggle_button.setParent(parent)
    if geometry:
        toggle_button.setGeometry(geometry)
    if toggle_changed:
        toggle_button.toggleChanged.connect(toggle_changed)
    return toggle_button