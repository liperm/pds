from signals.signal import Signal
from signals.unit_impulse import UnitImpulse
from signals.unit_step import UnitStep
from signals.cos import Cosine
from signals.exponencial_sequence import ExponencialSequence


class SignalGenerator:
    @staticmethod
    def unit_impulse(
            gain: float = 1.0,
            offset: int = 0,
            start: int = 0,
            end: int = 1,
            step: int = 1) -> Signal:

        return UnitImpulse(
            gain=gain, offset=offset, start=start, end=end, step=step)

    @staticmethod
    def unit_step(
            gain: float = 1.0,
            offset: int = 0,
            start: int = 0,
            end: int = 1,
            step: float = 1.0) -> Signal:

        return UnitStep(
            gain=gain, offset=offset, start=start, end=end, step=step)

    @staticmethod
    def cosine(
            frequency: float = 1.0,
            sampling_rate: int = 10,
            duration: float = 1.0,
            gain: float = 1.0,) -> Signal:
        '''
            frequency (float): the cosine frequency (Hz)\n
            sampling_rate (int): the number of samples taken by second\n
            duration (float): duration of the wave (s)\n
            gain (float): the total amplitude
        '''

        return Cosine(
            gain=gain,
            duration=duration,
            frequency=frequency,
            sampling_rate=sampling_rate)

    @staticmethod
    def exponencial_sequence(
            step: float = 1.0,
            start: int = 0,
            end: int = 1,
            gain: float = 1.0,
            a: float = 1.0) -> Signal:

        return ExponencialSequence(
            gain=gain, a=a, start=start, end=end, step=step)
