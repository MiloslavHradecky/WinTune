# services_window.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from utils.resources import resource_path


class ServicesWindow(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window
        self.setWindowTitle("Service Manager")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #1C1C1C; color: white; font-size: 16px;")

        # 🧩 Set window icon using resource_path for compatibility
        icon_path = resource_path("view/assets/main.ico")
        self.setWindowIcon(QIcon(str(icon_path)))

        layout = QVBoxLayout()

        lbl_info = QLabel("Tady bude seznam a ovládání služeb 💾")
        lbl_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl_info)

        # 🧭 Back button
        self.btn_back = QPushButton("⟵ Zpět")
        layout.addStretch()
        layout.addWidget(self.btn_back)

        self.setLayout(layout)
