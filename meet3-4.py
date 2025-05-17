# Meminta input dari pengguna
panjang = int(input("Masukkan panjang persegi panjang: "))
lebar = int(input("Masukkan lebar persegi panjang: "))

# Mengecek apakah input valid (lebih dari 0)
if panjang > 0 and lebar > 0:

    # Menghitung luas
    luas = panjang * lebar
    print(f"\nLuas persegi panjang adalah: {luas:.2f}\n")

    # Menampilkan bentuk persegi panjang dengan bintang
    print("Gambar persegi panjang:")
    for i in range(lebar):  # lebar = jumlah baris
        print('*' * panjang)  # panjang = jumlah bintang per baris

else:
    print("Panjang dan lebar harus lebih dari 0!")
