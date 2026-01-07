#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTextEdit,
    QStatusBar,
)
from menu_bar import MenuBar
from controllers import MainController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Notepad')
        self.setMinimumSize(750, 650)
        self.current_file_path = None

        #Menubar 
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.text_edit = QTextEdit()

        self.setCentralWidget(self.text_edit)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.status_bar.showMessage('notepad', 0)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    controller = MainController(window, window_class=MainWindow)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()