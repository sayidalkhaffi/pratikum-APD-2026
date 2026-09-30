nama_benar = "sayid"
nim_benar = "95"

nama = input("Masukkan nama panggilan: ")
nim = input("Masukkan digit terakhir NIM: ")

if nama == nama_benar and nim == nim_benar:
    print("Login berhasil")
    print()

    print("Pilih konsol:")
    print("1. PS4 - Rp 10000/jam")
    print("2. PS4 Pro - Rp 15000/jam")
    print("3. PS5 - Rp 20000/jam")
    pilihan = int(input("Masukkan pilihan (1-3): "))

    if pilihan == 1 or pilihan == 2 or pilihan == 3:
        if pilihan == 1:
            konsol = "PS4"
            harga = 10000
        elif pilihan == 2:
            konsol = "PS4 Pro"
            harga = 15000
        else:
            konsol = "PS5"
            harga = 20000

        jam = int(input("Masukkan jumlah jam sewa: "))

        if jam >= 5:
            persen = 0.08
        elif jam >= 3:
            persen = 0.05
        else:
            persen = 0

        total_harga = harga * jam
        diskon = int(persen * total_harga)
        total_bayar = total_harga - diskon

        print()
        print("===== STRUK RENTAL =====")
        print("Nama          :", nama)
        print("NIM           :", nim)
        print("Jenis konsol  :", konsol)
        print("Jumlah jam    :", jam)
        print("Total harga   : Rp", total_harga)
        print("Diskon durasi : Rp", diskon)
        print("Total bayar   : Rp", total_bayar)
    else:
        print("Pilihan tidak ada, program berhenti")
else:
    print("Login gagal")