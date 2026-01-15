from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton

class View:

    def _create_button(self, text_button, dialog):
        return QPushButton(
            text=text_button,
            parent=dialog
        )
    
    def _search_content(self, content_line_edit, target_window, dialog):
        query = content_line_edit.text()

        # al realizar la busqueda se hace tomando en cuenta la posicion del cursor, por lo que found tiende hacer false.
        # The search takes into account the cursor's position, so `found` tends to return false. I made the cursor start from the beginning.
        cursor = target_window.text_edit.textCursor()
        cursor.movePosition(cursor.MoveOperation.Start)
        target_window.text_edit.setTextCursor(cursor)

        found = target_window.text_edit.find(query)
        
        if found:
            dialog.close()

    def find_content(self, target_window):
        dialog = QDialog(target_window)
        dialog.setWindowTitle('Search')

        layout = QVBoxLayout()
        line_edit = QLineEdit()
        button = self._create_button('Search', dialog)
        button.setFixedSize(45, 25)

        button.clicked.connect(lambda: self._search_content(line_edit, target_window, dialog))

        layout.addWidget(line_edit)
        layout.addWidget(button)
        dialog.setLayout(layout)

        dialog.exec()
    