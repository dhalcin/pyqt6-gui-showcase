from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QTextStream, QFile, QIODevice

class FileServices:

    # menu bar services
    def new_file(self):
        print('selected action new_file')

    def open_file(self, target_window):
        file_path, _= QFileDialog.getOpenFileName(target_window, "Open File", "", "Text documents (*.txt);All files(*.*)")
        
        if not file_path:
            return
        
        file = QFile(file_path)
        
        if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            try:    
                stream = QTextStream(file)
                target_window.text_edit.setPlainText(stream.readAll())
            except Exception as e:
                print(f"Error processing file : {file.errorString()}")
            
            finally:
                file.close()
        else:
            print(f'Error when opening the file : {file.errorString}')
