def create_qtreew_style(severity=None):
    if severity == "low" or severity == "blocked":
        color = "#23B7E5"
    elif severity == "medium":
        color = "#FF902B"
    elif severity == "high" or severity == "unblocked":
        color = "#F05050"
    else:
        color = "#DDDDDD"

    qtreewidget_styles = f"""
        QTreeWidget {{
            outline: 0;
            background-color: #202123;
            color: white;
            border: none;
            font-size: 14px;
        }}

        QHeaderView::section {{
            background-color: #0f0f0f;
            color: white;
            font-size: 17px;
            border: none;
            padding: 0px;
            margin: 0px 0px 0px 0px;
        }}

        QTreeWidget::item {{
            padding: 1px;
        }}

        QTreeWidget::item:hover {{
            background-color: #DDDDDD;
            color: #0f0f0f;
        }}

        QTreeWidget::item:selected {{
            background-color: {color};
            color: #0f0f0f;
        }}

        QScrollBar:vertical {{
            background-color: grey;
            width: 14px;
            margin: 1px 1px 1px 1px;
        }}

        QScrollBar::handle:vertical {{
            background-color: #4C566A;
            min-height: 30px;
            max-height: 30px;
        }}

        QScrollBar::handle:vertical:hover {{
            background-color: #5E81AC;
        }}

        QScrollBar::handle:vertical:pressed {{
            background-color: #81A1C1;
        }}

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            border: none;
            background: none;
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }}

        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {{
            background: none;
        }}
    """
    return qtreewidget_styles
