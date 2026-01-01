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
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)
        
        menu_bar.addMenu('&File')
        menu_bar.addMenu('&Edit')
        menu_bar.addMenu('&Format')
        menu_bar.addMenu('&View')
        menu_bar.addMenu('&Help')

    def actions_dict(self):
        dicts = {
            "file": {
                "file": "New",
                "new_window": "New Window",
                "open": "Open",
                "save_as": "Save As",
                "Print": "Print",
                "Exit": "Exit"
            },
            "edit": {
                "find": "Find"
            },
            "format": {
                "font": "Font",
                "size": "Size"
            },
            "view": {
                "zoom_in": "Zoom In",
                "zoom_out": "Zoom Out",
                "restore": "Restore Default Zoom",
                "status_bar": "Status Bar"
            },
            "help": {
                "about": "About Notepad"
            }
        }

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()