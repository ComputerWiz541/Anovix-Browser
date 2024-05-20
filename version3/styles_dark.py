def get_styles_dark():
    styles = """
    /* General Styles */
    QMainWindow {
        background-color: #313244;
        color: #cdd6f4;
        font-family: "Segoe UI", sans-serif;
    }

    /* Tab Widget */
    QTabWidget::pane {
        border: none;
        background-color: #45475a;
        border-radius: 4px;
        padding: 4px;
    }

    QTabBar {
        background-color: #45475a;
        border-bottom: 1px solid #6c7086;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QTabBar::tab {
        background-color: #45475a;
        color: #cdd6f4;
        padding: 8px 16px;
        min-width: 120px;
        border: 1px solid transparent;
        border-bottom: 1px solid transparent;
        font-weight: normal;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QTabBar::tab:selected {
        background-color: #313244;
        color: #cdd6f4;
        border-color: #6c7086;
        border-bottom: 1px solid #45475a;
    }

    QTabBar::tab:!selected {
        margin-top: 2px;
    }

    QTabBar::tab:hover {
        background-color: #585b70;
    }

    QTabBar::close-button {
        qproperty-icon: url(close.svg);
        subcontrol-origin: padding;
        padding: 2px;
        border-radius: 2px;
        background-color: transparent;
    }

    QTabBar::close-button:hover {
        background-color: #f38ba8;
    }

    /* Toolbar */
    QToolBar {
        background-color: #313244;
        padding: 4px;
        border-bottom: 1px solid #6c7086;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QToolBar QToolButton {
        padding: 4px;
        border-radius: 4px;
    }

    QToolBar QToolButton:hover {
        background-color: #585b70;
    }

    /* URL Bar */
    QLineEdit {
        padding: 4px 8px;
        border: 1px solid #6c7086;
        border-radius: 4px;
        background-color: #45475a;
        color: #cdd6f4;
        font-size: 14px;
        selection-background-color: #89b4fa;
        selection-color: #1e1e2e;
    }

    QLineEdit:focus {
        border-color: #89b4fa;
    }

    /* Status Bar */
    QStatusBar {
        background-color: #313244;
        color: #cdd6f4;
        padding: 4px;
        border-top: 1px solid #6c7086;
        font-size: 12px;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
    }

    /* Misc */
    QToolTip {
        background-color: #89b4fa;
        color: #1e1e2e;
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
        background-color: #313244;
        width: 16px;
        margin: 0;
    }

    QScrollBar::handle:vertical {
        background-color: #6c7086;
        min-height: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #89b4fa;
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0;
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        background-color: #313244;
        height: 16px;
        margin: 0;
    }

    QScrollBar::handle:horizontal {
        background-color: #6c7086;
        min-width: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:horizontal:hover {
        background-color: #89b4fa;
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
        background-color: #313244;
        color: #cdd6f4;
        padding: 4px;
        border-bottom: 1px solid #6c7086;
    }

    QMenuBar::item {
        padding: 4px 8px;
        background-color: transparent;
        color: #cdd6f4;
    }

    QMenuBar::item:selected {
        background-color: #585b70;
    }

    QMenuBar::item:pressed {
        background-color: #7f849c;
    }

    /* Menu */
    QMenu {
        background-color: #45475a;
        color: #cdd6f4;
        border: 1px solid #6c7086;
        padding: 4px;
        border-radius: 4px;
    }

    QMenu::item {
        padding: 4px 8px;
        background-color: transparent;
        color: #cdd6f4;
    }

    QMenu::item:selected {
        background-color: #585b70;
    }

    QMenu::item:pressed {
        background-color: #7f849c;
    }

    QMenu::separator {
        height: 1px;
        background-color: #6c7086;
        margin: 4px 0;
    }

    /* Buttons */
    QPushButton {
        background-color: #585b70;
        color: #cdd6f4;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: normal;
    }

    QPushButton:hover {
        background-color: #7f849c;
    }

    QPushButton:pressed {
        background-color: #6c7086;
    }

    /* Dialog */
    QDialog {
        background-color: #45475a;
        border: 1px solid #6c7086;
        border-radius: 4px;
    }

    QDialog QLabel {
        color: #cdd6f4;
        font-weight: bold;
    }

    QDialog QLineEdit {
        padding: 4px 8px;
        border: 1px solid #6c7086;
        border-radius: 4px;
        background-color: #45475a;
        color: #cdd6f4;
        font-size: 14px;
    }

    QDialog QLineEdit:focus {
        border-color: #89b4fa;
    }

    QDialog QPushButton {
        background-color: #89b4fa;
        color: #1e1e2e;
        padding: 4px 8px;
        border-radius: 4px;}

    QDialog QPushButton:hover {
        background-color: #b4befe;
    }

    QDialog QPushButton:pressed {
        background-color: #cba6f7;
    }

    /* Scrollbar Handle */
    QScrollBar::handle:vertical {
        background-color: #6c7086;
        min-height: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #89b4fa;
    }

    QScrollBar::handle:horizontal {
        background-color: #6c7086;
        min-width: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:horizontal:hover {
        background-color: #89b4fa;
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