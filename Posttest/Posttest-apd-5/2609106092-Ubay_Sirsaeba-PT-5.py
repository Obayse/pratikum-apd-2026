print("==========================================")
print("          SISTEM KARTU MEMBER")
print("==========================================")
data_member = []
while True:
    print("\n========== MENU ADMIN ==========")
    print("1. Daftar Kartu Member")
    print("2. Lihat Data Member")
    print("3. Hapus Kartu Member")
    print("4. Update Pangkat Member")
    print("5. Keluar")
    print("================================")
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        print("\n===== PENDAFTARAN MEMBER =====")
        nama = input("Masukkan nama pelanggan: ")
        print("\nPilihan Pangkat Member:")
        print("1. Silver    - Rp25.000 - Diskon 15%")
        print("2. Gold      - Rp50.000 - Diskon 25%")
        print("3. Platinum  - Rp100.000 - Diskon 35%")
        pangkat = input("Pilih pangkat (1-3): ")
        if pangkat == "1":
            nama_pangkat = "Silver"
            biaya = 25000
            diskon = 15
            keuntungan = "Diskon 15% setiap belanja"
        elif pangkat == "2":
            nama_pangkat = "Gold"
            biaya = 50000
            diskon = 25
            keuntungan = (
                "Diskon 25%, ruangan khusus Gold dan Platinum, "
                "serta barang eksklusif/terbatas"
            )
        elif pangkat == "3":
            nama_pangkat = "Platinum"
            biaya = 100000
            diskon = 35
            keuntungan = (
                "Diskon 35%, ruangan khusus Gold dan Platinum, "
                "barang eksklusif/terbatas, dan pengantaran gratis"
            )
        else:
            print("Pilihan pangkat tidak valid!")
            continue
        nama_ditemukan = False
        for member in data_member:
            if member["nama"].lower() == nama.lower():
                nama_ditemukan = True
                break
        if nama_ditemukan:
            print("Pelanggan sudah memiliki kartu member!")
        else:
            konfirmasi = input(
                "Konfirmasi pendaftaran? (ya/tidak): "
            )
            if konfirmasi.lower() == "ya":
                kartu = {
                    "nama": nama,
                    "pangkat": nama_pangkat,
                    "biaya": biaya,
                    "diskon": diskon,
                    "keuntungan": keuntungan,
                    "status": "Aktif"
                }
                data_member.append(kartu)
                print("\n===== KARTU MEMBER BERHASIL DIBUAT =====")
                print("Nama       :", nama)
                print("Pangkat    :", nama_pangkat)
                print("Biaya      : Rp", format(biaya, ",").replace(",", "."))
                print("Diskon     :", str(diskon) + "%")
                print("Keuntungan :", keuntungan)
                print("Status     : Aktif")
                print("========================================")
                print("Kartu member siap diberikan kepada pelanggan.")
            else:
                print("Pendaftaran dibatalkan.")
    elif pilihan == "2":
        print("\n===== DATA KARTU MEMBER =====")
        if len(data_member) == 0:
            print("Belum ada pelanggan yang terdaftar.")
        else:
            nomor = 1
            for member in data_member:
                print("\nMember ke-", nomor)
                print("Nama       :", member["nama"])
                print("Pangkat    :", member["pangkat"])
                print("Biaya      : Rp", format(
                    member["biaya"], ","
                ).replace(",", "."))
                print("Diskon     :", str(member["diskon"]) + "%")
                print("Keuntungan :", member["keuntungan"])
                print("Status     :", member["status"])
                nomor += 1
    elif pilihan == "3":
        print("\n===== HAPUS KARTU MEMBER =====")
        if len(data_member) == 0:
            print("Belum ada kartu member yang terdaftar.")
        else:
            nama_hapus = input(
                "Masukkan nama pemilik kartu: "
            )
            indeks = -1
            for i in range(len(data_member)):
                if data_member[i]["nama"].lower() == nama_hapus.lower():
                    indeks = i
                    break
            if indeks == -1:
                print("Data member tidak ditemukan.")
            else:
                print("\nData Member Ditemukan")
                print("Nama    :", data_member[indeks]["nama"])
                print("Pangkat :", data_member[indeks]["pangkat"])
                print("Status  :", data_member[indeks]["status"])
                print("\nAlasan penghapusan:")
                print("1. Kartu sudah tidak aktif")
                print("2. Pelanggan melakukan pelanggaran")
                alasan = input("Pilih alasan (1-2): ")
                if alasan == "1" or alasan == "2":
                    konfirmasi = input(
                        "Yakin ingin menghapus kartu? (ya/tidak): "
                    )
                    if konfirmasi.lower() == "ya":
                        if alasan == "1":
                            print("Alasan: Kartu sudah tidak aktif.")
                        else:
                            print("Alasan: Pelanggan melakukan pelanggaran.")
                        data_member.pop(indeks)
                        print("Kartu member berhasil dihapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                else:
                    print("Pilihan alasan tidak valid.")
    elif pilihan == "4":
        print("\n===== UPDATE PANGKAT MEMBER =====")
        if len(data_member) == 0:
            print("Belum ada kartu member yang terdaftar.")
        else:
            nama_update = input(
                "Masukkan nama pemilik kartu: "
            )
            indeks = -1
            for i in range(len(data_member)):
                if data_member[i]["nama"].lower() == nama_update.lower():
                    indeks = i
                    break
            if indeks == -1:
                print("Data member tidak ditemukan.")
            else:
                print("\nData Member Ditemukan")
                print("Nama          :", data_member[indeks]["nama"])
                print("Pangkat Lama  :", data_member[indeks]["pangkat"])
                print("Diskon Lama   :", str(data_member[indeks]["diskon"]) + "%")
                print("\nPilihan Pangkat Baru:")
                print("1. Silver    - Rp25.000 - Diskon 15%")
                print("2. Gold      - Rp50.000 - Diskon 25%")
                print("3. Platinum  - Rp100.000 - Diskon 35%")
                pangkat_baru = input(
                    "Pilih pangkat baru (1-3): "
                )
                if pangkat_baru == "1":
                    nama_pangkat_baru = "Silver"
                    biaya_baru = 25000
                    diskon_baru = 15
                    keuntungan_baru = "Diskon 15% setiap belanja"
                elif pangkat_baru == "2":
                    nama_pangkat_baru = "Gold"
                    biaya_baru = 50000
                    diskon_baru = 25
                    keuntungan_baru = (
                        "Diskon 25%, ruangan khusus Gold dan Platinum, "
                        "serta barang eksklusif/terbatas"
                    )
                elif pangkat_baru == "3":
                    nama_pangkat_baru = "Platinum"
                    biaya_baru = 100000
                    diskon_baru = 35
                    keuntungan_baru = (
                        "Diskon 35%, ruangan khusus Gold dan Platinum, "
                        "barang eksklusif/terbatas, dan pengantaran gratis"
                    )
                else:
                    print("Pilihan pangkat tidak valid!")
                    continue
                if nama_pangkat_baru == data_member[indeks]["pangkat"]:
                    print("Pangkat yang dipilih sama dengan pangkat lama.")
                else:
                    print("\n===== KONFIRMASI UPDATE =====")
                    print("Pangkat Lama :", data_member[indeks]["pangkat"])
                    print("Pangkat Baru :", nama_pangkat_baru)
                    print("Biaya Baru   : Rp", format(
                        biaya_baru, ","
                    ).replace(",", "."))
                    print("Diskon Baru  :", str(diskon_baru) + "%")
                    konfirmasi = input(
                        "Simpan perubahan? (ya/tidak): "
                    )
                    if konfirmasi.lower() == "ya":
                        data_member[indeks]["pangkat"] = nama_pangkat_baru
                        data_member[indeks]["biaya"] = biaya_baru
                        data_member[indeks]["diskon"] = diskon_baru
                        data_member[indeks]["keuntungan"] = keuntungan_baru
                        print("\nPangkat member berhasil diperbarui!")
                        print("Nama       :", data_member[indeks]["nama"])
                        print("Pangkat    :", data_member[indeks]["pangkat"])
                        print("Biaya      : Rp", format(
                            data_member[indeks]["biaya"], ","
                        ).replace(",", "."))
                        print("Diskon     :", str(data_member[indeks]["diskon"]) + "%")
                        print("Keuntungan :", data_member[indeks]["keuntungan"])
                        print("Status     :", data_member[indeks]["status"])
                    else:
                        print("Update dibatalkan.")
    elif pilihan == "5":
        print("\nAdmin keluar dari sistem.")
        print("Terima kasih.")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih 1-5.")
