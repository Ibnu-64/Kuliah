import math

# A = [[1,8,6],[8,4,7],[9,6,3]]
# B = [[5,8,5],[7,8,7],[3,1,8]]

def penjumlahanVektor(a,b):
    if len(a) != len(b):
        return "tidak dapat menjumlahkan kedua vektor karena kedua element vector tidak sama"
    else:
        output = []
        for i in range(len(a)):
            output.append(a[i] + b[i])     
        return output
   
def penguranganVektor(a,b):
    if len(a) != len(b):
        return "tidak dapat mengurangi kedua vektor karena kedua element vector tidak sama"
    else:
        output = []
        for i in range(len(a)):
            output.append(a[i] - b[i])
        return output

def perkalianSkalar(k,v):
    output = []
    for value in v:
        output.append(k * value)
    return output

def produkTitik(a,b):
    if len(a) != len(b):
        return "tidak dapat menghitung produk titik karena kedua element vector tidak sama"
    else:
        output = 0
        for i in range(len(a)):
            output += a[i] * b[i]
        return output
    
def panjangVektorNorma(v):
    output = 0
    for value in v:
        output += value * value
    return math.sqrt(output)

a= [3,5,1]
b = [2,-3,4]
W = [-1, 0 ,2]
p = [3,4]
a = [4,1,2]
b = [2,0,3]

print(penjumlahanVektor(a,b))
print(perkalianSkalar(3,W))
print(panjangVektorNorma(p))
print(produkTitik(a,b))