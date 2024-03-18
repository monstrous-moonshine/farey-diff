import numpy as np
import matplotlib.pyplot as plt
from sympy.ntheory import totient
from fractions import Fraction

n = 100
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

s = np.zeros(n + 1, dtype=np.float64)
t = np.zeros(n + 1, dtype=np.int64)
for i in range(1, Fn // 2 + 1):
    a, b = numer[i], denom[i]
    for j in range(b, n + 1):
        t[j] += 1
        s[j] += abs(a/b - t[j]/tot[j])

plt.plot(s)
plt.show()
