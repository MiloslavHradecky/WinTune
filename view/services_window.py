# services_window.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from utils.resources import resource_path
from utils.text_loader import get_description


class ServicesWindow(QWidget):
    def __init__(self, controller, main_window):
        super().__init__()
        self.controller = controller
        self.main_window = main_window
        self.setWindowTitle("Service Manager")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #1C1C1C; color: white; font-size: 16px;")

        style_app_btn_path = resource_path("view/themes/application_buttons.qss")
        with open(style_app_btn_path, encoding="utf-8") as f:
            app_btn_style = f.read()
            
        style_ctrl_btn_path = resource_path("view/themes/control_buttons.qss")
        with open(style_ctrl_btn_path, encoding="utf-8") as f:
            ctrl_btn_style = f.read()

        # 🧩 Set window icon using resource_path for compatibility
        icon_path = resource_path("view/assets/main.ico")
        self.setWindowIcon(QIcon(str(icon_path)))

        # 🏗️ Main horizontal layout
        main_layout = QVBoxLayout()
        content_layout = QHBoxLayout()

        # 🔹 Left column – buttons
        button_column = QVBoxLayout()

        # ✅ Backup button
        self.btn_backup = QPushButton("Backup Services")
        self.btn_backup.setStyleSheet(app_btn_style)
        button_column.addWidget(self.btn_backup)

        # Místo pro další tlačítka v budoucnu...
        button_column.addStretch()

        # 🔸 Right column – text with description
        description_text = get_description("services")
        self.lbl_info = QLabel(description_text)
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setAlignment(Qt.AlignmentFlag.AlignTop)
        content_layout.addLayout(button_column, 1)
        content_layout.addWidget(self.lbl_info, 2)

        # ➕ Merger
        main_layout.addLayout(content_layout)

        # 🧭 Back button
        self.btn_back = QPushButton("Return to Main Window")
        self.btn_back.setStyleSheet(ctrl_btn_style)
        main_layout.addStretch()
        main_layout.addWidget(self.btn_back)

        self.setLayout(main_layout)
