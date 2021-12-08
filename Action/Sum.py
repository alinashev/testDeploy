import numpy as np
from Action.Action import Action


class Sum(Action):
    def execute(self) -> None:
        self.get_sum()
        self.get_array()

    def get_sum(self):
        sum = 0
        for i in range(0, 10):
            sum = sum + i
        print('sum ', sum)

    def get_array(self):
        a = np.arange(0, 10, 2)
        for i in a:
            print(i)
