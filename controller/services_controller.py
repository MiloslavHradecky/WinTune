# services_controller.py

from view.services_window import ServicesWindow


class ServicesController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = ServicesWindow(self, main_window)

        # ✅ Let's connect the handle
        self.window.btn_back.clicked.connect(self.handle_back_click)

    def show(self):
        self.window.show()

    def handle_back_click(self):
        self.window.close()
        self.main_window.show()
