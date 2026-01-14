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
                "Guardar Cambios",
                "El Documento ha sido modificado. ¿Deseas guardar los cambios?",
                QMessageBox.StandardButton.Save |
                QMessageBox.StandardButton.Discard |
                QMessageBox.StandardButton.Cancel
            )

            if response == QMessageBox.StandardButton.Save:
                # We emit the save signal
                self.menu_bar.signal_actions.emit("save")
                
                # We check if it was actually saved, the document should no longer be marked as modified
                if not self.text_edit.document().isModified():
                    event.accept()
                else:
                    # If the user canceled the "Save As" dialog, we do not close
                    event.ignore() 
                    
            elif response == QMessageBox.StandardButton.Discard:
                event.accept() # Close without saving
            else:
                event.ignore() # Cancel: stays in the window
        else:
            event.accept()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    controller = MainController(window, window_class=MainWindow)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()