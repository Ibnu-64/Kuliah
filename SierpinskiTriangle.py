import matplotlib.pyplot as plt
import numpy as np

# Fungsi rekursif untuk menggambar Sierpinski Triangle
def sierpinski(order, points):
    if order == 0:
        plt.fill(points[:, 0], points[:, 1], 'k')
    else:
        midpoints = (points + np.roll(points, shift=-1, axis=0)) / 2
        sierpinski(order - 1, np.array([points[0], midpoints[0], midpoints[2]]))
        sierpinski(order - 1, np.array([points[1], midpoints[0], midpoints[1]]))
        sierpinski(order - 1, np.array([points[2], midpoints[1], midpoints[2]]))

# Koordinat untuk segitiga awal
points = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])

# Menggambar Sierpinski Triangle
plt.figure(figsize=(6, 6))
sierpinski(5, points)  # Level 5 fractal
plt.axis('off')
plt.show()
