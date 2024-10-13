import random
import matplotlib.pyplot as plt

# Koordinat awal
x, y = 0, 0
points = []

# Fungsi untuk iterasi Barnsley Fern
def barnsley_fern(n):
    global x, y
    for _ in range(n):
        r = random.random()
        if r < 0.01:
            x, y = 0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        points.append((x, y))

# Iterasi Barnsley Fern
barnsley_fern(100000)

# Plotting
x_vals, y_vals = zip(*points)
plt.scatter(x_vals, y_vals, s=0.2, color='green')
plt.axis('equal')
plt.show()
