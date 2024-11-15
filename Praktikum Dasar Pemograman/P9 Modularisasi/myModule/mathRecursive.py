def factorial(n):
    """
    Menghitung faktorial dari suatu bilangan. 

    Args:
        n (int): Bilangan yang akan dihitung faktorialnya.

    Returns:
        int: Hasil faktorial dari bilangan n.
    """

    if n == 0: # jika n = 0 maka return 1
        return 1
    else: # jika tidak maka return n * fungsi factorial(n-1)
        return n * factorial(n-1)

# fungsi rekursif adalah fungsi yg memanggil dirinya sendiri dengan parameter yg berbeda. dalam kasus ini fungsi factorial memanggil dirinya sendiri dengan parameter n-1 
# contoh
# factorial(5) = 5 * factorial(4)
# 5 * 4 * factorial(3) 
# 5 * 4 * 3 * factorial(2) 
# 5 * 4 * 3 * 2 * factorial(1) 
# 5 * 4 * 3 * 2 * 1 * factorial(0) => karena n = 0 maka return 1
# 5 * 4 * 3 * 2 * 1 * 1 = 120



def deret_geometri(n, a1, r):
    """Fungsi rekursif untuk menghitung suku ke-n dari deret geometri

    Args:
        n (int): Posisi suku yang ingin dihitung dalam deret geometri (misalnya, suku ke-3, ke-4, dll.)
        a1 (float): Nilai suku pertama (a₁) dari deret geometri.
        r (float): Rasio (r) yang menghubungkan setiap suku dalam deret (rasio antara suku berturut-turut).

    Returns:
        float: Nilai suku ke-n dari deret geometri.
    """
    
    # Basis: Jika n adalah 1, maka kembalikan suku pertama
    if n == 1:
        return a1
    # Rekursif: Suku ke-n adalah suku sebelumnya * rasio (r)
    else:
        return deret_geometri(n - 1, a1, r) * r

    

# penjelasan output:
# deret geometri adalah deret dimana setiap suku adalah hasil kali dari suku sebelumnya dengan rasio tertentu.
# misal n = 4, a1 = 2, r = 3 maka deret geometri nya adalah 2, 6, 18, 54

# jika dalam rekursi prosesusnya seperti ini
# deret_geometri(4, 2, 3) = deret_geometri(3, 2, 3) * 3
# deret_geometri(3, 2, 3) = deret_geometri(2, 2, 3) * 3
# deret_geometri(2, 2, 3) = deret_geometri(1, 2, 3) * 3
# deret_geometri(1, 2, 3) = 2 (basis case tercapai, return 2)
# Sekarang mulai menghitung hasil dari rekursi:
# deret_geometri(1, 2, 3) = 2
# deret_geometri(2, 2, 3) = 2 * 3 = 6
# deret_geometri(3, 2, 3) = 6 * 3 = 18
# deret_geometri(4, 2, 3) = 18 * 3 = 54



def fibonacci(n):
    """Fungsi rekursif untuk menghitung bilangan Fibonacci ke-n.

    Args:
        n (int): Posisi bilangan Fibonacci yang ingin dihitung (misalnya, bilangan ke-3, ke-4, dll.)

    Returns:
        int: Bilangan Fibonacci ke-n.
    """


    # Basis: Jika n adalah 0 atau 1, kembalikan n sebagai hasil langsung
    if n <= 1:
        return n
    # Rekursif: Fibonacci ke-n adalah penjumlahan dua Fibonacci sebelumnya
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Penjelasan output:
# Deret Fibonacci adalah deret di mana setiap suku adalah penjumlahan dari dua suku sebelumnya.
# Misalnya, jika n = 4 maka Fibonacci dari 4 dihitung seperti ini:
# fibonacci(4) = fibonacci(3) + fibonacci(2)
# fibonacci(3) = fibonacci(2) + fibonacci(1)
# fibonacci(2) = fibonacci(1) + fibonacci(0)
# fibonacci(1) = 1 (basis case tercapai, return 1)
# fibonacci(0) = 0 (basis case tercapai, return 0)
# Sekarang mulai menghitung hasil dari rekursi:
# fibonacci(1) = 1
# fibonacci(0) = 0
# fibonacci(2) = 1 + 0 = 1
# fibonacci(3) = 1 + 1 = 2
# fibonacci(4) = 2 + 1 = 3



def isPowerOf(n, exp):

    """Mengecek apakah suatu bilangan adalah hasil dari eksponen tertentu.
    Args:
        n (int) : _bilangan yang akan dicek apakah merupakan hasil dari eksponen tertentu.
        exp (int) : eksponen yang akan digunakan untuk mengecek apakah n adalah hasil dari eksponen tersebut.
    Returns:
        bool: True jika n adalah hasil dari eksponen exp, False jika tidak.

    """


    # Basis: Jika n <= 0, maka return False
    if n <= 0:
        return False
    
    # Basis: Jika n == 1, maka return True
    if n == 1:
        return True
    # Jika n dapat dibagi dengan exp, maka panggil fungsi isPowerOfExponen dengan parameter n / exp dan exp
    if n % exp == 0:
        return isPowerOf(n / exp, exp)
    # Jika n tidak dapat dibagi dengan exp, maka return False
    return False

# Penjelasan output:
# Fungsi isPowerOf digunakan untuk mengecek apakah suatu bilangan n adalah hasil dari eksponen exp.
# Misalnya, jika n = 16 dan exp = 2, maka 16 adalah 2 pangkat 4.
# Jadi, isPowerOf(16, 2) akan mengembalikan True.

# Jika dalam rekursi prosesusnya seperti ini
# isPowerOf(16, 2) = isPowerOf(8, 2)
# isPowerOf(8, 2) = isPowerOf(4, 2)
# isPowerOf(4, 2) = isPowerOf(2, 2)
# isPowerOf(2, 2) = isPowerOf(1, 2)
# isPowerOf(1, 2) = True (basis case tercapai, return True)
# Sekarang mulai menghitung hasil dari rekursi:
# isPowerOf(1, 2) = True
# isPowerOf(2, 2) = True
# isPowerOf(4, 2) = True
# isPowerOf(8, 2) = True