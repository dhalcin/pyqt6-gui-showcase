from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox
)

class View:
    def _dialog(self, target_window, title, text_button, widget=None):
        dialog = QDialog(target_window)
        dialog.setWindowTitle(title)
        layout = QVBoxLayout()

        if widget:
            layout.addWidget(widget)
        
        for text in text_button:
            button = QPushButton(
                text=text,
                parent=dialog
            )

            button.setFixedSize(45, 25)
            # Menu find dialog box
            if text == 'Search':
                button.clicked.connect(lambda: self._search_content(widget, target_window, dialog)) # widget = QLineEdit()
            
            layout.addWidget(button)
        
        dialog.setLayout(layout)
        dialog.exec()

    def _search_content(self, content_line_edit, target_window, dialog):
        query = content_line_edit.text()

        # The search takes into account the cursor's position, so `found` tends to return false. I made the cursor start from the beginning.
        cursor = target_window.text_edit.textCursor()
        cursor.movePosition(cursor.MoveOperation.Start)
        target_window.text_edit.setTextCursor(cursor)

        found = target_window.text_edit.find(query)
        
        if found:
            dialog.close()
            return
        
        self._message_box(target_window)
    
    def _message_box(self, target_window):
        msg = QMessageBox(target_window)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("The contents were not found")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msg.exec()   

    def find_content(self, target_window):
        self._dialog(target_window, 'Search', ['Search'], QLineEdit())