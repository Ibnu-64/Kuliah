n = 1000000000000
genap = []
ganjil = []
prime = []

# def SieveofEratosthenes(n):
#     primes = [True] * (n + 1) #Anggap semua angka dari 0 hingga n adalah bilangan prima (true)
#     p = 2 # Inisialisasi bilangan prima pertama yang akan digunakan untuk mencoret kelipatan
#     while p**2 <= n: # lakukan perulangan selama quadrat dari p masih di bawah batas yg telah di tentukan (n)
#         # Jika p masih dianggap sebagai bilangan prima
#         if primes[p]:
#             # Coret semua kelipatan dari p (mulai dari p*p hingga n)
#             # Dengan langkah p, tandai sebagai bukan prima (False)
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
                
#         p += 1 #lanjut ke bilangna berikutnya



# prime = [p for p in range(2, n + 1) if primes[p]]
    

# for num in range(1,n + 1):
#     if num % 2 == 0:
#         genap.append(num)
#     else:
#         ganjil.append(num)

#     faktor = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             faktor += 1

#     if faktor == 2: prime.append(num) 





isPrime = [True] * (n+1) #Membuat list boolean

for num in range(1,n+1):
    if num % 2 == 0:
        genap.append(num)
    else:
        ganjil.append(num)
    
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1): # menggunakan akar kuadrat untuk mengurangi jumlah perulangan.
            if  num % i == 0:
                break
        else:
            prime.append(num) 

            
    
            

    
    



print(f"List bilangan genap 1-100 = {genap}" )
print(f"List bilangan ganjil 1-100 = {ganjil}" )
print(f"List bilangan prima 1-100 = {prime}" )
