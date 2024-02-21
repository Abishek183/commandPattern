from app.commands import Command, CommandHandler, list

class MenuCommand(Command):
    def execute(self):
        self.command_handler = CommandHandler()
        print("Menu",list)