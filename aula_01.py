from signals.signal_generator import SignalGenerator

unit_impulse = SignalGenerator.unit_impulse()
unit_impulse.plot()

unit_step = SignalGenerator.unit_step()
unit_step.plot()

cos = SignalGenerator.cosine()
cos.plot()

expo = SignalGenerator.exponencial_sequence()
expo.plot()
