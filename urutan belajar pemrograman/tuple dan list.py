# Tuple dan List dalam Python
# ---------------------------

# LIST
data_list = [10, 20, 30, 40]
print("List:", data_list)

# Mengubah elemen list
data_list[2] = 300
print("List setelah diubah:", data_list)

# Menambah elemen list
data_list.append(50)
print("List setelah ditambah:", data_list)

# TUPLE (tidak dapat diubah)
data_tuple = (10, 20, 30, 40)
print("Tuple:", data_tuple)

# Akses elemen tuple
print("Elemen tuple indeks 1:", data_tuple[1])

# Menggabungkan list dan tuple
gabungan = data_list + list(data_tuple)
print("Gabungan list + tuple:", gabungan)
