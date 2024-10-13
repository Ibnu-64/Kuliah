import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung Mandelbrot Set
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Membuat grid nilai kompleks
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return n3

# Parameter untuk plotting
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height, max_iter = 800, 800, 256

# Menghitung Mandelbrot Set
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Menampilkan fractal
plt.imshow(mandelbrot_image.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])
plt.colorbar()
plt.show()
