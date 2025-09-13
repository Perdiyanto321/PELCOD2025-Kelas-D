print("-"*20)
print("MENGHITUNG HARGA TOTAL")
print("-"*20)
pensil = 2000
buku = 5000

jumlah_pensil = int(input("masukkan jumlah pensil "))
jumlah_buku = int(input("masukkan jumlah buku "))

total_pensil = pensil*jumlah_pensil
total_buku = buku*jumlah_buku
total_semua = total_pensil+total_buku

print("total harga harga pensil: ",total_pensil, "total harga buku : ", total_buku)
print("total semua barang ", total_semua)