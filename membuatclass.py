class Baju:
    def __init__(self, inputNama, inputHarga, inputWarna):
        self.nama = inputNama
        self.harga = inputHarga
        self.warna = inputWarna

Baju1 = Baju("Distro",100, "Maron")
Baju2 = Baju("Lining",150,"Putih")

print(Baju1.nama, Baju2.nama)