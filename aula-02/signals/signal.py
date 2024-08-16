from abc import ABC, abstractmethod


class Signal(ABC):
    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_range(self):
        pass
