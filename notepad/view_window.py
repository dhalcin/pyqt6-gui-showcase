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
            
            elif text == 'Qt':
                button.clicked.connect(lambda: self._font_qt(target_window, dialog))
                
            elif text == 'Other Fonts':
                button.clicked.connect(lambda: self._other_fonts(target_window, dialog))

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
    
    def _font_qt(self, target_window, dialog):
        # Native Qt styles
        font, ok = QFontDialog.getFont(target_window.text_edit.font(), target_window)
        if ok:
            target_window.text_edit.setFont(font)
            dialog.close()

    def _other_fonts(self, target_window, dialog):
        font_id = QFontDatabase.addApplicationFont('./styles/fonts/GoogleSans-Italic-VariableFont_GRAD,opsz,wght.ttf')
        if font_id < 0:
            print('Failed to laod font')
        
        families = QFontDatabase.applicationFontFamilies(font_id)
        font_family = families[0]
        target_window.text_edit.setFont(QFont(font_family))
        dialog.close()

    def change_font(self, target_window):
        self._dialog(target_window, 'Fonts', ['Qt', 'Other Fonts'],[QLabel('To change the font, you can choose between these 2 options')])

