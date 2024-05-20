def get_styles_light():
    styles = """
    /* General Styles */
    QMainWindow {
        background-color: #eff1f5;
        color: #4c4f69;
        font-family: "Segoe UI", sans-serif;
    }

    /* Tab Widget */
    QTabWidget::pane {
        border: none;
        background-color: #ccd0da;
        border-radius: 4px;
        padding: 4px;
    }

    QTabBar {
        background-color: #ccd0da;
        border-bottom: 1px solid #9ca0b0;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QTabBar::tab {
        background-color: #ccd0da;
        color: #4c4f69;
        padding: 8px 16px;
        min-width: 120px;
        border: 1px solid transparent;
        border-bottom: 1px solid transparent;
        font-weight: normal;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QTabBar::tab:selected {
        background-color: #eff1f5;
        color: #4c4f69;
        border-color: #9ca0b0;
        border-bottom: 1px solid #ccd0da;
    }

    QTabBar::tab:!selected {
        margin-top: 2px;
    }

    QTabBar::tab:hover {
        background-color: #acb0be;
    }

    QTabBar::close-button {
        qproperty-icon: url(close.svg);
        subcontrol-origin: padding;
        padding: 2px;
        border-radius: 2px;
        background-color: transparent;
    }

    QTabBar::close-button:hover {
        background-color: #d20f39;
    }

    /* Toolbar */
    QToolBar {
        background-color: #eff1f5;
        padding: 4px;
        border-bottom: 1px solid #9ca0b0;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    QToolBar QToolButton {
        padding: 4px;
        border-radius: 4px;
    }

    QToolBar QToolButton:hover {
        background-color: #acb0be;
    }

    /* URL Bar */
    QLineEdit {
        padding: 4px 8px;
        border: 1px solid #9ca0b0;
        border-radius: 4px;
        background-color: #ccd0da;
        color: #4c4f69;
        font-size: 14px;
        selection-background-color: #1e66f5;
        selection-color: #eff1f5;
    }

    QLineEdit:focus {
        border-color: #1e66f5;
    }

    /* Status Bar */
    QStatusBar {
        background-color: #eff1f5;
        color: #4c4f69;
        padding: 4px;
        border-top: 1px solid #9ca0b0;
        font-size: 12px;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
    }

    /* Misc */
    QToolTip {
        background-color: #1e66f5;
        color: #eff1f5;
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
        background-color: #eff1f5;
        width: 16px;
        margin: 0;
    }

    QScrollBar::handle:vertical {
        background-color: #9ca0b0;
        min-height: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #1e66f5;
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0;
        background: none;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        background-color: #eff1f5;
        height: 16px;
        margin: 0;
    }

    QScrollBar::handle:horizontal {
        background-color: #9ca0b0;
        min-width: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:horizontal:hover {
        background-color: #1e66f5;
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
        background-color: #eff1f5;
        color: #4c4f69;
        padding: 4px;
        border-bottom: 1px solid #9ca0b0;
    }

    QMenuBar::item {
        padding: 4px 8px;
        background-color: transparent;
        color: #4c4f69;
    }

    QMenuBar::item:selected {
        background-color: #acb0be;
    }

    QMenuBar::item:pressed {
        background-color: #8c8fa1;
    }

    /* Menu */
    QMenu {
        background-color: #ccd0da;
        color: #4c4f69;
        border: 1px solid #9ca0b0;
        padding: 4px;
        border-radius: 4px;
    }

    QMenu::item {
        padding: 4px 8px;
        background-color: transparent;
        color: #4c4f69;
    }

    QMenu::item:selected {
        background-color: #acb0be;
    }

    QMenu::item:pressed {
        background-color: #8c8fa1;
    }

    QMenu::separator {
        height: 1px;
        background-color: #9ca0b0;
        margin: 4px 0;
    }

    /* Buttons */
    QPushButton {
        background-color: #acb0be;
        color: #4c4f69;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: normal;
    }

    QPushButton:hover {
        background-color: #8c8fa1;
    }

    QPushButton:pressed {
        background-color: #9ca0b0;
    }

    /* Dialog */
    QDialog {
        background-color: #ccd0da;
        border: 1px solid #9ca0b0;
        border-radius: 4px;
    }

    QDialog QLabel {
        color: #4c4f69;
        font-weight: bold;
    }

    QDialog QLineEdit {
        padding: 4px 8px;
        border: 1px solid #9ca0b0;
        border-radius: 4px;
        background-color: #ccd0da;
        color: #4c4f69;font-size: 14px;
    }

    QDialog QLineEdit:focus {
        border-color: #1e66f5;
    }

    QDialog QPushButton {
        background-color: #1e66f5;
        color: #eff1f5;
        padding: 4px 8px;
        border-radius: 4px;
    }

    QDialog QPushButton:hover {
        background-color: #7287fd;
    }

    QDialog QPushButton:pressed {
        background-color: #8839ef;
    }

    /* Scrollbar Handle */
    QScrollBar::handle:vertical {
        background-color: #9ca0b0;
        min-height: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #1e66f5;
    }

    QScrollBar::handle:horizontal {
        background-color: #9ca0b0;
        min-width: 20px;
        border-radius: 4px;
    }

    QScrollBar::handle:horizontal:hover {
        background-color: #1e66f5;
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