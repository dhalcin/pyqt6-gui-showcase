from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit

class View:
    def find_content(self, target_window):
        dialog = QDialog(target_window)
        dialog.setWindowTitle('Search')

        layout = QVBoxLayout()
        line_edit = QLineEdit()

        layout.addWidget(line_edit)
        dialog.setLayout(layout)

        dialog.exec()
