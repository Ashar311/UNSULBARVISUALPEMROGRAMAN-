print ("Nama = Ashar ")
print( "Nim = D0219311")
def tambah(x, y):
   return x + y
def kurang(x, y):
   return x - y
def kali(x, y):
   return x * y
def bagi(x, y):
   return x / y
print("Pilih Operasi.")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

choice = input("silahkan pilih(1/2/3/4): ")
bil1 = int(input("Masukkan angka pertama: "))
bil2 = int(input("Masukkan angka kedua: "))
if choice == '1':
   print(bil1,"+",bil2,"=", tambah(bil1,bil2))
elif choice == '2':
   print(bil1,"-",bil2,"=", kurang(bil1,bil2))
elif choice == '3':
   print(bil1,"*",bil2,"=", kali(bil1,bil2))
elif choice == '4':
   print(bil1,"/",bil2,"=", bagi(bil1,bil2))
else:
   print("Input salah")