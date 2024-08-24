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

    @staticmethod
    def delay(
            signal: Signal,
            fs: int,
            a0: float,
            a1: float,
            a2: float,
            delay1: float,
            delay2: float):
        '''
            a0, a1 (float): coeficient of the nth sample
            delay1, delay2 (int): delay in seconds
            fs (float): amostration rate in samples per second
        '''
        signal_array = signal.get()
        result = np.zeros_like(signal.get_range(), dtype=np.float64)
        n1 = int(fs*delay1)
        n2 = int(fs*delay2)

        for n in range(len(signal_array)):
            i = n-n1 if n-n1 >= 0 else 0
            j = n-n2 if n-n2 >= 0 else 0

            result[n] = (
                a0*signal_array[n]
                + a1*signal_array[i]
                + a2*signal_array[j]
            )

        return result

    @staticmethod
    def echo(
            signal: Signal,
            fs: int,
            a0: float,
            a1: float,
            delay: int):
        signal_array = signal.get()
        result = np.zeros_like(signal.get_range(), dtype=np.float64)
        d = int(fs*delay)

        for n in range(len(signal_array)):
            i = n-d if n-d >= 0 else 0
            result[n] = a0*signal_array[n] + a1*result[i]

        return result
