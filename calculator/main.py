import sys
import platform
from PyQt6.QtWidgets import QApplication
from view import View
        
def main():
    app = QApplication(sys.argv)

    try: 
        with open("style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass

    view = View()
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()