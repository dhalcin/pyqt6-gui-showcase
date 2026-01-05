from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QTextStream, QFile

class FileServices:
    def __init__(self, main_window):
        self.main_window = main_window

    def open_file(self):
        file_path, _= QFileDialog.getOpenFileName(self.main_window, "Open File", "", "Text documents (*.txt);All files(*.*)")
        if file_path:
            with open(file_path, 'r') as file:
                self.main_window.text_edit.setPlainText(file.read())
