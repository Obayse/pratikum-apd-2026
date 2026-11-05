from prettytable import PrettyTable


def buat_tabel(judul, kolom, data):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = kolom

    for baris in data:
        tabel.add_row(baris)

    print(tabel)


def tampilkan_menu():
    data_menu = [
        [1, "Daftar Kartu Member"],
        [2, "Lihat Data Member"],
        [3, "Hapus Kartu Member"],
        [4, "Update Pangkat Member"],
        [5, "Keluar"]
    ]

    buat_tabel(
        "MENU ADMIN",
        ["Nomor", "Pilihan Menu"],
        data_menu
    )


def tampilkan_pangkat():
    data_pangkat = [
        ["1", "Silver", "Rp25.000", "15%"],
        ["2", "Gold", "Rp50.000", "25%"],
        ["3", "Platinum", "Rp100.000", "35%"]
    ]

    buat_tabel(
        "PILIHAN PANGKAT MEMBER",
        ["Nomor", "Pangkat", "Biaya", "Diskon"],
        data_pangkat
    )


def tampilkan_semua_member(data_member):
    if not data_member:
        print("Belum ada pelanggan yang terdaftar.")
        return

    data_tabel = []

    for nomor, member in enumerate(data_member, start=1):
        data_tabel.append([
            nomor,
            member["nama"],
            member["pangkat"],
            f"Rp{member['biaya']:,}".replace(",", "."),
            f"{member['diskon']}%",
            member["status"]
        ])

    buat_tabel(
        "DATA KARTU MEMBER",
        ["No", "Nama", "Pangkat", "Biaya", "Diskon", "Status"],
        data_tabel
    )


def tampilkan_detail_member(member):
    data_tabel = [
        ["Nama", member["nama"]],
        ["Pangkat", member["pangkat"]],
        ["Biaya", f"Rp{member['biaya']:,}".replace(",", ".")],
        ["Diskon", f"{member['diskon']}%"],
        ["Keuntungan", member["keuntungan"]],
        ["Status", member["status"]]
    ]

    buat_tabel(
        "DETAIL KARTU MEMBER",
        ["Keterangan", "Informasi"],
        data_tabel
    )