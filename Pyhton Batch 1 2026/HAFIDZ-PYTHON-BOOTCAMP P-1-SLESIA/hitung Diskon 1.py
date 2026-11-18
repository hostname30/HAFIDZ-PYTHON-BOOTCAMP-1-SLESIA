# Masukkan total harga belanjaan awal
total_harga = int(input("Masukkan total harga belanjaan: Rp "))

# Masukkan besar diskon dalam persen (misal: 10 untuk 10%)
diskon_persen = int(input("Masukkan persentase diskon (%): "))

# Hitung jumlah diskon dan harga akhir
besar_diskon = total_harga * (diskon_persen / 100)
harga_akhir = total_harga - besar_diskon

# Tampilkan hasil
print("--- RINCIAN PEMBAYARAN ---")
print("Total Harga Asli : Rp", total_harga)
print("Besar Diskon     : Rp", int(besar_diskon))
print("Harga Setelah Diskon : Rp", int(harga_akhir))\