"""
main.py

Application entry point. Shows splash screen, initializes main controller,
and launches the main GUI window.
"""

import sys
from PyQt6.QtWidgets import QApplication
from controller.main_controller import MainController
from view.splash_screen import CustomSplash

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 🌟 Initialize the main controller (including the main window)
    controller = MainController()

    # 🖼️ Create a splash screen with a transition to the main window
    splash = CustomSplash(target_window=controller.window)
    splash.show()

    # 🏁 Start the app
    sys.exit(app.exec())
