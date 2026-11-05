data_member = []

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