#buat program tentang pembelian tiket bioskopsederhana dengan harga berbeda
#DAFTAR_FILM 
film1 = '1 kakak 7 ponakan'
film2 = 'utusan iblis'
film3 = 'azzamine'
film4 = 'sebelum 7 hari'
film5 = 'perayaan mati rasa'
#harga tiket
harga1 = 40000
harga2 = 45000
harga3 = 50000
harga4 = 55000
harga5 = 60000
#menampilkan struk pemesanan 
Nama_pembeli = input('Masukkan Nama Anda : ')
Judul_film = input('Masukkan Judul Film :')
Jumlah_tiket = input('Masukkan Jumlah Tiket : ')
harga_tiket =input('Masukkan Harga Tiket : ')
total_harga = int(Jumlah_tiket) * float(harga_tiket)
diskon = 0
#jika potongan harga lebih dari 250.000 maka mendapat diskon 35%
#jika potongan harga lebih dari 100.000 maka mendapat diskon 15%

if 100000 <= total_harga < 250000:
    diskon = 0.15
elif total_harga >= 250000:
    diskon = 0.35
jumlah_diskon = total_harga * diskon
total_setelah_diskon = total_harga - jumlah_diskon
print('=== STRUK PEMESANAN ===')
print('Nama : ', Nama_pembeli)
print('Judul Film : ', Judul_film)
print('Jumlah Tiket : ', Jumlah_tiket)
print('Harga Satuan : ', harga_tiket)
print('Total Harga : ', total_harga)
print('Potongan Harga : ', diskon)
print('Jumlah Potongan : ', jumlah_diskon)
print('Total yang harus dibayar : ', total_setelah_diskon)
print('=== TERIMA KASIH TELAH MEMESAN TIKET DI BIOSKOP KAMI ===')
