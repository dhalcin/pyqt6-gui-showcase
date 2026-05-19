from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QLineEdit
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




        