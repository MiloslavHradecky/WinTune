"""
splash_screen.py

Provides visual splash screen displayed during application initialization.
Includes logo fade-in, progress bar, and automatic transition to main window.
"""

from PyQt6.QtWidgets import QWidget, QLabel, QProgressBar, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QPainter
from PyQt6.QtCore import Qt, QTimer
from utils.resources import resource_path


class PixmapFader(QLabel):
    """
    QLabel subclass used to animate the fade-in effect of a QPixmap.

    Useful for adding visual polish to splash screens or transitions.
    The image gradually becomes visible using a timer and alpha blending.
    """

    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.full_pixmap = pixmap
        self.alpha = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.fade_in)  # type: ignore
        self.timer.start(90)  # ⏱️ Trigger every 90 ms

    def fade_in(self):
        # 🧪 Stop fading once fully opaque
        if self.alpha >= 255:
            self.timer.stop()
            return

        # 🖼️ Create transparent pixmap with gradual opacity
        faded = QPixmap(self.full_pixmap.size())
        faded.fill(Qt.GlobalColor.transparent)

        painter = QPainter(faded)
        painter.setOpacity(self.alpha / 255)
        painter.drawPixmap(0, 0, self.full_pixmap)
        painter.end()

        self.setPixmap(faded)
        self.alpha += 5  # 📌 Gradually increase alpha


class CustomSplash(QWidget):
    """
    Custom splash screen displayed during application startup.

    Shows a logo with fade-in animation, a loading message, and a progress bar.
    Automatically transitions to the main window once loading is complete.
    """

    def __init__(self, target_window):
        super().__init__()
        self.target_window = target_window  # 👀 Window to show after splash

        # 🖼️ Frameless & topmost styling
        self.setWindowTitle("WinTune")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(600, 400)
        self.setStyleSheet("QWidget { background-color: #202020; }")

        # 🧩 Set window icon using resource_path for compatibility
        icon_login_path = resource_path("view/assets/main.ico")
        self.setWindowIcon(QIcon(str(icon_login_path)))

        # 🎬 Display splash logo with fade-in animation
        splash_image_path = resource_path("view/assets/splash_logo.png")
        pixmap = QPixmap(str(splash_image_path))
        scaled = pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        logo_label = PixmapFader(scaled)

        # 📦 Layout configuration
        layout = QVBoxLayout()
        layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        self.setLayout(layout)

        # 💬 Display loading message
        self.message = QLabel("Inicializuji aplikaci...", self)
        self.message.setGeometry(100, 310, 400, 30)
        self.message.setStyleSheet("color: white; font-size: 20px;")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 📶 Progress bar setup
        self.progress = QProgressBar(self)
        self.progress.setGeometry(100, 350, 400, 25)
        self.progress.setRange(0, 200)
        self.progress.setValue(0)
        self.progress.setTextVisible(True)

        # 🎨 Styling the progress bar
        self.progress.setStyleSheet("""
            QProgressBar {
                color: white;
                border: 2px solid white;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #00c4ff;
                width: 10px;
                margin: 1px;
            }
        """)

        # 🕒 Timer to update progress bar and trigger transition
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)  # type: ignore
        self.timer.start(30)
        self.counter = 0

    def handle_timer(self):
        self.counter += 1
        self.progress.setValue(self.counter)

        # 🚪 When progress completes, close splash and show main window
        if self.counter >= 200:
            self.timer.stop()
            self.target_window.show()
            self.close()
