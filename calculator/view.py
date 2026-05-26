from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QLineEdit,
    QGridLayout,
    QPushButton
)

class View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setMinimumSize(330, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        # Display
        self.display = QWidget()
        self.layout_display = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.line_edit = QLineEdit()

        self.layout_display.addWidget(self.text_edit)
        self.layout_display.addWidget(self.line_edit)

        self.display.setLayout(self.layout_display)

        self.main_layout.addWidget(self.display)

        # keys
        self.keys = QWidget()
        self.layout_keys = QGridLayout()
        
        symbols = {
            "file_1": ["C", "<", "%", "/"],
            "file_2": ["1", "2", "3", "X"],
            "file_3": ["4", "5", "6", "-"],
            "file_4": ["7", "8", "9", "+"],
            "file_5": ["0", ".", "="]
        }

        i = 0

        for files in symbols.values():
            for ch in range(0, len(files)):         
                row = i // 4
                column = i % 4
                i += 1
                self.button = QPushButton()
                
                if files[ch] == "=":
                    self.layout_keys.addWidget(self.button, 4, 2, 1, 2)
                    
                else:
                    self.layout_keys.addWidget(self.button, row, column)
                self.button.setText(files[ch])

        self.keys.setLayout(self.layout_keys)

        self.main_layout.addWidget(self.keys)