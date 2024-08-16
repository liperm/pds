from matplotlib import pyplot as plt
from .signal import Signal


class SignalPlotter:
    @staticmethod
    def plot(signal: Signal, title: str = '', x_label: str = 'n'):
        plt.stem(signal.get_range(), signal.get())
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()
