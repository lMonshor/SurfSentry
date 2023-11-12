
blocked_data_lists_style = """
    QListWidget {
            outline: 0;
            background-color: #101112; 
            color: white; 
            border: none; 
            padding: 5px; 
            border: 1px solid #555555;
        }

        QListWidget::item {
            padding: 3px; 
        }

        QListWidget::item:hover {
            background-color: #DDDDDD;
            color: #0f0f0f;
        }

        QScrollBar:vertical {
            border: 1px solid #555555;
            background: none;
            width: 10px;
            margin: 0px 0px 0px 0px;
        }

        QScrollBar::handle:vertical {
            background: #393E46;
            min-height: 30px;
            max-height: 30px;
            border-radius: 5px;
        }

        QScrollBar::add-line:vertical {
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical {
            height: 0px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }

        QListWidget::viewport {
            background: #101112;
        }"""
        

blocked_data_list_style = """
    QListWidget {
            outline: 0;
            background-color: #101112; 
            color: white; 
            border: none; 
            padding: 5px; 
            border: 1px solid #555555;
        }

        QListWidget::item {
            padding: 3px; 
        }

        QListWidget::item:selected {
            background-color: #23B7E5; 
            color: white; 
        }

        QListWidget::item:hover {
            background-color: #DDDDDD;
            color: #0f0f0f;
        }

        QScrollBar:vertical {
            border: 1px solid #555555;
            background: none;
            width: 10px;
            margin: 0px 0px 0px 0px;
        }

        QScrollBar::handle:vertical {
            background: #393E46;
            min-height: 30px;
            max-height: 30px;
            border-radius: 5px;
        }

        QScrollBar::add-line:vertical {
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical {
            height: 0px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }

        QListWidget::viewport {
            background: #101112;
        }
        """


unblocked_data_list_style = """
    QListWidget {
            outline: 0;
            background-color: #101112; 
            color: white; 
            border: none; 
            padding: 5px; 
            border: 1px solid #555555;
        }

        QListWidget::item {
            padding: 3px; 
        }

        QListWidget::item:selected {
            background-color: #F05050; 
            color: white; 
        }

        QListWidget::item:hover {
            background-color: #DDDDDD;
            color: #0f0f0f;
        }

        QScrollBar:vertical {
            border: 1px solid #555555;
            background: none;
            width: 10px;
            margin: 0px 0px 0px 0px;
        }

        QScrollBar::handle:vertical {
            background: #393E46;
            min-height: 30px;
            max-height: 30px;
            border-radius: 5px;
        }

        QScrollBar::add-line:vertical {
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }

        QScrollBar::sub-line:vertical {
            height: 0px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }

        QListWidget::viewport {
            background: #101112;
        }
        """
