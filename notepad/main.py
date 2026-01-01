import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication 
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clone of Notepad')
        self.setMinimumSize(750, 650)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()