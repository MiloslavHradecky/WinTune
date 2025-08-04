"""
main_controller.py

Main application controller. Manages initialization of main window,
application services, data loading, and GUI launch logic.
"""

from view.main_window import MainWindow


class MainController:
    def __init__(self):
        self.window = MainWindow()

    def run_app(self):
        # 🚀 Případné další logiky při startu (např. načtení dat, kontrola systému)
        self.window.show()
