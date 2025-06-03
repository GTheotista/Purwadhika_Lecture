# Daftar atau List di Python

# List adalah kumpulan data yang terurut. Dalam list, kita bisa menyimpan berbagai jenis data, seperti angka, string, atau boolean.
my_list = ['satu', 2, 2, 4, False, True]

# Mengakses elemen dalam list dengan index positif
print(my_list[0])  # Output: 'satu'
print(my_list[3])  # Output: 4

# Mengakses elemen dalam list dengan index negatif
print(my_list[-1])  # Output: True

# Slicing: Mengambil sebagian elemen dari list
print(my_list[2:5])  # Output: [2, 4, False] (mulai dari index 2 sampai sebelum index 5)
print(my_list[-3:])  # Output: [4, False, True] (mulai dari index -3 sampai akhir)
print(my_list[3:])   # Output: [4, False, True] (mulai dari index 3 sampai akhir)
print(my_list[:-5])  # Output: ['satu'] (dari awal sampai sebelum index -5)
print(my_list[:4])   # Output: ['satu', 2, 2, 4] (dari awal sampai sebelum index 4)

# Menambahkan elemen ke dalam list
# append() menambahkan elemen di akhir list
my_list.append('dua')
print(my_list)  # Output: ['satu', 2, 2, 4, False, True, 'dua']

# insert() menambahkan elemen pada posisi tertentu dalam list
my_list.insert(1, 'tiga')
print(my_list)  # Output: ['satu', 'tiga', 2, 2, 4, False, True, 'dua']

# remove() menghapus elemen berdasarkan nilai yang kita tentukan 
# tapi tidak remove duplikasi
# me remove kita value kita tentukan dengan index paling terkecil
my_list = ['satu', 2, 2, 4, False, True]
my_list.remove(2)
print(my_list)  # Output: ['satu', 2, 2, 4, False, True, 'dua']

# pop() menghapus elemen terakhir dari list
my_list.pop()
print(my_list)  # Output: ['satu', 2, 2, 4, False, True]

# del digunakan untuk menghapus elemen berdasarkan index
del my_list[0]
print(my_list)  # Output: [2, 2, 4, False, True]

# clear() menghapus semua elemen dalam list
my_list.clear()
print(my_list)  # Output: []

# Mengembalikan list ke kondisi semula
my_list = ['satu', 2, 2, 4, False, True]

# Menampilkan semua elemen dalam list menggunakan loop
for item in my_list:
    print(item)

# Mengecek apakah elemen tertentu ada dalam list menggunakan 'in'
if 2 in my_list:
    print("ada string 'satu' di list")  # Output: ada string 'satu' di list
else:
    print("Masuk condition dalam list")

# Mengetahui jumlah elemen dalam list dengan len()
print(len(my_list))  # Output: 6

# copy() digunakan untuk menyalin list. List baru yang disalin tidak mempengaruhi list asli
new_list_2 = my_list.copy()
new_list_2.clear()
print(new_list_2)  # Output: []
print(my_list)     # Output: ['satu', 2, 2, 4, False, True]

# Tanpa menggunakan copy(), list yang disalin akan saling mempengaruhi
new_list_2 = my_list
new_list_2.clear()
print(new_list_2)  # Output: []
print(my_list)     # Output: []

# Menggabungkan dua list dengan cara mencantumkan satu per satu
list_satu = ['string', 'abu', 'putih']
list_dua = [2, 1, 3]
list_tiga = [1.0, 2.2, 3.3]

list_gabungan = list_satu + list_tiga + list_dua
print(list_gabungan)  # Output: ['string', 'abu', 'putih', 1.0, 2.2, 3.3, 2, 1, 3]

# extend() menambahkan elemen dari list lain ke list yang sudah ada
# kayak append() dia ada paling ujung
list_satu.extend(list_dua)
print(list_satu)  # Output: ['string', 'abu', 'putih', 2, 1, 3]

# Sorting (Urutkan) list. Sorting hanya bisa dilakukan pada list dengan tipe data yang sama
list_dua = [2, 1, 3]
list_dua.sort()  # Mengurutkan angka dari terkecil ke terbesar
print(list_dua)  # Output: [1, 2, 3]

# reverse() membalikkan urutan elemen dalam list
list_dua.reverse()  # Membalikkan urutan list
print(list_dua)     # Output: [3, 2, 1]

# Operasi aritmetika dengan list
# Kita bisa mengalikan list dengan angka untuk menggandakan elemen-elemen dalam list
list_1 = [2, 2, 2]
var_multiple_list = list_1 * 3  # Menggandakan list sebanyak 3 kali
print(var_multiple_list)  # Output: [2, 2, 2, 2, 2, 2]
