from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtCore import pyqtSignal
from functools import partial

class MenuBar(QMenuBar):
    signal_actions = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.main_windows = parent
        
        file_menu, edit_menu, format_menu, view_menu, help_menu = self._actions_dict()
        
        file_menu_container = self._create_menu('File')
        self.create_actions(file_menu_container, file_menu)

        edit_menu_container = self._create_menu('Edit')
        self.create_actions(edit_menu_container, edit_menu)

        format_menu_container = self._create_menu('Format')
        self.create_actions(format_menu_container, format_menu)

        view_menu_container = self._create_menu('View')
        self.create_actions(view_menu_container, view_menu)

        help_menu_container = self._create_menu('Help')
        self.create_actions(help_menu_container, help_menu)

    def _actions_dict(self):
        file_menu = {
            "new_file": "New File",
            "new_window": "New Window",
            "open_file": "Open File",
            "save": "Save",
            "save_as": "Save As",
            "print": "Print",
            "exit": "Exit"
        }
        
        edit_menu = {
            "find": "Find"
        }
        
        format_menu = {
            "font": "Font",
            "size": "Size"
        }

        view_menu = {
            "zoom_in": "Zoom In",
            "zoom_out": "Zoom Out",
            "restore": "Restore Default Zoom",
            "status_bar": "Status Bar"
        }

        help_menu = {
            "about": "About Notepad"
        }
        
        return file_menu, edit_menu, format_menu, view_menu, help_menu
    
    def _create_menu(self, menu_name):
        return self.addMenu(f'&{menu_name}')
    
    def create_actions(self, menu_container, actions):
        for action_name, action_value in actions.items():
            action = menu_container.addAction(action_value)
            action.triggered.connect(
                partial(self.signal_actions.emit, action_name)
            )
