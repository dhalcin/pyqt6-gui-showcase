import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QMenuBar,
    QTextEdit,
    QStatusBar,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Notepad')
        self.setMinimumSize(750, 650)

        #Menubar 
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        
        file_menu, edit_menu, format_menu, view_menu, help_menu = self.actions_dict()

        file_menu_container = self.create_menu('File')
        self.create_acctions(file_menu_container, file_menu)

        edit_menu_container = self.create_menu('Edit')
        self.create_acctions(edit_menu_container, edit_menu)

        format_menu_container = self.create_menu('Format')
        self.create_acctions(format_menu_container, format_menu)

        view_menu_container = self.create_menu('View')
        self.create_acctions(view_menu_container, view_menu)

        help_menu_container = self.create_menu('Help')
        self.create_acctions(help_menu_container, help_menu)

        self.text_edit = QTextEdit()

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        hola = QWidget()

        self.status_bar.showMessage('notepad', 0)

        self.setCentralWidget(self.text_edit)

    # bar menu methods
    def actions_dict(self):
        file_menu = {
            "file": "New",
            "new_window": "New Window",
            "open": "Open",
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

    def create_menu(self, menu_name):
        return self.menu_bar.addMenu(f'&{menu_name}')
         
    def create_acctions(self, menu_container, actions):
        for action_name, action_value in actions.items():
            menu_container.addAction(action_value)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()