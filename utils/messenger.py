from PyQt6.QtWidgets import QMessageBox

class Messenger:
    @staticmethod
    def error(message: str, title: str = "Error"):
        box = QMessageBox()
        box.setIcon(QMessageBox.Icon.Critical)
        box.setWindowTitle(title)
        box.setText(message)
        box.exec()

    @staticmethod
    def info(message: str, title: str = "Information"):
        box = QMessageBox()
        box.setIcon(QMessageBox.Icon.Information)
        box.setWindowTitle(title)
        box.setText(message)
        box.exec()

    @staticmethod
    def warning(message: str, title: str = "Warning"):
        box = QMessageBox()
        box.setIcon(QMessageBox.Icon.Warning)
        box.setWindowTitle(title)
        box.setText(message)
        box.exec()
