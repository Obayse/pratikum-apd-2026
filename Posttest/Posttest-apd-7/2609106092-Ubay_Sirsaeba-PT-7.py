
nama_aplikasi = "SISTEM KARTU MEMBER"
batas_menu = 5
data_member = []
def tampilkan_menu():
    print("\n========== MENU ADMIN ==========")
    print("1. Daftar Kartu Member")
    print("2. Lihat Data Member")
    print("3. Hapus Kartu Member")
    print("4. Update Pangkat Member")
    print("5. Keluar")
    print("================================")
def tampilkan_pangkat():
    print("\nPilihan Pangkat Member:")
    print("1. Silver   - Rp25.000 - Diskon 15%")
    print("2. Gold     - Rp50.000 - Diskon 25%")
    print("3. Platinum - Rp100.000 - Diskon 35%")
def cari_member(nama):
    for indeks, member in enumerate(data_member):
        if member["nama"].lower() == nama.lower():
            return indeks
    return -1
def ambil_data_pangkat(pilihan):
    data_pangkat = {
        "1": {
            "pangkat": "Silver",
            "biaya": 25000,
            "diskon": 15,
            "keuntungan": "Diskon 15% setiap belanja"
        },
        "2": {
            "pangkat": "Gold",
            "biaya": 50000,
            "diskon": 25,
            "keuntungan": (
                "Diskon 25%, ruangan khusus Gold dan Platinum, "
                "serta barang eksklusif/terbatas"
            )
        },
        "3": {
            "pangkat": "Platinum",
            "biaya": 100000,
            "diskon": 35,
            "keuntungan": (
                "Diskon 35%, ruangan khusus Gold dan Platinum, "
                "barang eksklusif/terbatas, dan pengantaran gratis"
            )
        }
    }
    return data_pangkat.get(pilihan)
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
    konfirmasi = input("Konfirmasi pendaftaran? (ya/tidak): ").strip().lower()
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
        print("\n===== KARTU MEMBER BERHASIL DIBUAT =====")
        print("Nama       :", kartu["nama"])
        print("Pangkat    :", kartu["pangkat"])
        print("Biaya      : Rp", format(kartu["biaya"], ",").replace(",", "."))
        print("Diskon     :", str(kartu["diskon"]) + "%")
        print("Keuntungan :", kartu["keuntungan"])
        print("Status     :", kartu["status"])
    else:
        print("Pendaftaran dibatalkan.")
def lihat_member():
    print("\n===== DATA KARTU MEMBER =====")
    if not data_member:
        print("Belum ada pelanggan yang terdaftar.")
        return
    for nomor, member in enumerate(data_member, start=1):
        print("\nMember ke-", nomor)
        print("Nama       :", member["nama"])
        print("Pangkat    :", member["pangkat"])
        print("Biaya      : Rp", format(member["biaya"], ",").replace(",", "."))
        print("Diskon     :", str(member["diskon"]) + "%")
        print("Keuntungan :", member["keuntungan"])
        print("Status     :", member["status"])
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
    print("\nNama    :", member["nama"])
    print("Pangkat :", member["pangkat"])
    print("Status  :", member["status"])
    print("\nAlasan penghapusan:")
    print("1. Kartu sudah tidak aktif")
    print("2. Pelanggan melakukan pelanggaran")
    alasan = input("Pilih alasan (1-2): ").strip()
    if alasan not in ("1", "2"):
        print("Pilihan alasan tidak valid!")
        return
    konfirmasi = input("Yakin ingin menghapus kartu? (ya/tidak): ").strip().lower()
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
    print("\nNama         :", member["nama"])
    print("Pangkat Lama :", member["pangkat"])
    print("Diskon Lama  :", str(member["diskon"]) + "%")
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
    print("Biaya Baru   : Rp", format(pangkat_baru["biaya"], ",").replace(",", "."))
    print("Diskon Baru  :", str(pangkat_baru["diskon"]) + "%")
    konfirmasi = input("Simpan perubahan? (ya/tidak): ").strip().lower()
    if konfirmasi == "ya":
        member.update(pangkat_baru)
        print("Pangkat member berhasil diperbarui!")
        print("Nama       :", member["nama"])
        print("Pangkat    :", member["pangkat"])
        print("Biaya      : Rp", format(member["biaya"], ",").replace(",", "."))
        print("Diskon     :", str(member["diskon"]) + "%")
        print("Keuntungan :", member["keuntungan"])
        print("Status     :", member["status"])
    else:
        print("Update dibatalkan.")

print("=" * 42)
print("       " + nama_aplikasi)
print("=" * 42)

while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Pilih menu (1-5): "))
        if pilihan < 1 or pilihan > batas_menu:
            print("Pilihan tidak valid! Silakan pilih 1-5.")
            continue
        if pilihan == 1:
            daftar_member()
        elif pilihan == 2:
            lihat_member()
        elif pilihan == 3:
            hapus_member()
        elif pilihan == 4:
            update_pangkat()
        elif pilihan == 5:
            print("\nAdmin keluar dari sistem.")
            print("Terima kasih.")
            break
    except ValueError:
        print("Input harus berupa angka 1-5!")
    except (EOFError, KeyboardInterrupt):
        print("\nInput dihentikan. Program ditutup.")
        break
    except Exception as error:
        print("Terjadi kesalahan:", error)
