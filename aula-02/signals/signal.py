from abc import ABC, abstractmethod

import numpy as np


class Signal(ABC):
    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def get(self) -> np.ndarray:
        pass

    @abstractmethod
    def get_range(self):
        pass

    def get_energy(self):
        signal = self.get()
        squared_values = signal**2
        e = squared_values.sum()
        return e
