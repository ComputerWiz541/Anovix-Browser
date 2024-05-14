import sys
import tldextract
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QVBoxLayout,
    QWidget, QTabWidget, QToolBar, QStatusBar, QTabBar
)
from PyQt6.QtGui import QIcon, QKeySequence, QCursor, QAction, QShortcut
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtCore import QT_VERSION_STR
from PyQt6 import QtCore
print(QtCore.QT_VERSION_STR)

from urllib.parse import urlparse
from styles import get_styles
import cv2

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super(BrowserTab, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.PlaybackRequiresUserGesture, False)
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)
        self.full_screen_view = None

        # Enable mouse locking feature
        self.is_mouse_locked = False

        # Connect the fullScreenRequested signal to the toggleFullScreen method
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.browser.page().fullScreenRequested.connect(lambda request: request.accept())
        self.browser.page().fullScreenRequested.connect(self.handle_full_screen_request)
        self.browser.titleChanged.connect(self.update_title)

    def update_title(self, title):
        self.window().tabs.setTabText(self.window().tabs.indexOf(self), title)

    def mousePressEvent(self, event):
        self.is_mouse_locked = True
        self.browser.setCursor(Qt.CursorShape.BlankCursor)
        self.browser.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        if self.is_mouse_locked:
            self.browser.setCursor(Qt.CursorShape.BlankCursor)

    def mouseReleaseEvent(self, event):
        self.is_mouse_locked = False
        self.browser.setCursor(Qt.CursorShape.ArrowCursor)
        self.browser.setMouseTracking(False)

    def unlock_mouse(self):
        self.browser.page().setMousePanActive(False)
        self.browser.setCursor(Qt.CursorShape.ArrowCursor)

    def handle_full_screen_request(self, request):
        main_window = self.window()
        if request.toggleOn():
            request.accept()
            main_window.toolbar.hide()
            main_window.tabs.hide()
            main_window.statusBar.hide()
            self.browser.setParent(None)
            self.browser.showFullScreen()
        else:
            request.accept()
            main_window.toolbar.show()
            main_window.tabs.show()
            main_window.statusBar.show()
            self.browser.showNormal()
            self.browser.setParent(self)
            self.layout.addWidget(self.browser)

class BrowserWindow(QMainWindow):
    def __init__(self):
        super(BrowserWindow, self).__init__()
        self.setWindowTitle("Anovix Browser")
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setWindowIcon(QIcon('browser_icon.png'))

        # Set the style sheet
        self.setStyleSheet(get_styles())

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.setCentralWidget(self.tabs)

        self.setup_toolbar()

        self.add_tab(QUrl('http://www.google.com'), 'Homepage')

    def setup_toolbar(self):
        self.toolbar = QToolBar("Main Toolbar")
        self.toolbar.setMovable(True)
        self.addToolBar(self.toolbar)

        new_tab_button = QAction(QIcon("plus.svg"), "New Tab", self)
        new_tab_button.triggered.connect(self.add_new_tab)
        self.toolbar.addAction(new_tab_button)

        self.back_button = QAction(QIcon("back.svg"), "Back", self)
        self.back_button.triggered.connect(self.navigate_back)
        self.toolbar.addAction(self.back_button)

        self.forward_button = QAction(QIcon("forward.svg"), "Forward", self)
        self.forward_button.triggered.connect(self.navigate_forward)
        self.toolbar.addAction(self.forward_button)

        self.reload_button = QAction(QIcon("reload.svg"), "Reload", self)
        self.reload_button.triggered.connect(self.reload_page)
        self.toolbar.addAction(self.reload_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.mousePressEvent = self.highlight_text
        self.toolbar.addWidget(self.url_bar)

        self.settings_button = QAction(QIcon("settings.svg"), "Settings", self)
        #self.settings_button.triggered.connect(self.open_settings)
        self.toolbar.addAction(self.settings_button)



    def add_new_tab(self):
        self.add_tab(QUrl('http://www.google.com'), 'New Tab')

    def add_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl('http://www.google.com')
        browser = BrowserTab()
        browser.browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.browser.urlChanged.connect(lambda qurl, browser=browser: self.update_urlbar(qurl, browser))
        browser.browser.loadFinished.connect(lambda _, i=i, browser=browser: self.update_urlbar(browser.browser.url(), browser))
        browser.browser.titleChanged.connect(browser.update_title)

        self.update_urlbar(qurl, browser)

    def close_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def update_urlbar(self, qurl, browser=None):
        if browser != self.current_tab():
            return
        self.url_bar.setText(qurl.toString())
        self.url_bar.setCursorPosition(0)

    def highlight_text(self, event):
        self.url_bar.selectAll()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if self.is_valid_url(url):
            self.current_tab().browser.setUrl(QUrl(url))
        else:
            extracted = tldextract.extract(url)
            if extracted.suffix:
                url = "http://" + url
                self.current_tab().browser.setUrl(QUrl(url))
            else:
                url = "https://www.google.com/search?q=" + url.replace(" ", "+")
                self.current_tab().browser.setUrl(QUrl(url))

    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def navigate_back(self):
        self.current_tab().browser.back()

    def navigate_forward(self):
        self.current_tab().browser.forward()

    def reload_page(self):
        self.current_tab().browser.reload()

    def current_tab(self):
        return self.tabs.currentWidget()

    def current_tab_changed(self, i):
        qurl = self.current_tab().browser.url()
        self.update_urlbar(qurl, self.current_tab())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())
