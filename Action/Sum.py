from Action.Action import Action


class Sum(Action):
    def execute(self) -> None:
        self.get_sum()

    def get_sum(self):
        sum = 0
        for i in range(0, 10):
            sum = sum + i
        print('sum ', sum)