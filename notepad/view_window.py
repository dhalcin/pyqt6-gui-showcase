from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFontDialog,
    QLabel,
    QHBoxLayout,
    QComboBox,
    QFrame
)
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
from functools import partial
import os

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
        font_dialog = QDialog()
        font_dialog.setWindowTitle('Fonts')
        font_dialog.setFixedSize(400, 300)

        layout = QVBoxLayout()
        
        combobox_container = QHBoxLayout()
        
        font_container = QVBoxLayout()
        title_font = QLabel('Font :')
        title_font.setFixedHeight(20)
        font_combobox = QComboBox()

        styles_path = './styles/fonts'
        files = os.listdir(styles_path)
        font_combobox.addItems(files)

        font_container.addWidget(title_font)
        font_container.addWidget(font_combobox)

        size_container = QVBoxLayout()
        size_title = QLabel('Size :')
        size_title.setFixedHeight(20)
        size_combobox = QComboBox()
        size_combobox.addItems([str(x) for x in range(8, 31, 2)])

        size_container.addWidget(size_title)
        size_container.addWidget(size_combobox)

        combobox_container.addLayout(font_container)
        combobox_container.addLayout(size_container)

        buttons_container = QHBoxLayout()
        options = {'apply': 'Apply', 'cancel': 'Cancel'}

        preview_frame = QFrame()
        preview_frame.setProperty('class', 'changes')
        
        preview_layout = QVBoxLayout(preview_frame)
        preview_frame.setFixedHeight(100)
        show_changes = QLabel('ABCDEXYZ')

        show_changes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        preview_layout.addWidget(show_changes)
        
        def update_label_font_preview():
            selected_font = font_combobox.currentText()#.strip()
            path_selected_fond = f'{styles_path}/{selected_font}'
            font_id = QFontDatabase.addApplicationFont(path_selected_fond)

            if font_id < 0:
                print('Faild to load fond in label')

            families = QFontDatabase.applicationFontFamilies(font_id)
            font_family = families[0]

            font = QFont(font_family)
            
            show_changes.setFont(QFont(font))

        font_combobox.currentTextChanged.connect(update_label_font_preview)

        def apply_fonts(btn_text, font_dialog):
            if btn_text != 'Apply':
                font_dialog.close()
                return
            
            selected_font = font_combobox.currentText()
            path_selected_font = f'{styles_path}/{selected_font}'
            font_id = QFontDatabase.addApplicationFont(path_selected_font)

            if font_id < 0:
                print('Failed to load font')
            
            families = QFontDatabase.applicationFontFamilies(font_id)
            font_family = families[0]

            font = QFont(font_family)

            target_window.text_edit.setFont(font)

            font_dialog.close()
            dialog.close()

        for btn_text in options.values():
            button = QPushButton(text=btn_text, parent=font_dialog)
            button.setProperty('class', 'btn')
            buttons_container.addWidget(button)
        
            # Using partial to avoid "Late Binding": freezes 
            # the arguments # (btn_text and font_dialog) in each 
            # iteration of the loop so that # each button maintains 
            # its correct value when clicked.
            button.clicked.connect(partial(apply_fonts, btn_text, font_dialog))
        
        layout.addLayout(combobox_container)
        layout.addWidget(preview_frame)
        layout.addLayout(buttons_container)

        font_dialog.setLayout(layout)
        font_dialog.exec()

        #dialog.close()


    def change_font(self, target_window):
        self._dialog(target_window, 'Fonts', ['Qt', 'Other Fonts'],[QLabel('To change the font, you can choose between these 2 options')])

