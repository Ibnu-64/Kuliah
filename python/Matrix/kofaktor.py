def minor(matrix, row, col):
    """Menghasilkan submatriks dengan menghilangkan baris 'row' dan kolom 'col'."""
    return [ [matrix[i][j] for j in range(len(matrix)) if j != col] for i in range(len(matrix)) if i != row]

def determinant(matrix):
    """Menghitung determinan matriks menggunakan metode ekspansi kofaktor sepanjang baris pertama."""
    # Jika matriks berukuran 2x2, hitung determinan secara langsung
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Inisialisasi determinan
    det = 0
    print("det(A) = ", end="")

    # Ekspansi kofaktor sepanjang baris pertama
    for col in range(len(matrix)):
        # Tentukan tanda kofaktor
        sign = (-1) ** col
        # Hitung submatriks setelah menghilangkan baris pertama dan kolom ke-col
        submatrix = minor(matrix, 0, col)
        # Hitung determinan dari submatriks
        sub_determinant = determinant(submatrix)
        # Hitung kofaktor
        cofactor = sign * matrix[0][col] * sub_determinant
        # Tambahkan hasil kofaktor ke determinan
        det += cofactor

        # Cetak alur perhitungannya
        if col > 0:
            print(" + ", end="")
        print(f"{matrix[0][col]} * (-1)^{col+1} * det({submatrix}) = {matrix[0][col]} * ({sign}) * {sub_determinant} = {cofactor}", end="")

    print("\n")

    return det

# Matriks yang diberikan
A = [
    [2, 3, 1, 2, 2],
    [1, 3, 5, 3, 4],
    [2, 2, 1, 1, 5],
    [2, 3, 1, 5, 1],
    [1, 4, 2, 2, 1]
]

# Hitung determinan dengan alur perhitungannya
print("Menghitung determinan matriks A:")
det_A = determinant(A)
print(f"Determinan matriks A adalah {det_A}")