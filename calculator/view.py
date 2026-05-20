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

        operations = {
            "C": (0, 0),
            "<<": (0, 1),
            "%": (0, 2),
            "/": (0, 3),
            "X": (1, 4),
            "-": (2, 4),
            "+": (3, 4),
            "=": (4, 4) 
        }

        for num in range(0, 21):
            self.button = QPushButton()
            
            row = num // 4
            column = num % 4

            if (row, column) == operations[num]:
                self.button.setText(operations)
            else:
                self.button.setText(str(num))

            self.layout_keys.addWidget(self.button, row, column)

        self.keys.setLayout(self.layout_keys)

        self.main_layout.addWidget(self.keys)