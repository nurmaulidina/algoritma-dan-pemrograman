# Contoh penggunaan dictionary Python
# -----------------------------------

mahasiswa = {
    "nama": "nrmaulidina",
    "nim": "D0425318",
    "jurusan": "sisfo",
    "nilai": 90 # hehe
}

print("Nama:", mahasiswa["nama"])
print("NIM:", mahasiswa["nim"])

# Menambah data
mahasiswa["alamat"] = "pamboang"

# Mengubah data
mahasiswa["nilai"] = 95

# Menghapus data
del mahasiswa["jurusan"]

print("Data mahasiswa:", mahasiswa)
