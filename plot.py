import numpy as np
import matplotlib.pyplot as plt
import sys

a = np.array([[float(s) for s in line.split()] for line in sys.stdin])
fig, ax = plt.subplots()
ax.plot(a[:, 0], a[:, 1])
plt.show()
