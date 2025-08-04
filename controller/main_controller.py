"""
main_controller.py

Main application controller. Manages initialization of main window,
application services, data loading, and GUI launch logic.
"""

from pathlib import Path
import getpass
import socket
from view.main_window import MainWindow
from utils.logger import get_logger


class MainController:
    def __init__(self):
        self.prepare_environment()
        self.logger = get_logger("MainController")
        self.log_start()
        self.window = MainWindow()

    @staticmethod
    def prepare_environment():
        Path("logs").mkdir(exist_ok=True)

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except OSError as e:
            ip = "Nezjištěno"
            self.logger.warning(f"IP adresu se nepodařilo zjistit: {e}")
        finally:
            s.close()
        return ip

    def log_start(self):
        username = getpass.getuser()
        ip_address = self.get_local_ip()
        self.logger.info(f"Aplikace spuštěna uživatelem: {username}, IP: {ip_address}")

    def run_app(self):
        # 🚀 Případné další logiky při startu (např. načtení dat, kontrola systému)
        self.window.show()
