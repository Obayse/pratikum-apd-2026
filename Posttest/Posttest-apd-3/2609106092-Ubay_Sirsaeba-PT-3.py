nama_panggilan = input("Masukkan nama imut Kamu : ")
nim = input("Masukkan NIM kamu : ")

if nama_panggilan == "Brownies" and nim == "092":
    print("\nLogin berhasil! :D")
    print("Selamat datang di Rental PlayStation")
    
    
    print("\n=== PILIHAN KONSOL ===")
    print("1. PS4     - Rp10.000/jam")
    print("2. PS4 Pro - Rp15.000/jam")
    print("3. PS5     - Rp20.000/jam")
    
    pilihan = int(input("Pilih jenis konsol (1-3): "))
    
    if pilihan == 1:
        konsol = "PS4"
        harga_per_jam = 10.000
    
    elif pilihan == 2:
        konsol = "PS4 Pro"
        harga_per_jam = 15.000
    
    elif pilihan == 3:
        konsol = "PS5"
        harga_per_jam = 20.000
    else:
        print("Maaf, tidak ada pilihan yang sesuai :(")
        print("Program berhenti.")
        exit()
    
    jumlah_jam = int(input("Masukkan jumlah jam sewa: "))
    
    total_harga = harga_per_jam * jumlah_jam
    
    if jumlah_jam >= 5:
        persen_diskon = 0.08
    elif jumlah_jam >= 3:
        persen_diskon = 0.05
    else:
        persen_diskon = 0
    
    diskon_Waktu = persen_diskon * total_harga
    total_bayar = total_harga - diskon_Waktu
    
    print("\n=== DETAIL TRANSAKSI ===")
    print("Nama           :", nama_panggilan)
    print("NIM            :", nim)
    print("Jenis Konsol   :", konsol)
    print("Jumlah Jam     :", jumlah_jam, "jam")
    print("Total Harga    : Rp", int(total_harga))
    print("Diskon Waktu   : Rp", int(diskon_Waktu))
    print("Total Bayar    : Rp", int(total_bayar))
else:
    print("\nLogin salah! :(")
    print("Program berhenti.")