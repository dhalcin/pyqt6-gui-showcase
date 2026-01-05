from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QTextStream, QFile, QIODevice
from pathlib import Path

class FileServices:
    # menu bar services
    def new_file(self):
        print('selected action new_file')

    def open_file(self, target_window):
        file_path, _= QFileDialog.getOpenFileName(target_window, "Open File", "", "Text documents (*.txt);All files(*.*)")
        
        if not file_path:
            return

        target_window.current_file_path = file_path # current_file_path es un atributo de instancia de MainWindow
        name_file = Path(file_path).name
        target_window.setWindowTitle(name_file)

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


    def _write_file(self, file_path, target_window):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                stream = target_window.text_edit.toPlainText()
                file.write(stream)
        except FileNotFoundError:
            print('File not found')
        except Exception as e:
            print('error:', e)

    def save_file(self, target_window):
        file_path = target_window.current_file_path
        if file_path:
            self._write_file(file_path, target_window)
        else:
            path = './new_file.txt'
            self._write_file(path, target_window)
