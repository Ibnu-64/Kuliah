# Ibnu Shabill Al Zahari_2411102441264

def penjumlahanVektor(v1,v2):
    if len(v1) != len(v2):
        return "tidak dapat menjumlahkan kedua vektor karena kedua panjang element vector tidak sama"
    else:
        output = []

        for i in range(len(v1)):
            output.append(v1[i] + v2[i])
            
        return output
    
def penguranganVektor(v1,v2):
    if len(v1) != len(v2):
        return "tidak dapat mengurangi kedua vektor karena kedua panjang vector tidak sama"
    else:
        output = []

        for i in range(len(v1)):
            output.append(v1[i] - v2[i])
            
        return output

V1= [3,5,1]
V2 = [2,-3,4]

hasil_penjumlahan_kedua_vektor = penjumlahanVektor(V1, V2) 
hasil_pengurangan_kedua_vektor = penguranganVektor(V1,V2) 

print(V1, " + ", V2, " = ", hasil_penjumlahan_kedua_vektor)
print(V1, " - ", V2, " = ", hasil_pengurangan_kedua_vektor)