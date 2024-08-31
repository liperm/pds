from signals.signal_generator import SignalGenerator
from filters.filter import Filter
from signals.plotter import SignalPlotter

# signal = SignalGenerator.unit_step()
# signal.plot()
# filtered = Filter.moving_average(signal=signal, k=4)
# signal.plot()
# print(signal.get())
# SignalPlotter.plot(filtered.get(), signal.get_range())

signal = SignalGenerator.from_file('./sweep_20_2000.wav', 8000)
filtered = Filter.moving_average(signal=signal, k=128)
filtered.to_audio_file()
