def get_styles():
    styles = """
    /* General Styles */
    QMainWindow {
        background-color: #F5F5F5;
        color: #333333;
        font-family: "Segoe UI", sans-serif;
    }

    /* Tab Widget */
    QTabWidget::pane {
        border: none;
        background-color: #FFFFFF;
        border-radius: 4px;
        padding: 4px;
    }

    QTabBar {
        background-color: #FFFFFF;
        border-bottom: 1px solid #CCCCCC;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QTabBar::tab {
        background-color: #FFFFFF;
        color: #333333;
        padding: 8px 16px;
        min-width: 120px;
        border: 1px solid transparent;
        border-bottom: 1px solid transparent;
        font-weight: normal;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QTabBar::tab:selected {
        background-color: #F5F5F5;
        color: #333333;
        border-color: #CCCCCC;
        border-bottom: 1px solid #FFFFFF;
    }

    QTabBar::tab:!selected {
        margin-top: 2px;
    }

    QTabBar::tab:hover {
        background-color: #F0F0F0;
    }

    QTabBar::close-button {
        qproperty-icon: url(close.svg);
        subcontrol-origin: padding;
        padding: 2px;
        border-radius: 2px;
        background-color: transparent;
    }

    QTabBar::close-button:hover {
        background-color: rgb(0, 89, 240);
    }

    /* Toolbar */
    QToolBar {
        background-color: #F5F5F5;
        padding: 4px;
        border-bottom: 1px solid #CCCCCC;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QToolBar QToolButton {
        padding: 4px;
        border-radius: 4px;
    }

    QToolBar QToolButton:hover {
        background-color: #EEEEEE;
    }

    /* URL Bar */
    QLineEdit {
        padding: 4px 8px;
        border: 1px solid #CCCCCC;
        border-radius: 4px;
        background-color: #FFFFFF;
        color: #333333;
        font-size: 14px;
        selection-background-color: rgb(0, 130, 240);
        selection-color: #FFFFFF;
    }

    QLineEdit:focus {
        border-color: rgb(0, 170, 240);
    }

    /* Status Bar */
    QStatusBar {
        background-color: #F5F5F5;
        color: #333333;
        padding: 4px;
        border-top: 1px solid #CCCCCC;
        font-size: 12px;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
    }

    /* Misc */
    QToolTip {
        background-color: rgb(0, 130, 240);
        color: #FFFFFF;
        border: none;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
    }

    /* Tab Content */
    QWebEngineView {
        border: none;
        border-radius: 4px;
    }

    /* Scrollbars */
    QScrollBar:vertical {
        background-color: #F5F5F5;
        width: 16px;
        margin: 0;
    }

    QScrollBar::handle:vertical {
        background-color: #CCCCCC;
        min-height: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: rgb(0, 170, 240);
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0;
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        background-color: #F5F5F5;
        height: 16px;
        margin: 0;
    }

    QScrollBar::handle:horizontal {
        background-color: #CCCCCC;
        min-width: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:horizontal:hover {
        background-color: rgb(0, 170, 240);
    }

    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        width: 0;
        background: none;
    }

    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    }

    /* Menu Bar */
    QMenuBar {
        background-color: #F5F5F5;
        color: #333333;
        padding: 4px;
        border-bottom: 1px solid #CCCCCC;
    }

    QMenuBar::item {
        padding: 4px 8px;
        background-color: transparent;
        color: #333333;
    }

    QMenuBar::item:selected {
        background-color: #EEEEEE;
    }

    QMenuBar::item:pressed {
        background-color: #DDDDDD;
    }

    /* Menu */
    QMenu {
        background-color: #FFFFFF;
        color: #333333;
        border: 1px solid #CCCCCC;
        padding: 4px;
        border-radius: 4px;
    }

    QMenu::item {
        padding: 4px 8px;
        background-color: transparent;
        color: #333333;
    }

    QMenu::item:selected {
        background-color: #EEEEEE;
    }

    QMenu::item:pressed {
        background-color: #DDDDDD;
    }

    QMenu::separator {
        height: 1px;
        background-color: #CCCCCC;
        margin: 4px 0;
    }

    /* Buttons */
    QPushButton {
        background-color: #EEEEEE;
        color: #333333;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: normal;
    }

    QPushButton:hover {
        background-color: #DDDDDD;
    }

    QPushButton:pressed {
        background-color: #CCCCCC;
    }

    /* Dialog */
    QDialog {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        border-radius: 4px;
    }

    QDialog QLabel {
        color: #333333;
        font-weight: bold;
    }

    QDialog QLineEdit {
        padding: 4px 8px;
        border: 1px solid #CCCCCC;
        border-radius: 4px;
        background-color: #FFFFFF;
        color: #333333;
        font-size: 14px;
    }

    QDialog QLineEdit:focus {
        border-color: rgb(0, 170, 240);
    }

    QDialog QPushButton {
        background-color: rgb(0, 170, 240);
        color: #FFFFFF;
        padding: 4px 8px;
        border-radius: 4px;
    QPushButton:hover {
    background-color: #DDDDDD;
}

QPushButton:pressed {
    background-color: #CCCCCC;
}

/* Dialog */
QDialog {
    background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    border-radius: 4px;
}

QDialog QLabel {
    color: #333333;
    font-weight: bold;
}

QDialog QLineEdit {
    padding: 4px 8px;
    border: 1px solid #CCCCCC;
    border-radius: 4px;
    background-color: #FFFFFF;
    color: #333333;
    font-size: 14px;
}

QDialog QLineEdit:focus {
    border-color: rgb(0, 170, 240);
}

QDialog QPushButton {
    background-color: rgb(0, 170, 240);
    color: #FFFFFF;
    padding: 4px 8px;
    border-radius: 4px;
}

QDialog QPushButton:hover {
    background-color: rgb(0, 130, 240);
}

QDialog QPushButton:pressed {
    background-color: rgb(0, 100, 240);
}

/* Scrollbar Handle */
QScrollBar::handle:vertical {
    background-color: #CCCCCC;
    min-height: 20px;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background-color: rgb(0, 170, 240);
}

QScrollBar::handle:horizontal {
    background-color: #CCCCCC;
    min-width: 20px;
    border-radius: 4px;
}

QScrollBar::handle:horizontal:hover {
    background-color: rgb(0, 170, 240);
}

/* Scrollbar Add Line */
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
    background: none;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
    background: none;
}

/* Scrollbar Add Page */
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

/* Menu Bar */
QMenuBar {
    background-color: #F5F5F5;
    color: #333333;
    padding: 4px;
    border-bottom: 1px solid #CCCCCC;
}

QMenuBar::item {
    padding: 4px 8px;
    background-color: transparent;
    color: #333333;
}

QMenuBar::item:selected {
    background-color: #EEEEEE;
}

QMenuBar::item:pressed {
    background-color: #DDDDDD;
}

/* Menu */
QMenu {
    background-color: #FFFFFF;
    color: #333333;
    border: 1px solid #CCCCCC;
    padding: 4px;
    border-radius: 4px;
}

QMenu::item {
    padding: 4px 8px;
    background-color: transparent;
    color: #333333;
}

QMenu::item:selected {
    background-color: #EEEEEE;
}

QMenu::item:pressed {
    background-color: #DDDDDD;
}

QMenu::separator {
    height: 1px;
    background-color: #CCCCCC;
    margin: 4px 0;
}

/* Buttons */
QPushButton {
    background-color: #EEEEEE;
    color: #333333;
    padding: 4px 8px;
    border-radius: 4px;
    font-weight: normal;
}

QPushButton:hover {
    background-color: #DDDDDD;
}

QPushButton:pressed {
    background-color: #CCCCCC;
}

/* Dialog */
QDialog {
    background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    border-radius: 4px;
}

QDialog QLabel {
    color: #333333;
    font-weight: bold;
}

QDialog QLineEdit {
    padding: 4px 8px;
    border: 1px solid #CCCCCC;
    border-radius: 4px;
    background-color: #FFFFFF;
    color: #333333;
    font-size: 14px;
}

QDialog QLineEdit:focus {
    border-color: rgb(0, 170, 240);
}

QDialog QPushButton {
    background-color: rgb(0, 170, 240);
    color: #FFFFFF;
    padding: 4px 8px;
    border-radius: 4px;
}

QDialog QPushButton:hover {
    background-color: rgb(0, 130, 240);
}

QDialog QPushButton:pressed {
    background-color: rgb(0, 100, 240);
}

/* Scrollbar Handle */
QScrollBar::handle:vertical {
    background-color: #CCCCCC;
    min-height: 20px;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background-color: rgb(0, 170, 240);
}

QScrollBar::handle:horizontal {
    background-color: #CCCCCC;
    min-width: 20px;
    border-radius: 4px;
}

QScrollBar::handle:horizontal:hover {
    background-color: rgb(0, 170, 240);
}

/* Scrollbar Add Line */
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
    background: none;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
    background: none;
}

/* Scrollbar Add Page */
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}
"""
    return styles

