import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QMenuBar
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clone of Notepad')
        self.setMinimumSize(750, 650)

        #Menubar 
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)

        self.create_menu_bar()
        
    def actions_dict(self):
        return {
            "File": {
                "file": "New",
                "new_window": "New Window",
                "open": "Open",
                "save_as": "Save As",
                "Print": "Print",
                "Exit": "Exit"
            },
            "Edit": {
                "find": "Find"
            },
            "Format": {
                "font": "Font",
                "size": "Size"
            },
            "View": {
                "zoom_in": "Zoom In",
                "zoom_out": "Zoom Out",
                "restore": "Restore Default Zoom",
                "status_bar": "Status Bar"
            },
            "Help": {
                "about": "About Notepad"
            }
        }

    def create_menu_bar(self):
        actions = self.actions_dict()
        for menu, menu_value in actions.items():
            menu_name = self.menu_bar.addMenu(f'{menu}')
            for sub_menu_name, sub_menu_value in menu_value.items():
                menu_name.addAction(sub_menu_value)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()