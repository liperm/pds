import numpy as np
from .plotter import SignalPlotter
from scipy.io.wavfile import write


class Signal():
    def __init__(self, samples: np.ndarray, fs: int):
        self._signal = samples
        self._fs = fs

    def plot(self):
        SignalPlotter.plot(signal=self._signal, range=self.get_range())

    def get(self) -> np.ndarray:
        return self._signal

    def get_range(self):
        return np.arange(0, self._signal.size, 1/self._fs)

    def get_sample_frequency(self):
        return self._fs

    def get_energy(self):
        signal = self.get()
        squared_values = signal**2
        e = squared_values.sum()
        return e

    def to_audio_file(self, file_name: str = 'result.pcm'):
        original_signal = self.get()
        cliped_signal = np.clip(original_signal, -32768, 32767)
        signal_int16 = cliped_signal.astype(np.int16)
        write(f'./{file_name}', self._fs, signal_int16)
