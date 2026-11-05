from data import data_member, cari_member, ambil_data_pangkat
from tampilan import tampilkan_pangkat, tampilkan_detail_member, tampilkan_semua_member


def daftar_member():
    nama = input("Masukkan nama pelanggan: ").strip()

    if not nama:
        print("Nama tidak boleh kosong!")
        return

    if cari_member(nama) != -1:
        print("Pelanggan sudah memiliki kartu member!")
        return

    tampilkan_pangkat()
    pilihan = input("Pilih pangkat (1-3): ").strip()

    pangkat = ambil_data_pangkat(pilihan)

    if pangkat is None:
        print("Pilihan pangkat tidak valid!")
        return

    konfirmasi = input(
        "Konfirmasi pendaftaran? (ya/tidak): "
    ).strip().lower()

    if konfirmasi == "ya":
        kartu = {
            "nama": nama,
            "pangkat": pangkat["pangkat"],
            "biaya": pangkat["biaya"],
            "diskon": pangkat["diskon"],
            "keuntungan": pangkat["keuntungan"],
            "status": "Aktif"
        }

        data_member.append(kartu)

        print("\nKartu member berhasil dibuat!")
        tampilkan_detail_member(kartu)

    else:
        print("Pendaftaran dibatalkan.")


def lihat_member():
    tampilkan_semua_member(data_member)


def hapus_member():
    if not data_member:
        print("Belum ada kartu member yang terdaftar.")
        return

    nama = input("Masukkan nama pemilik kartu: ").strip()
    indeks = cari_member(nama)

    if indeks == -1:
        print("Data member tidak ditemukan.")
        return

    member = data_member[indeks]

    tampilkan_detail_member(member)

    print("\nAlasan penghapusan:")
    print("1. Kartu sudah tidak aktif")
    print("2. Pelanggan melakukan pelanggaran")

    alasan = input("Pilih alasan (1-2): ").strip()

    if alasan not in ("1", "2"):
        print("Pilihan alasan tidak valid!")
        return

    konfirmasi = input(
        "Yakin ingin menghapus kartu? (ya/tidak): "
    ).strip().lower()

    if konfirmasi == "ya":
        if alasan == "1":
            print("Alasan: Kartu sudah tidak aktif.")
        else:
            print("Alasan: Pelanggan melakukan pelanggaran.")

        data_member.pop(indeks)
        print("Kartu member berhasil dihapus.")

    else:
        print("Penghapusan dibatalkan.")


def update_pangkat():
    if not data_member:
        print("Belum ada kartu member yang terdaftar.")
        return

    nama = input("Masukkan nama pemilik kartu: ").strip()
    indeks = cari_member(nama)

    if indeks == -1:
        print("Data member tidak ditemukan.")
        return

    member = data_member[indeks]

    tampilkan_detail_member(member)
    tampilkan_pangkat()

    pilihan = input("Pilih pangkat baru (1-3): ").strip()
    pangkat_baru = ambil_data_pangkat(pilihan)

    if pangkat_baru is None:
        print("Pilihan pangkat tidak valid!")
        return

    if pangkat_baru["pangkat"] == member["pangkat"]:
        print("Pangkat yang dipilih sama dengan pangkat lama.")
        return

    print("\n===== KONFIRMASI UPDATE =====")

    print("Pangkat Lama :", member["pangkat"])
    print("Pangkat Baru :", pangkat_baru["pangkat"])
    print(
        "Biaya Baru   : Rp",
        format(pangkat_baru["biaya"], ",").replace(",", ".")
    )
    print("Diskon Baru  :", str(pangkat_baru["diskon"]) + "%")

    konfirmasi = input(
        "Simpan perubahan? (ya/tidak): "
    ).strip().lower()

    if konfirmasi == "ya":
        member.update(pangkat_baru)

        print("Pangkat member berhasil diperbarui!")
        tampilkan_detail_member(member)

    else:
        print("Update dibatalkan.")