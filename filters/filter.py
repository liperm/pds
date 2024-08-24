import numpy as np
from signals.signal import Signal


class Filter():
    @staticmethod
    def moving_average(signal: Signal, k: int) -> np.ndarray:
        signal_array = signal.get()
        result = np.zeros_like(signal.get_range(), dtype=np.float64)

        for n in range(len(signal_array)):
            sum = 0.0
            for i in range(k):
                sum += signal_array[n-i] if n - i >= 0 else 0.0

            avg = sum/float(k)
            result[n] = avg

        return result
