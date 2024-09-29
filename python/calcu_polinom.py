import numpy as np


# derajat = int(input("Masukan derajat polinom: "))
# coeffs = []

# for i in range(0, derajat + 1):
#     coeffs.append(int(input("Masukan koefesien dari polinom: ")))
# Membuat polinomial 3x^2 + 2x + 1
# p = np.poly1d(coeffs)
p = np.poly1d([3,273,792])
x = [-3, -1, 0, 1, 3]

# x = int(input("subsitusikan polinom dengan: "))
for value in x:
    print(f"Nilai polinomial untuk x = {value}: {p(value)}")

print("\n")
akar = p.r
print(f"Akar-akar polinomial: {akar}")