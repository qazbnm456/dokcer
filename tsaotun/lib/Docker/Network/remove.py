"""This module contains `docker network remove` class"""

from docker.errors import APIError

from .command import Command


class Remove(Command):
    """This class implements `docker network remove` command"""

    name = "network remove"
    require = []

    def __init__(self):
        Command.__init__(self)
        self.settings[self.name] = None

    def eval_command(self, args):
        try:
            Ids = []
            networks = args["networks"]
            del args["networks"]
            for Id in networks:
                Ids.append(Id)
                self.client.remove_network(Id)
            self.settings[self.name] = '\n'.join(Ids)
        except APIError as e:
            raise e

    def final(self):
        return self.settings[self.name]
