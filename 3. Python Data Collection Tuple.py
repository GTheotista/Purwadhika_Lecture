# Tuple di Python

# Tuple adalah tipe data yang mirip dengan list, tetapi perbedaannya adalah tuple bersifat **immutable** (tidak bisa diubah setelah dibuat).
my_tuple = ('satu', 2, 2, 4, False, True)

# Mengakses elemen dalam tuple dengan index positif
print(my_tuple[0])  # Output: 'satu'
print(my_tuple[3])  # Output: 4

# Mengakses elemen dalam tuple dengan index negatif
print(my_tuple[-1])  # Output: True

# Slicing: Mengambil sebagian elemen dari tuple
print(my_tuple[2:5])  # Output: (2, 4, False) (mulai dari index 2 sampai sebelum index 5)
print(my_tuple[-3:])  # Output: (4, False, True) (mulai dari index -3 sampai akhir)
print(my_tuple[3:])   # Output: (4, False, True) (mulai dari index 3 sampai akhir)
print(my_tuple[:-5])  # Output: ('satu') (dari awal sampai sebelum index -5)
print(my_tuple[:4])   # Output: ('satu', 2, 2, 4) (dari awal sampai sebelum index 4)

# Kesimpulan untuk akses data pada tuple mirip dengan list.

# Perbedaan dengan List
# 1. Tidak bisa mengubah elemen tuple secara langsung
# Jika mencoba mengubah elemen tuple seperti berikut:
# my_tuple[0] = 70  # Akan muncul error: "TypeError: 'tuple' object does not support item assignment"

# Jika tetap ingin mengubah, kita bisa mengubah tuple menjadi list terlebih dahulu, lalu kembali ke tuple setelah dimodifikasi:
my_tuple = list(my_tuple)  # Mengubah tuple menjadi list
my_tuple[0] = 70  # Mengubah elemen
my_tuple = tuple(my_tuple)  # Mengubah kembali menjadi tuple
print(my_tuple)  # Output: (70, 2, 2, 4, False, True)

# Tuple juga dapat di-loop seperti list
for i in my_tuple:
    print(i)  # Output: 70, 2, 2, 4, False, True

# Kondisi dengan 'in' juga sama seperti list
if 70 in my_tuple:
    print('Ada int 70')  # Output: Ada int 70
else:
    print('Masuk ke kondisi else')

# Menggunakan len() untuk mengetahui jumlah elemen dalam tuple
print(len(my_tuple))  # Output: 6

# 2. Perbedaan lainnya: tuple yang terdiri dari satu elemen harus menggunakan koma
# Contoh 1: Tuple dengan satu elemen
my_tuple = ('Hello',)  # Koma wajib agar dianggap sebagai tuple
print(type(my_tuple))  # Output: <class 'tuple'>

my_tuple = ('Hello')  # Tanpa koma, dianggap sebagai string
print(type(my_tuple))  # Output: <class 'str'>

# List tidak membutuhkan koma walaupun hanya ada satu elemen
my_list = ['Hello']
print(type(my_list))  # Output: <class 'list'>

# Menggabungkan tuple dengan operator '+'
my_tuple_1 = (1, 8, 9, 19)
my_tuple_2 = ('satu', 'delapan', 'bulan')

# Tuple dapat digabungkan menggunakan operator '+'
gabungan_tuple = my_tuple_1 + my_tuple_2
print(gabungan_tuple)  # Output: (1, 8, 9, 19, 'satu', 'delapan', 'bulan')

# Tuple tidak memiliki method append() seperti list, jadi penggabungan hanya bisa menggunakan operator '+'

# Mencari index dari elemen dalam tuple
find_my_tuple_index = my_tuple_1.index(19)
print(find_my_tuple_index)  # Output: 3 (index ke-3 dari nilai 19)

# Jika elemen yang dicari tidak ada dalam tuple, akan muncul error
# Berikut adalah contoh yang akan error:
# find_my_tuple_index = my_tuple_1.index(20)  # Akan error: "tuple.index(x): x not in tuple"

# Kesimpulan Kemiripan dengan List:
# 1. Bisa mengakses data dengan index
# 2. Bisa mencari index elemen tertentu
# 3. Bisa menggunakan looping dan kondisi (condition statement)
# 4. Menggunakan len() untuk menghitung jumlah elemen
# 5. Penggabungan tuple hanya bisa menggunakan operator '+'
