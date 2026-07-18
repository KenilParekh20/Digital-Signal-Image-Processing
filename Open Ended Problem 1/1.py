import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-3, 7)

x = [2, 3, 2, 1, 2, 3, 2, 3, 2, 3]

plt.stem(n, x)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Discrete Time Signal")
plt.grid(True)
plt.show()