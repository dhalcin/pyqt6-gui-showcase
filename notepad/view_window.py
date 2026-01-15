from PyQt6.QtWidgets import QDialog

class View:
    def find_content(self, target_window):
        dialog = QDialog(target_window)
        dialog.setWindowTitle('Search')
        dialog.exec()
