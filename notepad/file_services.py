from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QTextStream, QFile, QIODevice
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QTextDocument
from pathlib import Path

class FileServices:
    # menu bar services
    def new_file(self):
        print('selected action new_file')

    def _set_title_window(self, file_path, target_window):
        target_window.current_file_path = file_path # current_file_path is an instance atribute of MainWindow
        name_file = Path(file_path).name
        target_window.setWindowTitle(name_file)

    def open_file(self, target_window):
        file_path, _= QFileDialog.getOpenFileName(target_window, "Open File", "", "Text documents (*.txt);;All Files(*.*)")
        
        if not file_path:
            return

        self._set_title_window(file_path, target_window)

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
        self._set_title_window(file_path, target_window)

        file = QFile(file_path)
        if file.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Text):
            try:    
                stream = QTextStream(file)
                stream << target_window.text_edit.toPlainText()
            except Exception as e:
                print(f"Error processing file : {file.errorString()}")
            finally:
                file.close()
        else:
            print(f'Error when opening the file : {file.errorString}')    

    def save_file(self, target_window):
        file_path = target_window.current_file_path
        if file_path:
            self._write_file(file_path, target_window)
        else:
            path = './new_file.txt'
            self._write_file(path, target_window)

    def save_as_file(self, target_window):
        file_path, _= QFileDialog.getSaveFileName(target_window, "Save As File", ".txt", "Text documments (*.txt);;All Files(*.*)")
        if not file_path:
            return
        self._write_file(file_path, target_window)

    def print_file(self, target_window):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, target_window)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            target_window.text_edit.print(printer)
        # agregar un mensaje en Statusbar para indicar que ya se imprimio el archivo