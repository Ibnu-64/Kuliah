import numpy as np
import matplotlib.pyplot as plt

# Membuat polinomial p(x) = x^3 - 6x^2 + 9x
def p(x):
    return x**3 - 6*x**2 + 9*x

# Turunan kedua dari polinomial: p''(x) = 6x - 12
def second_derivative(x):
    return 6*x - 12

# Nilai x dari -2 hingga 5
x = np.linspace(-2, 5, 400)
y = p(x)
y_prime2 = second_derivative(x)

# Plot grafik polinomial
plt.plot(x, y, label="p(x) = x^3 - 6x^2 + 9x", color="blue")

# Menambahkan garis titik belok
plt.axvline(x=2, color="green", linestyle="--", label="Titik belok (x=2)")

# Mengarsir kecekungan
plt.fill_between(x, y, where=(y_prime2 > 0), color='orange', alpha=0.3, label='Cekung ke atas')
plt.fill_between(x, y, where=(y_prime2 < 0), color='red', alpha=0.3, label='Cekung ke bawah')

# Memberi label
plt.title("Grafik Polinomial dan Kecekungan")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.legend()

# Menampilkan grafik
plt.grid(True)
plt.show()
