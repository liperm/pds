from signals.signal_generator import SignalGenerator
from filters.filter import Filter
from signals.plotter import SignalPlotter

signal = SignalGenerator.unit_step()
signal.plot()
filtered = Filter.moving_average()
SignalPlotter.plot(filtered, signal.get_range())
