class MainController:
    def __init__(self, view):
        self.view = view
        print(self.view)
        self.view.menu_bar.signal_actions.connect(self._handle_menu_actions)

    def _handle_menu_actions(self, action_name):
        print(action_name)