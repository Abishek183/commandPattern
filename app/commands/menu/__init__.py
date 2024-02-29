from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        menu_list = self.command_handler.menuList()
        print("Menu", list(menu_list))