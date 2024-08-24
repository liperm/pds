from signals.signal_generator import SignalGenerator
from signals.plotter import SignalPlotter
from filters.filter import Filter


def main():
    signal = SignalGenerator.unit_step(end=10, step=.5)
    signal.plot()
    filtered_signal = Filter.moving_average(signal, 4)
    SignalPlotter.plot(filtered_signal, range=signal.get_range())


if __name__ == '__main__':
    main()
