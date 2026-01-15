from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton

class View:

    def _create_button(self, text_button, dialog):
        return QPushButton(
            text=text_button,
            parent=dialog
        )

    def find_content(self, target_window):
        dialog = QDialog(target_window)
        dialog.setWindowTitle('Search')

        layout = QVBoxLayout()
        line_edit = QLineEdit()
        button = self._create_button('Search', dialog)
        button.setFixedSize(45, 25)

        layout.addWidget(line_edit)
        layout.addWidget(button)
        dialog.setLayout(layout)

        dialog.exec()
