from Action.Mult import Mult
from Action.Sum import Sum


class Router:
    def __init__(self, version: int) -> None:
        self.version = version

    def generate_menu(self) -> None:
        self.menu = {1: Sum(),
                     2: Mult()}

    def selection_version(self) -> None:
        self.menu[self.version].execute()
