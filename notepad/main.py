#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTextEdit,
    QStatusBar,
    QMessageBox
)
from menu_bar import MenuBar
from controllers import MainController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(750, 650)
        self.current_file_path = None
        self.setWindowTitle('Untitled: Notepad')

        #Menubar 
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(lambda: self.text_edit.document().setModified(True))

        self.setCentralWidget(self.text_edit)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.status_bar.showMessage('notepad', 0)

    def closeEvent(self, event): 
        if self.text_edit.document().isModified():
            response = QMessageBox.question(
                self,
                "Save As",
                "The Document has been modified. ¿You want to save the changes?",
                QMessageBox.StandardButton.Save |
                QMessageBox.StandardButton.Discard |
                QMessageBox.StandardButton.Cancel
            )

            if response == QMessageBox.StandardButton.Save:
                # We emit the signal for the controller to handle
                self.menu_bar.signal_actions.emit("save")
                event.accept()
            elif response == QMessageBox.StandardButton.Cancel:
                event.ignore()  # Stops closing
            else:
                event.accept()  # Close without saving (Discard)
        else:
            event.accept()

def load_styles(app):
    try:
        with open('./styles/styles.qss', 'r') as file:
            # print(file.read())
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print('File not found')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    load_styles(app)
    controller = MainController(window, window_class=MainWindow)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()