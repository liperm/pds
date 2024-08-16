import numpy as np
from .signal import Signal
from .plotter import SignalPlotter


class UnitStep(Signal):
    def __init__(
            self,
            gain: float = 1.0,
            offset: int = 0,
            start: int = 0,
            end: int = 1,
            step: int = 1):

        self._gain = gain
        self._offset = offset
        self._range = np.arange(start, end, step)

    def get(self):
        signal = np.zeros_like(self._range)
        signal[self._range >= self._offset] = 1*self._gain
        return signal

    def get_range(self):
        return self._range

    def plot(self):
        SignalPlotter.plot(self, title='Step Impulse')
