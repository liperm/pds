import numpy as np
from signals.signal import Signal


class Filter():
    @staticmethod
    def moving_average(signal: Signal, k: int) -> Signal:
        signal_array = signal.get()
        signal_array = np.append(signal_array, np.zeros(k, dtype=np.float64))
        result = np.zeros_like(signal_array, dtype=np.float64)

        for n in range(len(signal_array)):
            sum = 0.0
            for i in range(k):
                sum += signal_array[n-i] if n - i >= 0 else 0

            avg = sum/float(k)
            result[n] = avg

        return Signal(result, signal.get_sample_frequency())

    @staticmethod
    def delay(
            signal: Signal,
            fs: int,
            a0: float,
            a1: float,
            a2: float,
            delay1: float,
            delay2: float) -> Signal:
        '''
            a0, a1 (float): coeficient of the nth sample
            delay1, delay2 (int): delay in seconds
            fs (float): amostration rate in samples per second
        '''
        signal_array = signal.get()
        signal_array = np.append(signal_array, np.zeros(20, dtype=np.float64))
        result = np.zeros_like(signal_array, dtype=np.float64)
        n1 = int(fs*delay1)
        n2 = int(fs*delay2)

        for n in range(len(signal_array)):
            i = signal_array[n-n1] if n-n1 >= 0 else 0.0
            j = signal_array[n-n2] if n-n2 >= 0 else 0.0
            result[n] = (
                a0*signal_array[n]
                + a1*i
                + a2*j
            )

        return Signal(result, signal.get_sample_frequency())

    @staticmethod
    def echo(
            signal: Signal,
            fs: int,
            a0: float,
            a1: float,
            delay: int):
        signal_array = signal.get()
        signal_array = np.append(signal_array, np.zeros(24, dtype=np.float64))
        result = np.zeros_like(signal_array, dtype=np.float64)
        d = int(fs*delay)

        for n in range(len(signal_array)):
            s = signal_array[n]
            r = result[n-d] if n-d >= 0 else 0
            result[n] = a0*s + a1*r

        return Signal(samples=result, fs=signal.get_sample_frequency())

    @staticmethod
    def low_pass(
        signal: Signal,
        fc: int,
        fs: int
    ):
        k = np.tan(np.pi * fc / fs)
        b0 = (k**2) / (1 + np.sqrt(2) * k + k**2)
        b1 = 2 * b0
        b2 = b0
        a1 = (2 * (k**2 - 1)) / (1 + np.sqrt(2) * k + k**2)
        a2 = (1 - np.sqrt(2) * k + k**2) / (1 + np.sqrt(2) * k + k**2)

        signal_array = signal.get()
        result = np.zeros_like(signal_array, dtype=np.float64)
        x = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        y = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        for n in range(len(signal_array)):
            x[0] = signal_array[n]

            result[n] = np.clip(
                b0 * x[0] + b1*x[1] + b2*x[2] - a1*y[1] - a2*y[2],
                -32768, 32767
            )
            x = np.roll(x, shift=1)
            y = np.roll(y, shift=1)
            y[0] = result[n]

        return Signal(samples=result, fs=fs)

    @staticmethod
    def high_pass(
        signal: Signal,
        fc: int,
        fs: int
    ):
        k = np.tan(np.pi * fc / fs)
        b0 = (1) / (1 + np.sqrt(2) * k + k**2)
        b1 = -2 / (1 + np.sqrt(2) * k + k**2)
        b2 = b0
        a1 = (2 * (k**2 - 1)) / (1 + np.sqrt(2) * k + k**2)
        a2 = (1 - np.sqrt(2) * k + k**2) / (1 + np.sqrt(2) * k + k**2)

        signal_array = signal.get()
        result = np.zeros_like(signal_array, dtype=np.float64)
        x = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        y = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        for n in range(len(signal_array)):
            x[0] = signal_array[n]

            result[n] = np.clip(
                b0 * x[0] + b1*x[1] + b2*x[2] - a1*y[1] - a2*y[2],
                -32768, 32767
            )
            x = np.roll(x, shift=1)
            y = np.roll(y, shift=1)
            y[0] = result[n]

        return Signal(samples=result, fs=fs)

    @staticmethod
    def band_pass(
        signal: Signal,
        fb: int,
        fc: int,
        fs: int
    ):
        c = (np.tan(np.pi*(fb/fs)) - 1) / (np.tan(2*np.pi*(fb/fs)) + 1)
        d = -np.cos(2*np.pi*(fc/fs) + 1)

        b0 = 1/2 * (1 + c)
        b1 = 0
        b2 = 1/2 * (-c - 1)
        a1 = d * (1 - c)
        a2 = -c

        signal_array = signal.get()
        signal_array = np.append(signal_array, np.zeros(2, dtype=np.float64))
        result = np.zeros_like(signal_array, dtype=np.float64)
        x = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        y = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        for n in range(len(signal_array)):
            x[0] = signal_array[n]

            result[n] = np.clip(
                b0 * x[0] + b1*x[1] + b2*x[2] - a1*y[1] - a2*y[2],
                -32768, 32767
            )
            x = np.roll(x, shift=1)
            y = np.roll(y, shift=1)
            y[0] = result[n]

        return Signal(samples=result, fs=fs)

    @staticmethod
    def band_reject(
        signal: Signal,
        fb: int,
        fc: int,
        fs: int
    ):
        c = (np.tan(np.pi*(fb/fs)) - 1) / (np.tan(2*np.pi*(fb/fs)) + 1)
        d = -np.cos(2*np.pi*(fc/fs))
        b0 = (1/2) * (1 - c)
        b1 = d * (1 - c)
        b2 = (1/2) * (1 - c)
        a1 = d * (1 - c)
        a2 = -c

        signal_array = signal.get()
        result = np.zeros_like(signal_array, dtype=np.float64)
        x = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        y = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        for n in range(len(signal_array)):
            x[0] = signal_array[n]

            result[n] = np.clip(
                b0 * x[0] + b1*x[1] + b2*x[2] - a1*y[1] - a2*y[2],
                -32768, 32767
            )
            x = np.roll(x, shift=1)
            y = np.roll(y, shift=1)
            y[0] = result[n]

        return Signal(samples=result, fs=fs)
