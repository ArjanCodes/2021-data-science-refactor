from numbers import Real
from typing import List


class Metric:
    values: List[Real] = []
    running_total: float = 0.0
    num_updates: float = 0.0
    average: float = 0.0

    def __init__(self):
        self.reset()

    def __str__(self):
        return f"Metric(average={self.average:0.4f})"

    def update(self, value: Real, batch_size: int):
        self.values.append(value)
        self.running_total += value * batch_size
        self.num_updates += batch_size
        self.average = self.running_total / self.num_updates

    def reset(self):
        self.values: list[Real] = []
        self.running_total: float = 0.0
        self.num_updates: float = 0.0
        self.average: float = 0.0
