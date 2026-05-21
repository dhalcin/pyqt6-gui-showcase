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
            (0, 0): "C",
            (0, 1): "<",
            (0, 2): "%",
            (0, 3): "/",
            (1, 3): "X",
            (2, 3): "-",
            (3, 3): "+",
            (4, 3): "="
        }
        
        flag = 0

        for num in range(0, 21):
            self.button = QPushButton()
            
            row = num // 4
            column = num % 4

            if (row, column) in operations:
                self.button.setText(operations[(row, column)])
            else:
                flag += 1
                self.button.setText(str(flag))

            self.layout_keys.addWidget(self.button, row, column)

        self.keys.setLayout(self.layout_keys)

        self.main_layout.addWidget(self.keys)