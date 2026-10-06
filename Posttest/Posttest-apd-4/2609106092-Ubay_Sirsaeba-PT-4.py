username = "BROWNIES" 
password = "092"
batas = 0

while batas < 3:
    login = input("masukkan username : ").upper()
    login_pass = input("masukkan password : ")
    if login != username or login_pass != password:
        batas += 1
        print("Login Salah!")
        if batas == 3:
            print("Percobaan login telah habis.")
            exit()
    else:
        print("Login Berhasil!")
        break

uang_bulanan = int(input("Masukan jumlah uang saku awal : Rp "))
total_pengeluaran = 0

while uang_bulanan > 0:
    print("=== Menu Utama ===")
    print("[1] catat pengeluaran")
    print("[2] Cek sisa uang saku")
    print("[3] Keluar")
    pilihan = input("Pilih menu (1-3): ")
    if pilihan == "1":
        while uang_bulanan > 0:
            pengeluaran = int(input("Masukan nominal pengeluaran: Rp "))
            uang_bulanan -= pengeluaran
            total_pengeluaran += pengeluaran
            print("Sisa uang saku: Rp", uang_bulanan)
            if uang_bulanan <= 0:
                print("Uang saku telah habis.")
                break
            lagi = input("Apakah Anda ingin mencatat pengeluaran lagi? (ya/tidak):")
            if lagi == "tidak":
                break
    elif pilihan == "2":
        print("===Rekapitulasi===")
        print("Sisa uang saku : Rp", uang_bulanan)
        print("Total pengeluaran : Rp", total_pengeluaran)
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
    if uang_bulanan <= 0:
        print("Uang saku telah habis.")
        break

