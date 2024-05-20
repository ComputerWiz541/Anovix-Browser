import sys
import tldextract
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QVBoxLayout,
    QWidget, QTabWidget, QToolBar, QStatusBar
)
from PyQt6.QtGui import QIcon, QKeySequence, QCursor, QAction, QShortcut
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtCore import QUrl, Qt, pyqtSignal, QThread
import cv2
from urllib.parse import urlparse
from styles_dark import get_styles_dark
from styles_light import get_styles_light

class VideoThread(QThread):
    finished = pyqtSignal()

    def __init__(self, video_path):
        super().__init__()
        self.video_path = video_path

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print(f"Error: Cannot open video file {self.video_path}")
            self.finished.emit()
            return

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
        self.finished.emit()

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
        self.is_mouse_locked = False
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
        self.current_theme = "dark"
        self.setStyleSheet(get_styles_dark())

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
        self.video_thread = VideoThread("intro.mp4")
        self.video_thread.finished.connect(self.show_browser_window)
        self.video_thread.start()

    def toggle_theme(self):
        if self.current_theme == "dark":
            self.setStyleSheet(get_styles_light())
            self.current_theme = "light"
        else:
            self.setStyleSheet(get_styles_dark())
            self.current_theme = "dark"

    def show_browser_window(self):
        self.show()

    def setup_toolbar(self):
        self.toolbar = QToolBar("Main Toolbar")
        self.toolbar.setMovable(True)
        self.addToolBar(self.toolbar)

        new_tab_button = QAction(QIcon("plus-light.svg"), "New Tab", self)
        new_tab_button.triggered.connect(self.add_new_tab)
        self.toolbar.addAction(new_tab_button)

        self.back_button = QAction(QIcon("back-light.svg"), "Back", self)
        self.back_button.triggered.connect(self.navigate_back)
        self.toolbar.addAction(self.back_button)

        self.forward_button = QAction(QIcon("forward-light.svg"), "Forward", self)
        self.forward_button.triggered.connect(self.navigate_forward)
        self.toolbar.addAction(self.forward_button)

        self.reload_button = QAction(QIcon("reload-light.svg"), "Reload", self)
        self.reload_button.triggered.connect(self.reload_page)
        self.toolbar.addAction(self.reload_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.mousePressEvent = self.highlight_text
        self.toolbar.addWidget(self.url_bar)

        self.settings_button = QAction(QIcon("settings-light.svg"), "Settings", self)
        self.settings_button.triggered.connect(self.toggle_theme)
        self.toolbar.addAction(self.settings_button)

        self.setup_shortcuts()

    def setup_shortcuts(self):
        QShortcut(QKeySequence("Ctrl+T"), self, self.add_new_tab)
        QShortcut(QKeySequence("Ctrl+W"), self, lambda: self.close_tab(self.tabs.currentIndex()))
        QShortcut(QKeySequence("Ctrl+R"), self, self.reload_page)

    def highlight_text(self, event):
        self.url_bar.selectAll()

    def add_new_tab(self):
        self.add_tab(QUrl('http://www.google.com'), 'New Tab')

    def add_tab(self, url, label):
        new_tab = BrowserTab(self)
        new_tab.browser.setUrl(url)
        index = self.tabs.addTab(new_tab, label)
        self.tabs.setCurrentIndex(index)
        new_tab.update_title(label)

    def close_tab(self, index):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(index)

    def current_tab_changed(self, index):
        qurl = self.tabs.currentWidget().browser.url()
        self.update_urlbar(qurl, self.tabs.currentWidget().browser.page().title())

    def update_urlbar(self, qurl, title):
        self.url_bar.setText(qurl.toString())
        self.setWindowTitle(title)

    def navigate_to_url(self):
        url_text = self.url_bar.text()
        if not self.is_valid_url(url_text):
            url_text = 'https://www.google.com/search?q=' + url_text.replace(' ', '+')
        qurl = QUrl(url_text)
        if qurl.scheme() == '':
            qurl.setScheme('http')
        self.tabs.currentWidget().browser.setUrl(qurl)

    def is_valid_url(self, url):
        result = urlparse(url)
        return all([result.scheme, result.netloc])

    def navigate_back(self):
        self.tabs.currentWidget().browser.back()

    def navigate_forward(self):
        self.tabs.currentWidget().browser.forward()

    def reload_page(self):
        self.tabs.currentWidget().browser.reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    sys.exit(app.exec())
