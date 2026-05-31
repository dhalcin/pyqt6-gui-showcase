from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QSizePolicy,
    QGridLayout,
    QPushButton
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator

class View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setMinimumSize(330, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        central_widget.setLayout(self.main_layout)

        # Display
        self.display = QWidget()
        self.layout_display = QVBoxLayout()
        self.layout_display.setContentsMargins(0, 0, 0, 0)
        self.layout_display.setSpacing(0)

        self.historial_line = QLineEdit()
        self.historial_line.setObjectName("historial_line")

        self.historial_line.setReadOnly(True)
        self.historial_line.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.historial_line.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.input_line = QLineEdit()
        self.input_line.setValidator(QIntValidator())
        self.input_line.setObjectName("input_line")

        self.input_line.setReadOnly(False)
        self.input_line.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.input_line.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.layout_display.addWidget(self.historial_line, stretch=1)
        self.layout_display.addWidget(self.input_line, stretch=2)

        self.display.setLayout(self.layout_display)

        self.main_layout.addWidget(self.display, stretch=2)

        # keys
        self.keys = QWidget()
        self.layout_keys = QGridLayout()
        self.layout_keys.setContentsMargins(0, 0, 0, 0)
        self.layout_keys.setSpacing(1)
        
        symbols = {
            "file_1": ["C", "<", "%", "/"],
            "file_2": [1, 2, 3, "X"],
            "file_3": [4, 5, 6, "-"],
            "file_4": [7, 8, 9, "+"],
            "file_5": [0, ".", "="]
        }

        i = 0

        for files in symbols.values():
            for ch in range(0, len(files)):         
                row = i // 4
                column = i % 4
                i += 1
                button = QPushButton()

                if not isinstance(files[ch], int):
                    if not files[ch] == ".":
                        button.setObjectName("fun_btn")

                button.setText(str(files[ch]))
                button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                button.setCursor(Qt.CursorShape.PointingHandCursor)
                
                if files[ch] == "=":
                    self.layout_keys.addWidget(button, 4, 2, 1, 2)
                    
                else:
                    self.layout_keys.addWidget(button, row, column)
                

        self.keys.setLayout(self.layout_keys)

        self.main_layout.addWidget(self.keys, stretch=5)
