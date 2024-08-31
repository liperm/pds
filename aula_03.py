from signals.signal_generator import SignalGenerator
from signals.plotter import SignalPlotter
from filters.filter import Filter


def main():
    delay()
    echo()


def delay():
    # signal = SignalGenerator.unit_impulse(fs=8000)
    # filtered_signal = Filter.delay(
    #     signal=signal,
    #     a0=.5, a1=.3, a2=.2, delay1=(10/1000), delay2=(15/1000), fs=8000)
    # SignalPlotter.plot(filtered_signal.get(), range=signal.get_range())

    signal = SignalGenerator.from_file('./teste.pcm', 8000)
    filtered_signal = Filter.delay(
        signal=signal,
        a0=.5, a1=.3, a2=.2, delay1=(200/1000), delay2=(200/1000), fs=8000)
    filtered_signal.to_audio_file('result_delay.pcm')


def echo():
    # signal = SignalGenerator.unit_impulse(fs=8000)
    # filtered_signal = Filter.echo(
    #     signal=signal,
    #     a0=1.0, a1=.5, delay=1/10, fs=8000)
    # SignalPlotter.plot(filtered_signal, range=signal.get_range())

    signal = SignalGenerator.from_file(file_path='./teste.pcm', fs=8000)
    filtered_signal = Filter.echo(
        signal=signal,
        a0=.5, a1=.3, delay=200/1000, fs=8000)
    filtered_signal.to_audio_file('result_echo.pcm')



if __name__ == '__main__':
    main()
