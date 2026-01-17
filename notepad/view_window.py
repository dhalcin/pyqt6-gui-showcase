from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFontDialog,
    QLabel,
    QHBoxLayout
)
from PyQt6.QtGui import QFont, QFontDatabase

class View:
    def _dialog(self, target_window, title, text_button, widgets=None):
        dialog = QDialog(target_window)
        dialog.setWindowTitle(title)
        layout = QVBoxLayout()

        if widgets:
            for widget in widgets:
                layout.addWidget(widget)
        
        buttons_container = QHBoxLayout()
        for text in text_button:
            button = QPushButton(
                text=text,
                parent=dialog
            )

            button.setFixedSize(45, 25)
            button.setProperty('class', 'btn')
            button.setObjectName(text.replace(' ', '-'))
            # Menu find dialog box
            if text == 'Search':
                button.clicked.connect(lambda: self._search_content(widget, target_window, dialog)) # widget = QLineEdit()
            
            buttons_container.addWidget(button)
        layout.addLayout(buttons_container)
        
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
        # If the content of text_edit is not empty, the search is performed
        if target_window.text_edit.toPlainText() != '':
            self._dialog(target_window, 'Search', ['Search'], [QLineEdit()])
    
    def change_font(self, target_window):
        #Native Qt styles
        font, ok = QFontDialog.getFont(target_window.text_edit.font(), target_window)
        if ok:
            target_window.text_edit.setFont(font)
