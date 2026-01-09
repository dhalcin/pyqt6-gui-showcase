from PyQt6.QtCore import Qt
from file_services import FileServices

class MainController:
    def __init__(self, view, window_class):
        self.view = view
        self.window_class = window_class
        self.file_services = FileServices()
        self.windows = []
        self._setup_window(self.view)
        
    def _setup_window(self, window):
        window.menu_bar.signal_actions.connect(
            lambda action_name: self._handle_menu_actions(action_name, window)
        )
        
        #Configurar comportamiento de cierre
        # Esto le dice a Qt que destruya el objeto C++ al cerrar la ventana
        window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        
        #Limpiar nuestra lista de Python cuando la ventana se destruya
        # Usamos una lambda para saber exactamente qué ventana remover
        window.destroyed.connect(lambda: self._on_window_destroyed(window))

        self.windows.append(window)
        window.show()

    def _on_window_destroyed(self, window):
        if window in self.windows:
            self.windows.remove(window)

    def _handle_menu_actions(self, action_name, sender_window):
        # Al usar sender_window, cada ventana es independiente
        actions_menu = {
            #"new_file": "new_file",
            "new_window": self.open_new_window,
            "open_file": lambda: self.file_services.open_file(sender_window),
            "save": lambda: self.file_services.save_file(sender_window),
            "save_as": lambda: self.file_services.save_as_file(sender_window),
            "print": lambda: self.file_services.print_file(sender_window)
            # "exit"
        }

        action = actions_menu.get(action_name)
        if action:
            action()

    def open_new_window(self):
        new_window = self.window_class()
        new_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self._setup_window(new_window)
        
