# Introduction to Function

# Function adalah blok kode yang memiliki nama, dapat menerima input, mengeluarkan output,
# dan dapat digunakan berulang kali.

# Analogi Function dalam Dapur:
# Bayangkan Anda seorang koki di dapur. Anda sering membuat teh manis.
# Daripada melakukan proses membuat teh dari awal setiap kali, Anda bisa membuat "resep" (function)
# sehingga setiap kali ingin membuat teh, Anda cukup menjalankan "resep" tersebut.

# Contoh paling sederhana function tanpa input dan output

def say_hello():
    """
    Function ini hanya mencetak "Hello, Selamat Datang di Dapur!"
    Tidak memiliki parameter (input) dan tidak mengembalikan nilai (output).
    """
    print("Hello, Selamat Datang di Dapur!")

# Function tanpa input dan output digunakan untuk tugas-tugas sederhana
# yang hanya menjalankan instruksi tanpa perlu menerima data atau mengembalikan hasil
# Memanggil function say_hello
say_hello()

#-------------------------------------------------------------------------------------------------------------------
# Output:
# Hello, Selamat Datang di Dapur!

# Function dengan Parameter (Input) tetapi tanpa Return (Output)
def salam_balik(nama, umur ):
    """
    Function ini menerima input berupa nama dan mencetak salam.
    """

    print(f"Halo {nama}, selamat datang kembali di dapur! ,{umur} umur anda sekian")

# Memanggil function dengan parameter
input_nama = input('Masukan Nama Kamu: ')
input_umur = input('Masukan Umur Kamu: ')

salam_balik(input_nama, input_umur)

my_var = print('Halo Budi')
print(my_var)
salam_balik("Ani")


# Function dengan Parameter (Input)
def buat_teh(gula):
    """
    Function untuk membuat teh manis dengan jumlah gula yang bisa ditentukan.
    Memiliki parameter (input) gula.
    """
    print(f"Membuat teh dengan {gula} sendok gula.")

# Memanggil function dengan parameter
buat_teh(2)
buat_teh(5)

# Output:
# Membuat teh dengan 2 sendok gula.
# Membuat teh dengan 5 sendok gula.
# Function tanpa input dan output biasanya 
# digunakan untuk menjalankan tugas tertentu 
# yang tidak memerlukan parameter dan tidak mengembalikan nilai.
# Contoh pengunaan untuk
# 1. Menampilkan pesan tetap
# 2. Menjalankan serangkaian perintah tetap
# 3. Meningkatkan keterbacaan kode

# Default Parameter
# Mendefinisikan function dengan default parameter
def salamBalik(nama = 'Tidak diketahui', usia = 0):
    print(f"Hello, {nama}! Usia kamu {usia} tahun.")

# Memanggil function dengan memberikan satu argument
salamBalik("Ali",17)

# Memanggil function tanpa memberikan argument
salamBalik()

# Memanggil function dengan memberikan dua argument
salamBalik("Budi", 25)

# Di dalam function salamBalik, terdapat dua parameter yaitu nama dan usia. Kedua parameter ini memiliki nilai default: nama="Unknown" dan usia=0.
# Jika kita memanggil function tanpa memberikan argument, maka function akan menggunakan nilai default untuk nama dan usia.#
# Jika kita hanya memberikan satu argument (misalnya salamBalik("Ali")), maka parameter nama akan berisi "Ali", dan usia akan menggunakan nilai default yaitu 0.
# Jika kita memberikan kedua argument (misalnya salamBalik("Budi", 25)), maka kedua parameter tersebut akan diisi dengan nilai yang diberikan.


#-------------------------------------------------------------------------------------------------------------------
# Function dengan Input & Return (Output)
def jumlahkan(angka1, angka2):
    """
    Function ini menjumlahkan dua angka dan mengembalikan hasilnya.
    """
    return angka1+angka2

# Menggunakan hasil function
hasil = jumlahkan(3, 4)
print(f"Hasil penjumlahan: {hasil}")

# Output:
# Hasil penjumlahan: 7

# Lambda Function (Function Singkat)
# Function sederhana untuk perkalian dua angka
dikali = lambda x, y: x * y
print(f"Hasil perkalian: {dikali(3, 5)}")

# Output:
# Hasil perkalian: 15

# Kesimpulan:
# 1. Function membantu mengorganisir kode agar lebih rapi dan reusable.
# 2. Bisa memiliki parameter sebagai input.
# 3. Bisa mengembalikan nilai menggunakan return.
# 4. Bisa dibuat dengan def (regular function) atau lambda (function sederhana).

# Function sangat berguna dalam pemrograman untuk menghindari kode duplikat
# dan membuat program lebih mudah dikelola!

#-------------------------------------------------------------------------------------------------------------------
# Local Variable & Global Variabel
# Penjelasan tentang Variabel Global dan Local

# Variabel Global: Variabel yang dideklarasikan di luar fungsi atau blok kode dan bisa diakses dari mana saja dalam program.
x = 10  # Ini adalah variabel global

def contoh_local_global():
    # Variabel Local: Variabel yang dideklarasikan di dalam fungsi dan hanya bisa diakses di dalam fungsi tersebut.
    y = 5  # Ini adalah variabel local
    print(f"Local variabel y: {y}")  # Bisa mengakses y karena y adalah variabel local dalam fungsi ini
    print(f"Global variabel x: {x}")  # Bisa mengakses x karena x adalah variabel global

contoh_local_global()

# Output:
# Local variabel y: 5
# Global variabel x: 10

# Variabel Global yang dimodifikasi dalam fungsi:
def modify_global():
    global x  # Menyatakan bahwa kita ingin menggunakan variabel global x, bukan membuat variabel baru
    x = 20  # Mengubah nilai variabel global x

modify_global()
print(f"Nilai x setelah diubah: {x}")  # Output: 20

#-------------------------------------------------------------------------------------------------------------------
# Penjelasan tentang Callback Function

# Callback function adalah fungsi yang diteruskan sebagai argumen ke fungsi lain dan dipanggil di dalam fungsi tersebut.
# Callback memungkinkan kita untuk menunda eksekusi kode atau memberikan fleksibilitas dalam fungsi yang kita buat.

# Contoh sederhana:

# Fungsi yang menerima callback function sebagai argumen
def proses_data(data, callback, umur):
    print(f"Memproses data: {data}")
    # Memanggil callback function setelah proses selesai
    callback(data,umur)

# Callback function yang akan dipanggil
def tampilkan_data(input_function = 'Tidak diketahui',umur  =0):
    print(f"Data yang telah diproses: {input_function}, dengan umur {umur}")

# Memanggil fungsi utama dengan memberikan fungsi callback
proses_data(data = "Faroja",umur = 11 ,callback = tampilkan_data)

# Output:
# Memproses data: Data Pelanggan
# Data yang telah diproses: Data Pelanggan

# Penjelasan tambahan:
# Callback function digunakan untuk memperkenalkan logika tambahan atau penanganan hasil
# setelah sebuah operasi selesai tanpa harus menunggu hasilnya di dalam fungsi utama.
# Callback sering digunakan untuk penanganan event, seperti dalam pengolahan data atau event-driven programming,
# yang memungkinkan kita untuk menangani aksi tertentu setelah tugas utama selesai.
#-------------------------------------------------------------------------------------------------------------------
# Penjelasan tentang Calling Other Function

# Calling other function berarti memanggil atau menjalankan sebuah fungsi dari dalam fungsi lain.
# Fungsi dalam Python dapat saling memanggil satu sama lain, 
# baik di dalam satu blok kode ataupun dalam beberapa struktur program yang lebih kompleks.

# Contoh sederhana:

# Fungsi pertama yang menerima dua angka dan menjumlahkannya
def tambah(a, b):
    return a + b

# Fungsi kedua yang memanggil fungsi 'tambah' untuk melakukan operasi penjumlahan
def hitung_total():
    x = 5
    y = 9
    total = tambah(x, y)  # Memanggil fungsi 'tambah' dari dalam fungsi 'hitung_total'
    print(f"Total: {total}")

# Memanggil fungsi hitung_total
hitung_total()

# Output:
# Total: 8

# Penjelasan tambahan:
# Di contoh ini, fungsi 'hitung_total' memanggil fungsi lain yaitu 'tambah'.
# Fungsi 'tambah' bertugas untuk menjumlahkan dua angka, sementara 'hitung_total' bertanggung jawab untuk menggunakan hasil penjumlahan tersebut.
# Ini adalah contoh umum dalam pemrograman untuk membuat kode lebih modular dan terstruktur.

#-------------------------------------------------------------------------------------------------------------------
# Penjelasan tentang Recursive Function
# Recursive function adalah fungsi yang memanggil dirinya sendiri untuk menyelesaikan masalah.
# Dalam recursive function, kita membutuhkan dua hal penting:
# 1. **Base case**: Kondisi yang menghentikan rekursi.
# 2. **Recursive case**: Bagian di mana fungsi memanggil dirinya sendiri dengan argumen yang lebih kecil.

# Fungsi countdown menggunakan rekursi untuk menghitung mundur dari n hingga 0
def countdown(n):
    # Base case: jika n sudah 0, hentikan rekursi
    if n == 0:
        print("Selesai!")  # Menghentikan rekursi dan mencetak "Selesai!"
    else:
        # Menampilkan n dan memanggil countdown untuk n-1
        print(n)
        countdown(n - 1)  # Memanggil fungsi countdown dengan argumen n-1

# Memanggil fungsi countdown untuk menghitung mundur dari 5
countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1
# Selesai!

# Penjelasan:
# - Fungsi 'countdown' memanggil dirinya sendiri (recursive case) dengan mengurangi nilai n setiap kali.
# - Ketika n mencapai 0, fungsi tidak lagi memanggil dirinya sendiri dan berhenti (base case).
# - Proses ini memungkinkan kita untuk menghitung mundur secara otomatis tanpa menggunakan loop.
#-------------------------------------------------------------------------------------------------------------------

# Penjelasan singkat tentang Map Function dan Lambda Function

# Lambda Function adalah fungsi anonim (tanpa nama) yang bisa digunakan untuk operasi sederhana
# Biasanya digunakan dalam fungsi seperti map() atau filter() untuk operasi yang hanya membutuhkan satu kali penggunaan

# Contoh Lambda Function
function_kali2 = lambda x: x * 2  # Fungsi lambda yang mengalikan nilai dengan 2
function_tambah = lambda x, y: x + y  # Fungsi lambda yang menjumlahkan dua angka
function_kurang = lambda x, y, z: x - y - z  # Fungsi lambda yang mengurangi tiga angka

# Menggunakan Map Function
# Map function digunakan untuk memanipulasi data dalam sebuah collection (misalnya list, tuple)
# Tanpa merubah jumlah data, hanya nilai-nilainya yang diubah dengan fungsi callback

# List awal
list1 = [1, 2, 3, 4, 5]

# Fungsi yang akan digunakan dengan map, mengalikan nilai dengan 2
def kali2_func(x):
    return x * 2

# Menggunakan map untuk mengubah setiap elemen di list1
hasilMap = map(kali2_func, list1)  # Map function mengembalikan objek map

# Mengubah objek map menjadi list dan menampilkan hasilnya
hasilMapList = list(hasilMap)
print("Hasil map dengan function kali2_func:", hasilMapList)

# Hasilnya: [2, 4, 6, 8, 10]

# Menggunakan map dengan lambda function (lebih efektif daripada membuat function terpisah)
hasilMapLambda = map(lambda x: x * 2, list1)

# Mengubah objek map menjadi list dan menampilkan hasilnya
hasilMapListLambda = list(hasilMapLambda)
print("Hasil map dengan lambda function:", hasilMapListLambda)

# Hasilnya: [2, 4, 6, 8, 10]

# Penjelasan:
# - Fungsi map menerima dua argumen: sebuah fungsi dan sebuah collection (list1).
# - Fungsi yang diberikan akan diterapkan pada setiap elemen di collection tersebut.
# - Map mengembalikan objek map yang harus diubah menjadi list atau tipe data lain.
# - Lambda function membuat kode lebih ringkas tanpa perlu mendefinisikan fungsi terpisah.

# map digunakan untuk mengubah setiap elemen dalam kumpulan data (list, tuple, dll) 
# dengan menerapkan fungsi tertentu tanpa mengubah jumlah elemen dalam kumpulan data tersebut.

# Kapan menggunakan map:
# 1. Ketika kamu ingin menerapkan fungsi yang sama ke setiap elemen dalam koleksi.
# 2. Jika kamu ingin mengubah atau memodifikasi elemen-elemen dalam koleksi (misal: perkalian, pengubahan huruf kapital, dll).
# 3. Menghindari penggunaan loop eksplisit untuk operasi sederhana.

#-------------------------------------------------------------------------------------------------------------------
# List angka yang akan diproses
list1 = [1, 2, 3, 4, 5]

# Fungsi untuk memeriksa apakah angka genap
def angkaGenap(x):
    return x % 2 == 0

# Menggunakan filter dengan fungsi angkaGenap sebagai callback function
hasilFilter = filter(angkaGenap, list1)

# Mengubah objek filter menjadi list dan menampilkan hasilnya
hasilFilterList = list(hasilFilter)
print("Hasil filter menggunakan fungsi biasa (ambil angka genap):", hasilFilterList)

# Output:
# Hasil filter menggunakan fungsi biasa (ambil angka genap): [2, 4]
# Penjelasan
# Fungsi Biasa: Di sini kita mendefinisikan fungsi angkaGenap yang memeriksa apakah suatu angka genap.
# Filter Function: filter(angkaGenap, list1) akan memfilter elemen-elemen dalam list1 yang memenuhi kondisi dalam fungsi angkaGenap (angka genap).
# Output: Hanya angka genap yang akan muncul dalam hasilnya, yaitu [2, 4].

# List angka yang akan diproses
list1 = [1, 2, 3, 4, 5]

# Menggunakan filter dengan lambda function untuk memeriksa angka genap
hasilFilterLambda = filter(lambda x: x % 2 == 0, list1)

# Mengubah objek filter menjadi list dan menampilkan hasilnya
hasilFilterListLambda = list(hasilFilterLambda)
print("Hasil filter menggunakan lambda function (ambil angka genap):", hasilFilterListLambda)

# Output:
# Hasil filter menggunakan lambda function (ambil angka genap): [2, 4]
# Lambda Function: lambda x: x % 2 == 0 adalah fungsi tanpa nama (anonim) yang langsung digunakan untuk memeriksa apakah suatu angka genap.
# Filter Function: filter(lambda x: x % 2 == 0, list1) bekerja dengan cara yang sama seperti di contoh pertama, tetapi dengan menggunakan lambda untuk menyederhanakan kode.
# Output: Hasilnya tetap sama, yaitu angka genap [2, 4].


# Kapan Menggunakan Filter Function
# 1. Gunakan filter jika kamu ingin menyaring data berdasarkan kondisi yang ditentukan dalam callback function.
# 2. Pilih fungsi biasa jika fungsinya cukup panjang atau perlu digunakan di banyak tempat dalam kode.
# 3. Gunakan lambda function untuk fungsionalitas sederhana, seperti dalam contoh di atas, untuk membuat kode lebih ringkas dan jelas tanpa membuat fungsi terpisah.
#-------------------------------------------------------------------------------------------------------------------
