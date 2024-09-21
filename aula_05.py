import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt


# X(m) = Sum(x[n]e^(-j*2pi*n*m/N))
def calculate(signal: list, n: int, m: int, N: int):
    '''
    signal: array containing the signal data
    n: signal index
    m: desired frequency
    N: total number of amostration
    '''
    K = 2*np.pi/N
    return signal[n]*np.exp(-1j*K*n*m)


def dft(signal: list) -> dict:
    loop_range = range(len(signal))
    result = []
    for m in loop_range:
        z = []
        for n in loop_range:
            z.append(calculate(signal, n, m, len(signal)))

        result.append(abs(sum(z)))

    return result


def plot(signal, title):
    x = np.linspace(0, 2 * np.pi, len(signal))
    y = signal
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("x (radians)")
    plt.ylabel("sin(x)")

    plt.grid(True)
    plt.show()


Fs = 2000
N = 100
n = np.arange(N)

x1 = 1*np.cos(2*np.pi*60*n/Fs)
x2 = .5*np.cos(2*np.pi*400*n/Fs)
x = x1 + x2

plot(x, 'x')
# plot(x1, 'x1')
# plot(x2, 'x2')
y = dft(x)
# pprint(y)
plot(y, 'y')
