from signal_generator import SignalGenerator


def main():
    # impulse = SignalGenerator.unit_impulse(start=-2, end=3)
    # print(impulse.get())
    # impulse.plot()

    # step = SignalGenerator.unit_step()
    # print(step.get())
    # step.plot()

    # cos = SignalGenerator.cosine(duration=5, sampling_rate=30.0, frequency=1.0)
    # print(cos.get())
    # cos.plot()

    expo = SignalGenerator.exponencial_sequence(start=0, end=10, a=-.5, step=1)
    expo.plot()


if __name__ == '__main__':
    main()
