import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from sympy.ntheory import totient

def farey_seq(n):
    tot = np.cumsum(np.array([0] + [totient(k) for k in range(1, n+1)]))
    Fn = tot[-1]

    numer = np.zeros(1 + Fn // 2, dtype=np.int64)
    denom = np.zeros(1 + Fn // 2, dtype=np.int64)
    numer[0], denom[0] = 0, 1
    numer[1], denom[1] = 1, n
    for k in range(2, Fn // 2 + 1):
        a, b = numer[k - 2], denom[k - 2]
        c, d = numer[k - 1], denom[k - 1]
        m = (n + b) // d
        numer[k] = m * c - a
        denom[k] = m * d - b
    return numer, denom


def farey_diff(n):
    numer, denom = farey_seq(n)
    s = np.zeros(n + 1, dtype=np.float64)
    t = np.zeros(n + 1, dtype=np.int64)
    for i in range(1, Fn // 2 + 1):
        a, b = numer[i], denom[i]
        for j in range(b, n + 1):
            t[j] += 1
            s[j] += abs(a/b - t[j]/tot[j])
    return s


def ticks_plot(n):
    numer, denom = farey_seq(n)
    fig = plt.figure(figsize=(8, 1))
    y = 0.4
    dy = 0.15
    y_text=0.7
    xmin, xmax = 0.03, 0.97
    for a, b in zip(numer, denom):
        x = xmin + (xmax - xmin) * a/b
        fig.add_artist(lines.Line2D([x, x], [y, y + dy]))
        t1 = '$\\frac{' + str(a) + '}{' + str(b) + '}$'
        fig.text(x, y_text, t1, fontsize='x-large', ha='center', math_fontfamily='cm')
    for a, b in zip(numer[:-1], denom[:-1]):
        x = xmin + (xmax - xmin) * (1-a/b)
        fig.add_artist(lines.Line2D([x, x], [y, y + dy]))
        t2 = '$\\frac{' + str(b-a) + '}{' + str(b) + '}$'
        fig.text(x, y_text, t2, fontsize='x-large', ha='center', math_fontfamily='cm')
    Fn = 2 * (len(numer) - 1)
    for k in range(Fn + 1):
        x = xmin + (xmax - xmin) * k/Fn
        fig.add_artist(lines.Line2D([x, x], [y, y - dy], color='#ff7f0e'))
    fig.add_artist(lines.Line2D([xmin, xmax], [y, y]))
    plt.show()


def error_plot(n):
    numer, denom = farey_seq(n)
    Fn = 2 * (len(numer) - 1)
    x = np.linspace(0, 1, Fn + 1)
    y = ([a/b for a, b in zip(numer, denom)] +
         [1-a/b for a, b in zip(numer[-2::-1], denom[-2::-1])])
    xx = np.vstack((x, x))
    yy = np.vstack((x, y))
    fig, ax = plt.subplots()
    ax.plot(xx, yy, color='#1f77b4', marker='o', markerfacecolor='white')
    plt.show()


if __name__ == "__main__":
    ticks_plot(7)
