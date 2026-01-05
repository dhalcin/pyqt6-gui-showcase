from PyQt6.QtWidgets import QApplication
from file_services import FileServices
class MainController:
    def __init__(self, view):
        self.view = view
        self.file_services = FileServices(self.view)
        self.view.menu_bar.signal_actions.connect(self._handle_menu_actions)
    
    def _handle_menu_actions(self, action_name):
        content = self.file_services.open_file()
        