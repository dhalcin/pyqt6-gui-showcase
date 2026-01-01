import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QMenuBar
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clone of Notepad')
        self.setMinimumSize(750, 650)

        #Menubar 
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)
        menu_bar.addMenu('&File')
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()