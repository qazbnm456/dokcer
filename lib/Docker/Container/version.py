"""This module contains `docker version` class"""

from .command import Command

class Version(Command):
    """This class implements `docker version` command"""

    name = "version"
    require = []

    def __init__(self):
        Command.__init__(self)
        self.settings[self.name] = None

    def eval_command(self, args):
        self.settings[self.name] = self.client.version()

    def final(self):
        return self.settings[self.name]