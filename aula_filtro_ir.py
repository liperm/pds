from filters.filter import Filter
from signals.signal import Signal
from signals.signal_generator import SignalGenerator


s = SignalGenerator.from_file('Q2_voz_ruido.pcm', 8000)
# s.plot()
# result: Signal = Filter.low_pass(signal=s, fc=2000, fs=8000)
# result: Signal = Filter.high_pass(signal=s, fc=2000, fs=8000)
# result: Signal = Filter.band_pass(signal=s, fb=500, fc=1000, fs=8000)
result: Signal = Filter.band_reject(signal=s, fb=1000, fc=400, fs=8000)
result.to_audio_file()
