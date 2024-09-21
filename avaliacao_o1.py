import numpy as np
from signals import signal_generator
from filters.filter import Filter
from signals.plotter import SignalPlotter

# questao 01
# x = signal_generator.UnitImpulse()
# y = Filter.echo(x, fs=1, a0=1, a1=0.9, delay=6)
# y.plot()

# questao 02
# a
# x = np.array([1, 1, 0, 0, 0, 0, 0, 0])
# h = np.array([.1, .2, .4, .2, .1, 0, 0, 0])
# y = np.convolve(x, h)
# SignalPlotter.plot(y, np.arange(0, y.size))

# b
x = np.array([1])
h = np.array([.1, .2, .4, .2, .1, 0, 0, 0])
y = np.convolve(x, h)
SignalPlotter.plot(y, np.arange(0, y.size))
