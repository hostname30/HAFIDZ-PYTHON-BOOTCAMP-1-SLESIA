import random

def tebak_angka():
    print("=== SELAMAT DATANG DI GAME TEBAK ANGKA ===")
    print("Saya telah memilih angka antara 1 sampai 100. Coba tebak!")
    
    # 1. Komputer memilih angka acak dari 1 sampai 100
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    percobaan = 0
    
    # 2. Perulangan akan terus berjalan selama tebakan belum benar
    while tebakan != angka_rahasia:
        try:
            # Meminta input dari pengguna
            tebakan = int(input("Masukkan tebakan Anda: "))
            percobaan += 1
            
            # 3. Pengkondisian untuk memeriksa tebakan
            if tebakan < angka_rahasia:
                print("Terlalu kecil! Coba angka yang lebih besar.")
            elif tebakan > angka_rahasia:
                print("Terlalu besar! Coba angka yang lebih kecil.")
            else:
                print(f"Luar biasa! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} kali percobaan.")
                
        except ValueError:
            # Penanganan error jika pengguna memasukkan selain angka
            print("Mohon masukkan angka bulat yang valid!")

# Menjalankan fungsi utama
if __name__ == "__main__":
    tebak_angka()