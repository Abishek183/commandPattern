import logging
from app.commands import Command


class HelloCommand(Command):
    def execute(self):
        logging.info("Hi, How do you do")
        print("Hi, How do you do")