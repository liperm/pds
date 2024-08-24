from matplotlib import pyplot as plt
import numpy as np


class SignalPlotter:
    @staticmethod
    def plot(
            signal: np.ndarray,
            range: np.arange,
            title: str = '',
            x_label: str = 'n'):
        plt.stem(range, signal)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()
