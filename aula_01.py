from signals.signal_generator import SignalGenerator

unit_impulse = SignalGenerator.unit_impulse()
unit_impulse.plot()

unit_step = SignalGenerator.unit_step(start=0, end=10, fs=2)
print(unit_step.get())
unit_step.plot()

cos = SignalGenerator.cosine()
cos.plot()

expo = SignalGenerator.exponencial_sequence()
expo.plot()
