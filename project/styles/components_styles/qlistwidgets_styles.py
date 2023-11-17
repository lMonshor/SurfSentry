default_qlistw_style = """
    QTreeWidget {
        background-color: #2E3440;
        color: white;
        border: 1px solid #3B4252;
        padding: 5px;
        selection-background-color: #3B4252;
        alternate-background-color: #3B4252;
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


mal_low_qlistw_style = """
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


mal_medium_qlistw_style = """
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
            background-color: #FF902B; 
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


mal_high_qlistw_style = """
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


blocked_qlistw_style = """
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


unblocked_qlistw_style = """
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
