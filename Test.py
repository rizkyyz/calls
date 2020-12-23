
print('____________|`Rizky Codekulator`|_______')
print('=======================================')
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y


print('Menu operasi:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian')

operasi = int(input('silahkan masukan operasi pilihan (dalam angka): '))
x = int(input('masukan angka pertama: '))
y = int(input('masukan angka ke dua: '))

if operasi == 1:
    print(tambah(x, y))
elif operasi == 2:
    print(kurang(x, y))
elif operasi == 3:
    print(kali(x, y))
elif operasi == 4:
    print(bagi(x, y))
