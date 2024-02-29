from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        # Register commands here


    def start(self):
        menu_instance = MenuCommand(self.command_handler)
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", menu_instance)

        print("Type 'exit' to exit and menu for list of commands")
        while True:  #REPL Read, Evaluate, Process, Loop
            self.command_handler.execute_command(input(">>> ").strip())

