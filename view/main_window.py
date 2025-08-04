"""
main_window.py

Basic placeholder for application's main window.
Appears after splash screen and will be extended with full GUI.
"""

from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from utils.resources import resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinTune")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #121212;")

        # 🧩 Set window icon using resource_path for compatibility
        icon_path = resource_path("view/assets/main.ico")
        self.setWindowIcon(QIcon(str(icon_path)))

        # 📌 Dočasný text (placeholder)
        label = QLabel("WinTune GUI zatím ladíme...", self)
        label.setStyleSheet("color: white; font-size: 18px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
