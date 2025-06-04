# ===============================
# DICTIONARY DASAR DI PYTHON
# ===============================

# Dictionary adalah struktur data yang menyimpan data dalam format key-value
# Format umum: {key1: value1, key2: value2, ...}

my_dictionary = {
    'nilai': 89,
    'nama': 'Faroja',
    'Alamat': 'Tangerang Selatan',
    'umur': 19
}

# ===============================
# AKSES DATA
# ===============================

# Mengakses nilai dengan key
print(my_dictionary['nilai'])    # Output: 89
print(my_dictionary['nama'])     # Output: Faroja

# Alternatif akses data menggunakan method get()
print(my_dictionary.get('nama'))     # Output: Faroja
print(my_dictionary.get('nilai'))    # Output: 89

# ===============================
# MENGUBAH NILAI
# ===============================

# Mengubah nilai dari key yang sudah ada
my_dictionary['nilai'] = 120
print(my_dictionary['nilai'])    # Output: 120

# ===============================
# MENAMBAH DATA BARU
# ===============================

# Menambahkan key-value baru
my_dictionary['Peliharaan'] = 'Kucing'
print(my_dictionary)

# ===============================
# MENGHAPUS DATA
# ===============================

# Menghapus data berdasarkan key
del my_dictionary['Peliharaan']          # Menghapus 'Peliharaan'
my_dictionary.pop('nilai')               # Menghapus 'nilai'

# popitem() menghapus item terakhir yang dimasukkan (untuk Python 3.7+)
# Tapi perlu dipanggil sebagai fungsi
my_dictionary.popitem()                  # <- ini menghapus satu key terakhir (random di versi < 3.7)
print(my_dictionary)

# Menghapus semua isi dictionary
my_dictionary.clear()
print(my_dictionary)                     # Output: {}

# ===============================
# LOOPING DI DICTIONARY
# ===============================

# Reset dictionary
my_dictionary = {
    'nilai': 89,
    'nama': 'Faroja',
    'Alamat': 'Tangerang Selatan',
    'umur': 19
}

# Loop melalui key saja
for key in my_dictionary:
    print(f'{key} = {my_dictionary[key]}')

# Loop hanya key
for key in my_dictionary.keys():
    print(f'Key: {key}')

# Loop hanya value
for value in my_dictionary.values():
    print(f'Value: {value}')

# Loop key dan value sekaligus
for key, value in my_dictionary.items():
    print(f'Key: {key}, Value: {value}')

# ===============================
# CEK KEY ATAU VALUE DALAM DICTIONARY
# ===============================

if 'nama' in my_dictionary:
    print("'nama' adalah key di dictionary")

if 'nama' in my_dictionary.keys():
    print("'nama' adalah key di dictionary (dengan .keys())")

if 'Faroja' in my_dictionary.values():
    print("'Faroja' adalah value di dictionary")

# ===============================
# FUNGSI LAIN
# ===============================

# Menghitung panjang dictionary (jumlah key)
print(len(my_dictionary))   # Output: 4

# ===============================
# COPY DICTIONARY
# ===============================

# Copy dengan method .copy()
my_dictionary_2 = my_dictionary.copy()
my_dictionary_2.clear()
print(my_dictionary_2)      # Kosong
print(my_dictionary)        # Tetap utuh

# Copy tanpa method copy (hanya alias / referensi)
my_dictionary_2 = my_dictionary
my_dictionary_2.clear()
print(my_dictionary_2)      # Kosong
print(my_dictionary)        # Ikut kosong (karena pointing ke dict yang sama)

# ===============================
# NESTED DICTIONARY (Dictionary dalam Dictionary)
# ===============================

my_dictionary_3 = {
    'Alamat': {'Sauyunan', 'Tangerang', 'Sukabumi'},
    'Nama': {'Faroja', 'Farhan', 'Fikri'},
    'Nilai': {88, 90, 100}
}

print(my_dictionary_3)