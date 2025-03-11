#buat program tentang pembelian tiket bioskopsederhana dengan harga berbeda
#DAFTAR_FILM 
film1 = '1 kakak 7 ponakan'
film2 = 'utusan iblis'
film3 = 'bayang-bayang anak jahanam'
film4 = 'sebelum 7 hari'
film5 = 'perayaan mati rasa'
#harga tiket
harga1 = 40.000
harga2 = 45.000
harga3 = 50.000
harga4 = 55.000
harga5 = 60.000
#jika total pembelian tiket lebih dari 100.000 maka akan mendapat diskon 15%
#jika total pembelian tiket lebih dari 250.000 maka akan mendapat diskon 35%
#menampilkan struk pemesanan 
Nama = input('Masukkan Nama Anda : ')
Judul = input('Masukkan Judul Film : ')
Jumlah = input('Masukkan Jumlah Tiket : ')
harga_satuan =input('Masukkan Harga Tiket : ')
total_harga = int(Jumlah) * float(harga_satuan)
potongan_harga = 0
#jika poyongan harga lebih dari 250.000 maka mendapat diskon 35%
#jika poyongan harga lebih dari 100.000 maka mendapat diskon 15%
if total_harga >= 250.000:
    potongan_harga = 0.35
elif total_harga >= 100.000:
    potongan_harga = 0.15
jumlah_potongan = total_harga * potongan_harga
total_setelah_diskon = total_harga - jumlah_potongan
print('=== STRUK PEMESANAN ===')
print('Nama : ', Nama)
print('Judul Film : ', Judul)
print('Jumlah Tiket : ', Jumlah)
print('Harga Satuan : ', harga_satuan)
print('Total Harga : ', total_harga)
print('Potongan Harga : ', potongan_harga)
print('Total yang harus dibayar : ', total_setelah_diskon)
print('=== TERIMA KASIH TELAH MEMESAN TIKET DI BIOSKOP KAMI ===')