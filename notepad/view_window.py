from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton

class View:

    def _create_button(self, text_button, dialog):
        return QPushButton(
            text=text_button,
            parent=dialog
        )
    
    def _search_content(self, content_line_edit, target_window):
        txt = target_window.text_edit.toPlainText()
        content_to_search = content_line_edit.text()
        print(txt.find(content_to_search))

    def find_content(self, target_window):
        dialog = QDialog(target_window)
        dialog.setWindowTitle('Search')

        layout = QVBoxLayout()
        line_edit = QLineEdit()
        button = self._create_button('Search', dialog)
        button.setFixedSize(45, 25)

        button.clicked.connect(lambda: self._search_content(line_edit, target_window))

        layout.addWidget(line_edit)
        layout.addWidget(button)
        dialog.setLayout(layout)

        dialog.exec()
