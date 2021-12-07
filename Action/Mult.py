from Action.Action import Action


class Mult(Action):
    def execute(self) -> None:
        self.get_mult()

    def get_mult(self):
        mult = 1
        for i in range(1, 10):
            mult = mult * i
        print('Mult ', mult)