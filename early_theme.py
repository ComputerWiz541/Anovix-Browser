import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QGridLayout, QDialog, QRadioButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Web Browser")
        self.setWindowState(Qt.WindowMaximized)  # Maximize the window to take up the whole screen

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setStyleSheet("QLineEdit { border: 2px solid #ccc; border-radius: 5px; padding: 5px; }")

        self.go_button = QPushButton(QIcon("search.png"), "")
        self.go_button.clicked.connect(self.navigate_to_url)
        self.go_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; border: 2px solid #ccc; border-radius: 5px; padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; } QPushButton:hover { background-color: #f0f0f0; }")

        self.back_button = QPushButton(QIcon("back.png"), "")
        self.back_button.clicked.connect(self.browser.back)
        self.back_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; border: 2px solid #ccc; border-radius: 5px; padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; } QPushButton:hover { background-color: #f0f0f0; }")

        self.forward_button = QPushButton(QIcon("forward.png"), "")
        self.forward_button.clicked.connect(self.browser.forward)
        self.forward_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; border: 2px solid #ccc; border-radius: 5px; padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; } QPushButton:hover { background-color: #f0f0f0; }")

        self.reload_button = QPushButton(QIcon("reload.png"), "")
        self.reload_button.clicked.connect(self.browser.reload)
        self.reload_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; border: 2px solid #ccc; border-radius: 5px; padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; } QPushButton:hover { background-color: #f0f0f0; }")

        self.settings_button = QPushButton(QIcon("settings.png"), "")
        self.settings_button.clicked.connect(self.open_settings)
        self.settings_button.setStyleSheet("QPushButton { background-color: #ffffff; color: #000000; border: 2px solid #ccc; border-radius: 5px; padding: 5px 10px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; } QPushButton:hover { background-color: #f0f0f0; }")

        self.layout = QGridLayout()
        self.layout.addWidget(self.back_button, 0, 0)
        self.layout.addWidget(self.forward_button, 0, 1)
        self.layout.addWidget(self.reload_button, 0, 2)
        self.layout.addWidget(self.url_bar, 0, 3)
        self.layout.addWidget(self.go_button, 0, 4)
        self.layout.addWidget(self.settings_button, 0, 5)
        self.layout.addWidget(self.browser, 1, 0, 1, 6)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            if "." not in url:
                url = "https://www.google.com/search?q=" + url.replace(" ", "+")
            else:
                url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def open_settings(self):
        settings_dialog = QDialog(self)
        settings_dialog.setWindowTitle("Settings")
        settings_layout = QVBoxLayout()

        developer_theme_radio = QRadioButton("Developer Theme")
        developer_theme_radio.setChecked(True)
        developer_theme_radio.clicked.connect(self.set_developer_theme)

        gaming_theme_radio = QRadioButton("Gaming Theme")
        gaming_theme_radio.clicked.connect(self.set_gaming_theme)

        minimal_theme_radio = QRadioButton("Minimal Theme")
        minimal_theme_radio.clicked.connect(self.set_minimal_theme)

        settings_layout.addWidget(developer_theme_radio)
        settings_layout.addWidget(gaming_theme_radio)
        settings_layout.addWidget(minimal_theme_radio)

        settings_dialog.setLayout(settings_layout)
        settings_dialog.exec_()

    def set_developer_theme(self):
        self.browser.setStyleSheet("background-color: #ffffff; color: #000000;")

    def set_gaming_theme(self):
        self.browser.setStyleSheet("background-color: #000000; color: #ffffff;")

    def set_minimal_theme(self):
        self.browser.setStyleSheet("background-color: #f0f0f0; color: #000000;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
