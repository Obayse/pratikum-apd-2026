# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas
# #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang())

# def luas_persegi(panjang, lebar):
#     luas = panjang * lebar
#     return luas
# #Kita panggil fungsinya lalu argumen kita adalah angka 7
# print("Luas persegi:", luas_persegi(7, 5))
# print("Luas persegi:", luas_persegi(5, 3))
# print("Luas persegi:", luas_persegi(8, 99))
#Output
# Luas persegi: 49

# def pengumuman(matkul):
#     print(f"Hari ini Pengujian Proyek Akhir {matkul}")
# pengumuman("apd")

# def perkenalan(nama):
#     nama = input("masukkan nama anda : ")
#     print(f"Perkenalkan nama saya {nama}")
# perkenalan("ubay")


#Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"
# #Membuat variabel lokal
# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)
#     #Mengakses variabel lokal
# data()
# #Mengakses variabel global
# print("Nama:", nama)
# print("Prodi:", prodi)
#Output
# Nama: Teknik Kedokteran
# Prodi: Kedokteran Lanjut
# Nama: Larry
# Prodi: Informatika

# def hitung_mundur(n):
#     if n == 0:
#         print("selesai")
#     else:
#         print(n)
#         hitung_mundur(n-1)
# hitung_mundur(5)

#Variabel global untuk menyimpan data buku
# buku = []

# def lihat_buku():
#     if len(buku) == 0:
#         print("Belum ada data buku")
#     else:
#         print("ID Buku | Judul Buku")
#         for indeks in range(len(buku)):
#             print(indeks, "|", buku[indeks])

# def tambah_buku():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru)
#     print("Buku berhasil ditambahkan!")

# def edit_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku_baru = input("Judul baru: ")
#         buku[indeks] = buku_baru
#         print("Buku berhasil diupdate!")

# def hapus_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku.remove(buku[indeks])
#         print("Buku berhasil dihapus!")

# def tampilkan_menu():
#     print("\n")
#     print("========= MENU =========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")
#     try:
#         menu = int(input("PILIH MENU > "))
#         print("\n")
#         if menu == 1:
#             lihat_buku()
#         elif menu == 2:
#             tambah_buku()
#         elif menu == 3:
#             edit_buku()
#         elif menu == 4:
#             hapus_buku()
#         elif menu == 5:
#             exit()
#         else:
#             print("Pilihan tidak valid!")
#     except ValueError:
#         print("input harus berupa angka")
#     finally:
#         print("pasti berhasil")

# if __name__ == " _main _":
#     while(True):
#         tampilkan_menu()

# umur = int(input('Masukkan Angka : '))
# print(umur) #input 'cinta APD'

# try:
#     umur = int(input('Masukkan umur : '))
# execpt ValueError:
#     print("umur yang dimasukan ")

try:
    angka = int(input('Masukkan Angka : '))
except ValueError:
    print('input yang anda masukkan bukan Integer (angka)')
else :
    print(f'Angka yang kamu input : {angka}')
finally:
    print("program selesai :D")