# services_window.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
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

        # 🏗️ Main horizontal layout
        main_layout = QVBoxLayout()
        content_layout = QHBoxLayout()

        # 🔹 Left column – buttons
        button_column = QVBoxLayout()

        # ✅ Backup button
        self.btn_backup = QPushButton("Backup Services")
        self.btn_backup.setStyleSheet("""
            QPushButton {
                background-color: #2ECC71;
                color: white;
                font-family: 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
            QPushButton:pressed {
                background-color: #1E8449;
                padding-left: 12px;
                padding-top: 12px;
            }
        """)
        button_column.addWidget(self.btn_backup)

        # Místo pro další tlačítka v budoucnu...
        button_column.addStretch()

        # 🔸 Right column – text with description
        self.lbl_info = QLabel("Modul 'Služby' umožňuje spravovat systémové služby ve Windows. Můžeš je zobrazit, spustit, zastavit nebo změnit jejich typ spuštění.\n\nNěkteré služby mohou být kritické pro systém — buď opatrný.")
        self.lbl_info.setWordWrap(True)
        self.lbl_info.setAlignment(Qt.AlignmentFlag.AlignTop)
        content_layout.addLayout(button_column, 1)
        content_layout.addWidget(self.lbl_info, 2)

        # ➕ Merger
        main_layout.addLayout(content_layout)

        # 🧭 Back button
        self.btn_back = QPushButton("Return to Main Window")
        self.btn_back.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                font-family: 'Segoe UI', sans-serif;
                font-size: 20px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #1C5980;
                padding-top: 12px;
                padding-left: 22px;
            }
        """)
        main_layout.addStretch()
        main_layout.addWidget(self.btn_back)

        self.setLayout(main_layout)
