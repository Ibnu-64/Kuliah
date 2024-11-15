import numpy as np
import random

nim = [2,4,1,1,1,0,2,4,4,1,2,6,4]


import random

def createMatrix(data, n=2):
    # Mengacak urutan elemen-elemen di dalam data
    random.shuffle(data)
    
    # Membuat matriks dari elemen-elemen yang sudah diacak
    matrix = []
    for i in range(n):
        # Menambahkan sub-list (baris) ke dalam matriks
        row = data[i * n : (i + 1) * n]  # Memotong bagian dari data untuk setiap baris
        matrix.append(row)
    
    return matrix



def print_matrix(matrix, step):
    """Fungsi untuk mencetak matriks dengan format yang jelas."""
    print(f"Langkah {step}:")
    print(matrix)
    print()  # Baris kosong untuk pemisah

def gauss_jordan_inverse(matrix):
    # Mengubah matrix menjadi array numpy
    A = np.array(matrix, dtype=float)
    
    # Mendapatkan ukuran matriks
    n = A.shape[0]
    
    # Membuat matriks identitas
    I = np.eye(n)
    
    # Menggabungkan matriks A dan I
    augmented_matrix = np.hstack((A, I))
    
    # print_matrix(augmented_matrix, 0)  # Cetak matriks awal

    # Melakukan eliminasi Gauss-Jordan
    for i in range(n):
        # Mencari pivot
        if augmented_matrix[i, i] == 0:
            # Jika pivotnya 0, matriks tidak dapat diinversi
            print("Matriks tidak dapat diinversi.")
            return None
        
        # Membagi baris dengan pivot
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        # print_matrix(augmented_matrix, i + 1)  # Cetak setelah membagi baris
        
        # Menghilangkan elemen di atas dan di bawah pivot
        for j in range(n):
            if j != i:
                augmented_matrix[j] -= augmented_matrix[i] * augmented_matrix[j, i]
        
        # print_matrix(augmented_matrix, i + 1 + n)  # Cetak setelah eliminasi

    # Mengambil matriks invers dari augmented matrix
    inverse_matrix = augmented_matrix[:, n:]
    
    return inverse_matrix

def printMatrix(matrix):
    for row in matrix:
         print(" ".join(f"{num:>5}" for num in row))

# matrix = createMatrix(nim,3)

matrix = [[2, 3, 1,2,2], [1, 3, 5,3,4 ],[2,2, 1,1,5], [2,3,1,5,1], {1,4,2,2,1}]
print("formula:")
printMatrix(matrix)

inverse = gauss_jordan_inverse(matrix)
if inverse is not None:
    print("Matriks invers:")
    print(inverse.round(2))
else:
    print("Matriks tidak dapat diinversi.")