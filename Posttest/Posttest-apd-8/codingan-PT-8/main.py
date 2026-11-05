from tampilan import tampilkan_menu
from member import daftar_member, lihat_member, hapus_member, update_pangkat


nama_aplikasi = "SISTEM KARTU MEMBER"
batas_menu = 5

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