Update Log
Version 0.3
Date: May 20, 2024

New Features and Enhancements:

Initialization of the Application Window:

The browser window is initially hidden and only shown after the introductory video finishes playing. This ensures users see the video first before interacting with the browser.
Full-Screen Video Playback:

Implemented VideoThread class for full-screen video playback using OpenCV. The video plays in full screen, utilizing the cv2 package. Make sure cv2 is installed in your environment for this feature to work.
Mouse Locking:

Added functionality to lock the mouse cursor within the browser widget area when clicked and unlock it upon releasing the mouse button. The cursor visibility is toggled appropriately.
Theme Switching:

Introduced toggle_theme function to switch between dark and light themes by altering the style sheet of the main window. Predefined style sheets are included in styles_dark.py and styles_light.py.
Handling Full-Screen Requests:

The handle_full_screen_request method now properly handles full-screen mode toggling. It hides and shows the toolbar, tabs, and status bar as necessary.
URL Navigation:

Improved navigate_to_url method to ensure the input URL is valid. It also handles searches when the input is not a valid URL.
Suggested Improvements Implemented:

Error Handling in VideoThread:

Added error handling for cases where the video file is missing or cannot be opened.
python
Copy code
def run(self):
    cap = cv2.VideoCapture(self.video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video file {self.video_path}")
        self.finished.emit()
        return
Resource Management:

Ensured resources like video files and web page instances are properly released or deleted to prevent memory leaks.
Browser Navigation with Key Shortcuts:

Added keyboard shortcuts for common actions such as opening a new tab, closing a tab, refreshing the page, etc.
python
Copy code
def setup_shortcuts(self):
    QShortcut(QKeySequence("Ctrl+T"), self, self.add_new_tab)
    QShortcut(QKeySequence("Ctrl+W"), self, lambda: self.close_tab(self.tabs.currentIndex()))
    QShortcut(QKeySequence("Ctrl+R"), self, self.reload_page)
Enhanced URL Validation:

Styling Improvements:

Ensured that icons (e.g., plus-light.svg, back-light.svg) are available in the working directory. Consider using resource files to bundle these assets within the application.
Code Modularity:

Split the code into smaller modules to enhance readability and maintainability. Separate modules were created for GUI code, video handling, and utility functions.
