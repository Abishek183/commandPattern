import logging
from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        logging.info("Hello, World!")
        logging.warning("Hello, World!")
        logging.debug("Hello, World!")
        logging.error("Hello, World!")
        print("Hello, World!")