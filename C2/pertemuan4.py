# batas = 5
# for i in range(batas):
#     print("Ini adalah perulangan ke-", i)

# for sapa in range(5):
#     print("halo, selamat datang")

# pratikum ={"apd", "orsikom", "jarkom", 70, 89, 77}
# for i in pratikum:
#     # print(i)
#     print(i, end=" ")


# for i in range(1,10,2):
#     print("angka ke-i: ", i)

# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
# print('') #biar ada jarak tiap iterasi

# jawab = "ya"
# hitung = 0

# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")

# username = "puja"
# batas = 0
# while batas < 3:
#     login = input("masukkan username : ")
#     if login != username:
#         batas += 1
#     else:
#         bastas = 3

# for i in range(10):
#     print(i)
#     if i == 5:
#         break

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(1, 4):
#     if i == 2:
#         continue
#     print(i)

# tinggi = int(input("masukkan tinggi yang kalian mau : "))
# for i in range(1, tinggi + 1):
#     print("*" * i)

tinggi = int(input("masukkan tinggi yang kalian mau : "))
for i in range(tinggi):
    print(" " * (tinggi - i - 1), end="")
    print("*" * (i+1))

##################################
    # spasi = " " * (tinggi - i)
    # tanda = "*" * i
    # print(tanda + spasi)