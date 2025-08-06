"""
main_window.py

Basic placeholder for application's main window.
Appears after splash screen and will be extended with full GUI.
"""

from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGridLayout, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from utils.resources import resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WinTune")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #121212;")

        style_app_btn_path = resource_path("view/themes/application_buttons.qss")
        with open(style_app_btn_path, encoding="utf-8") as f:
            app_btn_style = f.read()

        # 🧩 Set window icon using resource_path for compatibility
        icon_path = resource_path("view/assets/main.ico")
        self.setWindowIcon(QIcon(str(icon_path)))

        # 🧩 Set images for buttons using resource_path for compatibility
        services_img_path = resource_path("view/assets/services.png")
        self.btn_services = QPushButton("Services")
        self.btn_services.setIcon(QIcon(str(services_img_path)))
        self.btn_services.setIconSize(QSize(32, 32))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        grid_layout = QGridLayout()

        # 🟦 First button: Services
        self.btn_services.setStyleSheet(app_btn_style)
        grid_layout.addWidget(self.btn_services, 0, 0)  # 📌 first column, first row

        main_layout.addLayout(grid_layout)
