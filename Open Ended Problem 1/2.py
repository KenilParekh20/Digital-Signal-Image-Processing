import matplotlib.pyplot as plt

n = [0, 1, 2, 3, 4, 5]
x = [1, 2, 3, 3, 2, 1]

plt.stem(n, x)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Staircase Signal")
plt.grid(True)
plt.show()