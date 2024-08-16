import numpy as np
from .signal import Signal
from .plotter import SignalPlotter


class Cosine(Signal):
    def __init__(
            self,
            frequency: float = 1.0,
            sampling_rate: int = 10,
            duration: float = 1.0,
            gain: float = 1.0,):

        self._frequency = frequency
        self._sampling_rate = sampling_rate
        self._duration = duration
        self._gain = gain
        self._t = np.arange(0, duration, 1/sampling_rate)

    def get(self):
        cosine_signal = self._gain * np.cos(
            2 * np.pi * self._frequency * self._t)
        return cosine_signal

    def get_range(self):
        return self._t

    def plot(self):
        SignalPlotter.plot(self, title='Cosine')
