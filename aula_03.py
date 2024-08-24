from signals.signal_generator import SignalGenerator
from signals.plotter import SignalPlotter
from filters.filter import Filter


def main():
    echo()


def delay():
    signal = SignalGenerator.unit_impulse(fs=8000)
    filtered_signal = Filter.delay(
        signal=signal,
        a0=.5, a1=.3, a2=.2, delay1=(10/1000), delay2=(15/1000), fs=8000)
    SignalPlotter.plot(filtered_signal, range=signal.get_range())


def echo():
    signal = SignalGenerator.unit_impulse(fs=80)
    filtered_signal = Filter.echo(
        signal=signal,
        a0=1.0, a1=.5, delay=1/10, fs=80)
    SignalPlotter.plot(filtered_signal, range=signal.get_range())


if __name__ == '__main__':
    main()
