print("----------------- Andikskuy Store -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 
def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Seblak Banyumas - Rp 15000")
   print("2. nasi bebek madura - Rp 9000")
   print("3. sate kelinci - Rp 11000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng Gila = Rp", totalmkn)
       mkn=("Seblak Banyumas")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," porsi Seblak Mercon Kadal = Rp", totalmkn)
       mkn=("nasi bebek madura")
   elif nomor==3:
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("sate kelinci")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 2000")
   print("2. Es leci - Rp 3500")
   print("3. Es teler - Rp 4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*2000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es leci")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es teler")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== TERIMA KASIH ATAS KUNJUNGAN NYA  =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("Terima Kasih atas kunjungan")
print("Perumahan Bumi Mutiara Blok JE 12 NO 05")