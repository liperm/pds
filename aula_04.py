import numpy as np

from filters.filter import Filter
from signals.plotter import SignalPlotter
from signals.signal_generator import SignalGenerator


def convolution(signal_1: np.ndarray, signal_2: np.ndarray) -> np.ndarray:
    result = np.convolve(signal_1, signal_2)
    return result


def main():
    signal_1 = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
    signal_2 = np.array([1, .5, .25, .125])
    result = convolution(signal_1, signal_2)
    print(result)
    SignalPlotter.plot(result, np.arange(0, result.size))


if __name__ == '__main__':
    # main()
    s = SignalGenerator.unit_impulse()
    f = Filter.moving_average(s, 8)

    unit_step = SignalGenerator.unit_step(end=3)
    filtered = Filter.moving_average(unit_step, 8)
    print('Filter', filtered.get())
    filtered.plot()

    r = convolution(unit_step.get(), f.get())
    print('Convolution', r)
    SignalPlotter.plot(r, np.arange(0, len(r)))
