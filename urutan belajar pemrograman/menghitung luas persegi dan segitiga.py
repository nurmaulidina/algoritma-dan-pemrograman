# Menghitung Luas Persegi dan Segitiga
# ------------------------------------

def luas_persegi(sisi):
    return sisi * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


# Contoh penggunaan
print("=== Menghitung Luas Bangun Datar ===")

# Luas Persegi
sisi = float(input("Masukkan sisi persegi: "))
print("Luas Persegi =", luas_persegi(sisi))

# Luas Segitiga
alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
print("Luas Segitiga =", luas_segitiga(alas, tinggi))
