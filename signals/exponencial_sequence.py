import numpy as np
from .signal import Signal
from .plotter import SignalPlotter


class ExponencialSequence(Signal):
    def __init__(
            self,
            step: float = 1.0,
            start: int = 0,
            end: int = 1,
            gain: float = 1.0,
            a: float = 1.0):

        self._range = np.arange(start, end, step)
        self._gain = gain
        self._a = a

    def get(self):
        signal = self._gain * self._a**self._range
        return signal

    def get_range(self):
        return self._range

    def plot(self):
        SignalPlotter.plot(
            signal=self.get(),
            range=self.get_range(),
            title='Exponencial Sequence')
