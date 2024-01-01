# Nama : Dyah Prameswari Cinta Herlianti
# NPM  : 5220411312
# Matakuliah : Pemograman Berorientasi Objek Praktik

import os 
os.system('cls')

class Pertanian:
    def __init__(self,Penanam,Produksi):
        self.penanam = Penanam
        self.produksi = Produksi

    def pertanian(self): 
        print ("Nama Petani : ", self.penanam, "Produksi Pertanian : ", self.produksi)

    def pertanian(self,Katagori = None, Hasil_Pertanian = None):
        if Katagori != None : 
            katagori = Katagori
            harga = Hasil_Pertanian
            print("Nama Petani : ", self.penanam)
            print("Produksi Pertanian : ",self.produksi)
            print("Katagori Pertanian : ",katagori)
            print("Total Harga Panen : ",harga)
            print("Panen Sudah dibayar lunas")
        else: 
            katagori = Katagori
            harga = Hasil_Pertanian
            print("Nama Petani : ", self.penanam)
            print("Produksi Pertanian : ",self.produksi)
            print("Katagori Pertanian : ",katagori)
            print("Total Harga Panen : ",harga)
            print("Panen belum dibayar lunas")
            
class Pertanian_Basah(Pertanian):
    def __init__(self,Waktu_PanenPertanianBasah):
        super().__init__("Cinta", "Padi/beras")
        self.panen = Waktu_PanenPertanianBasah

    def pertanian(self):
        print(" Waktu Panen : ", self.panen)
           
class Perkebunan(Pertanian): 
    def __init__(self,Waktu_PanenPerkebunan):
        super().__init__("Cinta", "Sayur/Buah")
        self.panen1 = Waktu_PanenPerkebunan

    def pertanian(self):
        print(" Waktu Panen : ", self.panen1)

class Sayur(Perkebunan):
    def __init__(self,Jenis_Sayur):
        super().__init__(Jenis_Sayur)
        self.sayur = Jenis_Sayur
    
    def pertanian(self):
        print("Jenis Sayur : ",self.sayur)




print("~~~~~~~~~~~~~~~ Inputan Data Pertanian ~~~~~~~~~~~~~~~ ")
print()
tanaman01 = Pertanian("Cinta", "Padi/Beras")
tanaman01.pertanian("Pertanian Basah", "5 Juta Rupiah")
sawah = Pertanian_Basah("2 bulan")
sawah.pertanian()
print("-------------------------------------------------------")
tanaman02 = Pertanian("Cinta", "Sayur/Buah")
sayur =  Sayur("Sayur Bayam")
tanaman02.pertanian("Perkebunan", "3 Juta Rupiah")
perkebunan = Perkebunan ("2 bulan")
perkebunan.pertanian()
sayur.pertanian()

