# lemari = ["baju", "celana", 69, 7.2, True]
# print("sebelum di append")
# print(lemari)
# lemari.append("KTP")
# print("sesudah di append")
# print(lemari)

# lemari = ["baju", "celana", 69, 7.2, True]
# print("sebelum di append")
# print(lemari)
# lemari.extend(["KTP", "sepatu", "dompet"])
# print("sesudah di append")
# print(lemari)

# lemari = ["baju", "celana", 69, 7.2, True]
# print("sebelum di append")
# print(lemari)
# lemari.insert(1, "KTP")
# print("sesudah di append")
# print(lemari)

# lemari = ["baju", "celana", 69, 7.2, True, 70, 222, 240]
# jumlah = 0
# for item in lemari:
#     if type (item) == int:
#         print(item)
#         jumlah += 1
# print("Jumlah elemen bertipe int:", ju

# for index, item in enumerate(lemari):
#     print(f"index ke-{index-1}: {item}")

# lemari = ["baju", "celana", 69, 7.2, True, 70, 222, 240]

# angka1 = [ [1, 2], [3, 4] ]
# print(angka1[0][1], angka1[1][0])


# angka2 = [2, 4, 6]
# gabungan = angka1 + angka2
# print("gabungan:", gabungan)

# ulang = angka1 * 3
# print("ulang:", ulang)

# print("Sebelum diubah:")
# print(lemari)

# lemari[1] = "celana panjang"
# print(" Sesudah diubah:")
# print(lemari)

# print("sebelum diubah")
# print(lemari)
# lemari.remove("baju")
# lemari.remove("celana")
# print("sesudah diubah")
# print(lemari)

# sisa = lemari.pop(0)

# print("sesudah diubah")
# print(lemari)

# print("elemen yang dihapus:", sisa)


# angka = (1, 2, 3, "Halo", True)
# ubah = list(angka)
# angka.append("hai")

# angka = tuple(ubah)
# print(angka)

lemari = ("baju", "celana", "sepatu")
(atasan, *bawahan) = lemari

print(bawahan)