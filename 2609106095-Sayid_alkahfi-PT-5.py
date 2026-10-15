import os

bersih = "cls" if os.name == "nt" else "clear"

pengguna = [
    ["admin", "admin123", "Admin", "Administrator", "0812544567961"],
    ["sayid", "domeng", "Pengguna Biasa", "Sayid Alkaffi", "081234567890"],
]
tenda = [
    ["T01", "Kanopi Pantai", "3 x 3 m (Kecil)", "Kanopi atap anti-UV, tanpa dinding", "Pantai", 6, 75000, 8],
    ["T02", "Pop-up Beach Shelter", "2 x 2 m (Kecil)", "Pop-up lipat, anti-UV, ventilasi", "Pantai", 3, 50000, 10],
    ["T03", "Gazebo Pantai", "4 x 4 m (Sedang)", "Gazebo rangka besi, tahan angin laut", "Pantai", 12, 150000, 5],
    ["T04", "Tenda Pesta Pantai", "5 x 10 m (Besar)", "Tenda pesta/pernikahan, rangka aluminium anti karat", "Pantai", 60, 600000, 3],
    ["T05", "Dome 2P", "2 x 1,5 m (Kecil)", "Dome double layer, ringan", "Gunung", 2, 40000, 12],
    ["T06", "Dome 4P", "2,4 x 2,4 m (Sedang)", "Dome double layer, waterproof 3000 mm", "Gunung", 4, 70000, 10],
    ["T07", "Tunnel 6P", "4 x 2,5 m (Sedang)", "Tunnel 2 kamar, tahan angin kencang", "Gunung", 6, 110000, 6],
    ["T08", "Basecamp 12P", "4 x 5 m (Besar)", "Tenda basecamp/rombongan, flysheet tebal", "Gunung", 12, 220000, 4],
]
sewa = []
pembayaran = []
id_sewa = 1
id_bayar = 1
no_tenda = 9
user_aktif = None

angka_valid = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}  
bulan_30 = {4, 6, 9, 11}                                        
status_aktif = {"Dipesan", "Lunas"}                                

metode_bayar = {"1": "Tunai", "2": "Transfer", "3": "E-Wallet"}
pilihan_medan = {"1": "Pantai", "2": "Gunung", "3": "Umum"}


while True:
    os.system(bersih)
    print("=" * 50)
    print("          SISTEM SEWA TENDA")
    print("   Pantai | Gunung | Pernikahan | Pesta")
    print("=" * 50)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih_awal = input("Pilih menu (1-3): ").strip()

    if pilih_awal == "2":
        os.system(bersih)
        print("=== REGISTER PELANGGAN ===")
        username_baru = input("Username                : ").strip()
        password_baru = input("Password (min 4 karakter): ").strip()
        nama_baru = input("Nama lengkap            : ").strip()
        teks = input("No. HP (10-13 digit)    : ").strip()
        sudah_ada = False
        for u in pengguna:
            if u[0].lower() == username_baru.lower():
                sudah_ada = True
        angka = True
        for h in teks:
            if h not in angka_valid:
                angka = False
        if teks == "":
            angka = False
        if username_baru == "" or sudah_ada:
            print("Username kosong atau sudah dipakai!")
        elif len(password_baru) < 4:
            print("Password minimal 4 karakter!")
        elif nama_baru == "":
            print("Nama lengkap tidak boleh kosong!")
        elif angka == False or len(teks) < 10 or len(teks) > 13:
            print("No. HP harus berupa 10-13 digit angka!")
        else:
            pengguna.append([username_baru, password_baru, "Pengguna Biasa", nama_baru, teks])
            print("Register berhasil! Silakan login.")
        input("Tekan Enter untuk lanjut...")
        
    elif pilih_awal == "1":
        percobaan = 0
        user_aktif = None
        while percobaan < 3 and user_aktif is None:
            os.system(bersih)
            print("=== LOGIN ===")
            input_user = input("Username : ").strip()
            input_pass = input("Password : ").strip()
            for u in pengguna:
                if u[0] == input_user and u[1] == input_pass:
                    user_aktif = u
            if user_aktif is None:
                percobaan = percobaan + 1
                print("Username/password salah! Sisa percobaan:", 3 - percobaan)
                input("Tekan Enter untuk lanjut...")
        if user_aktif is None:
            print("Login gagal 3 kali. Kembali ke menu awal.")
            input("Tekan Enter untuk lanjut...")
            continue

        while user_aktif is not None:
            os.system(bersih)
            print("=" * 50)
            print("Login sebagai:", user_aktif[3], "(" + user_aktif[2] + ")")
            print("=" * 50)
            print("1. Lihat katalog tenda")
            if user_aktif[2] == "Admin":
                print("2. Tambah tenda")
                print("3. Ubah data tenda (harga/stok)")
                print("4. Hapus tenda")
                print("5. Lihat jadwal & data penyewaan")
                print("6. Proses pengembalian tenda")
                print("7. Lihat data pelanggan")
                print("8. Hapus pelanggan")
                print("9. Riwayat pembayaran")
            else:
                print("2. Sewa tenda")
                print("3. Lihat pesanan & jadwal saya")
                print("4. Ubah pesanan (lama sewa/jumlah)")
                print("5. Bayar pesanan")
                print("6. Batalkan pesanan")
                print("7. Ubah profil")
            print("0. Logout")
            menu = input("Pilih menu: ").strip()

            if menu == "1":
                os.system(bersih)
                print("=== KATALOG TENDA ===")
                print("1. Semua medan")
                print("2. Medan Pantai")
                print("3. Medan Gunung")
                pilih_medan = input("Pilih tampilan (1-3): ").strip()
                if pilih_medan not in ["1", "2", "3"]:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")
                    continue
                cari = ""
                if pilih_medan == "2":
                    cari = "Pantai"
                elif pilih_medan == "3":
                    cari = "Gunung"
                os.system(bersih)
                tampil = 0
                for t in tenda:
                    if cari == "" or t[4] == cari or t[4] == "Umum":
                        print("[" + t[0] + "] " + t[1] + "   (Medan: " + t[4] + ")")
                        print("    Ukuran    :", t[2])
                        print("    Model     :", t[3])
                        print("    Kapasitas :", t[5], "orang")
                        print("    Harga     : Rp", t[6], "/ hari")
                        print("    Stok      :", t[7], "unit")
                        print("-" * 50)
                        tampil = tampil + 1
                if tampil == 0:
                    print("Belum ada tenda untuk tampilan ini.")
                input("Tekan Enter untuk lanjut...")

            elif menu == "0":
                user_aktif = None
                print("Berhasil logout.")
                input("Tekan Enter untuk lanjut...")

            elif user_aktif[2] == "Admin":

                if menu == "2":
                    os.system(bersih)
                    print("=== TAMBAH TENDA ===")
                    nama = input("Nama tenda                    : ").strip()
                    ukuran = input("Ukuran (mis. 3 x 3 m (Kecil)): ").strip()
                    model = input("Model/jenis tenda             : ").strip()
                    medan = input("Medan (1=Pantai 2=Gunung 3=Umum): ").strip()
                    nilai = []
                    valid = True
                    for lab in ["Kapasitas (orang)", "Harga sewa per hari (Rp)", "Stok (unit)"]:
                        teks = input(lab + " : ").strip()
                        angka = True
                        for h in teks:
                            if h not in angka_valid:
                                angka = False
                        if teks == "":
                            angka = False
                        if angka == False:
                            valid = False
                        else:
                            nilai.append(int(teks))
                    if nama == "" or ukuran == "" or model == "" or medan not in pilihan_medan:
                        print("Nama, ukuran, model, dan pilihan medan harus diisi dengan benar!")
                    elif valid == False:
                        print("Kapasitas, harga, dan stok harus berupa angka!")
                    elif nilai[0] < 1 or nilai[1] < 1 or nilai[2] < 1:
                        print("Kapasitas, harga, dan stok harus lebih dari 0!")
                    else:
                        if no_tenda < 10:
                            kode_baru = "T0" + str(no_tenda)
                        else:
                            kode_baru = "T" + str(no_tenda)
                        tenda.append([kode_baru, nama, ukuran, model, pilihan_medan[medan], nilai[0], nilai[1], nilai[2]])
                        no_tenda = no_tenda + 1
                        print("Tenda berhasil ditambahkan dengan kode", kode_baru)
                    input("Tekan Enter untuk lanjut...")

                elif menu in ["3", "4"]:
                    os.system(bersih)
                    if len(tenda) == 0:
                        print("Belum ada data tenda.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    print("=== DAFTAR TENDA ===")
                    for i in range(len(tenda)):
                        t = tenda[i]
                        print(str(i + 1) + ". [" + t[0] + "] " + t[1] + " | " + t[4] + " | Rp " + str(t[6]) + "/hari | Stok: " + str(t[7]))
                    teks = input("Pilih nomor tenda: ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("Nomor tenda harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if int(teks) < 1 or int(teks) > len(tenda):
                        print("Nomor tenda tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    t = tenda[int(teks) - 1]
                    os.system(bersih)

                    if menu == "3":
                        print("=== UBAH TENDA:", t[1], "===")
                        nilai = []
                        valid = True
                        for lab in ["Harga baru per hari (Rp)", "Stok baru (unit)"]:
                            teks = input(lab + " : ").strip()
                            angka = True
                            for h in teks:
                                if h not in angka_valid:
                                    angka = False
                            if teks == "":
                                angka = False
                            if angka == False:
                                valid = False
                            else:
                                nilai.append(int(teks))
                        if valid == False:
                            print("Harga dan stok harus berupa angka!")
                        elif nilai[0] < 1:
                            print("Harga harus lebih dari 0!")
                        else:
                            t[6] = nilai[0]
                            t[7] = nilai[1]
                            print("Data tenda diperbarui.")
                        input("Tekan Enter untuk lanjut...")

                    else:
                        aktif = False
                        for s in sewa:
                            if s[2] == t[0] and s[9] in status_aktif:
                                aktif = True
                        if aktif:
                            print("Tenda tidak bisa dihapus: masih ada pesanan aktif.")
                        else:
                            yakin = input("Yakin hapus " + t[1] + "? (Y/T): ").strip().upper()
                            if yakin == "Y":
                                tenda.remove(t)
                                print("Tenda dihapus.")
                            elif yakin == "T":
                                print("Penghapusan dibatalkan.")
                            else:
                                print("Input harus Y atau T!")
                        input("Tekan Enter untuk lanjut...")

                elif menu in ["5", "6"]:
                    os.system(bersih)
                    if len(sewa) == 0:
                        print("Belum ada data penyewaan.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    print("=== JADWAL & DATA PENYEWAAN ===")
                    for i in range(len(sewa)):
                        s = sewa[i]
                        print(str(i + 1) + ". [ID " + str(s[0]) + "] " + s[3] + " x" + str(s[4]) + " unit | Pelanggan: " + s[1])
                        print("   Jadwal : mulai " + s[5] + " selama " + str(s[6]) + " hari")
                        print("   Biaya  : Rp", s[7], "| Terbayar: Rp", s[8])
                        print("   Status :", s[9], "| Denda: Rp", s[10])
                        print("-" * 50)
                    if menu == "5":
                        input("Tekan Enter untuk lanjut...")
                        continue
                    teks = input("Pilih nomor pesanan yang dikembalikan: ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("Nomor pesanan harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if int(teks) < 1 or int(teks) > len(sewa):
                        print("Nomor pesanan tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    s = sewa[int(teks) - 1]
                    os.system(bersih)
                    if s[9] != "Lunas":
                        print("Hanya pesanan berstatus Lunas yang dapat diproses pengembaliannya!")
                    else:
                        teks = input("Keterlambatan pengembalian (hari, isi 0 jika tepat waktu): ").strip()
                        angka = True
                        for h in teks:
                            if h not in angka_valid:
                                angka = False
                        if teks == "":
                            angka = False
                        if angka == False:
                            print("Keterlambatan harus berupa angka!")
                        else:
                            terlambat = int(teks)
                            # denda = 50% dari biaya sewa per hari, untuk tiap hari terlambat
                            denda = terlambat * (s[7] // s[6]) // 2
                            print("Keterlambatan :", terlambat, "hari")
                            print("Denda         : Rp", denda)
                            yakin = input("Proses pengembalian? (Y/T): ").strip().upper()
                            if yakin == "Y":
                                s[9] = "Dikembalikan"
                                s[10] = denda
                                for t in tenda:
                                    if t[0] == s[2]:
                                        t[7] = t[7] + s[4]
                                print("Tenda dikembalikan. Stok bertambah kembali.")
                            elif yakin == "T":
                                print("Pengembalian dibatalkan.")
                            else:
                                print("Input harus Y atau T!")
                    input("Tekan Enter untuk lanjut...")

              
                elif menu in ["7", "8"]:
                    os.system(bersih)
                    pelanggan = []
                    for u in pengguna:
                        if u[2] == "Pengguna Biasa":
                            pelanggan.append(u)
                    if len(pelanggan) == 0:
                        print("Belum ada data pelanggan.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    print("=== DATA PELANGGAN ===")
                    for i in range(len(pelanggan)):
                        print(str(i + 1) + ". " + pelanggan[i][3] + " | Username: " + pelanggan[i][0] + " | HP: " + pelanggan[i][4])
                    if menu == "7":
                        input("Tekan Enter untuk lanjut...")
                        continue
                    teks = input("Pilih nomor pelanggan yang dihapus: ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("Nomor pelanggan harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if int(teks) < 1 or int(teks) > len(pelanggan):
                        print("Nomor pelanggan tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    target = pelanggan[int(teks) - 1]
                    aktif = False
                    for s in sewa:
                        if s[1] == target[0] and s[9] in status_aktif:
                            aktif = True
                    if aktif:
                        print("Pelanggan tidak bisa dihapus: masih ada pesanan aktif.")
                    else:
                        yakin = input("Yakin hapus " + target[3] + "? (Y/T): ").strip().upper()
                        if yakin == "Y":
                            i = 0
                            while i < len(sewa):
                                if sewa[i][1] == target[0]:
                                    sewa.pop(i)
                                else:
                                    i = i + 1
                            pengguna.remove(target)
                            print("Pelanggan beserta riwayat sewanya dihapus.")
                        elif yakin == "T":
                            print("Penghapusan dibatalkan.")
                        else:
                            print("Input harus Y atau T!")
                    input("Tekan Enter untuk lanjut...")

                # ---------- 9. READ RIWAYAT PEMBAYARAN ----------
                elif menu == "9":
                    os.system(bersih)
                    print("=== RIWAYAT PEMBAYARAN ===")
                    if len(pembayaran) == 0:
                        print("Belum ada pembayaran.")
                    else:
                        jumlah = 0
                        for b in pembayaran:
                            print("[Bayar #" + str(b[0]) + "] Pesanan ID " + str(b[1]) + " | " + b[2] + " | " + b[4] + " | Rp " + str(b[3]))
                            jumlah = jumlah + b[3]
                        print("-" * 50)
                        print("Total pemasukan: Rp", jumlah)
                    input("Tekan Enter untuk lanjut...")

                else:
                    print("Menu tidak valid!")
                    input("Tekan Enter untuk lanjut...")


            else:

                if menu == "2":
                    os.system(bersih)
                    print("=== SEWA TENDA ===")
                    for t in tenda:
                        print("[" + t[0] + "] " + t[1] + " | " + t[4] + " | " + t[2] + " | " + str(t[5]) + " orang | Rp " + str(t[6]) + "/hari | Stok " + str(t[7]))
                    kode = input("Masukkan kode tenda (mis. T01): ").strip().upper()
                    pilih = None
                    for t in tenda:
                        if t[0] == kode:
                            pilih = t
                    if pilih is None:
                        print("Kode tenda tidak ditemukan!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    print("Jadwal sewa untuk", pilih[1])
                    nilai = []
                    valid = True
                    for lab in ["Tanggal mulai (1-31)", "Bulan mulai (1-12)", "Tahun mulai (mis. 2026)", "Lama sewa (hari, maks 30)", "Jumlah unit tenda"]:
                        teks = input(lab + " : ").strip()
                        angka = True
                        for h in teks:
                            if h not in angka_valid:
                                angka = False
                        if teks == "":
                            angka = False
                        if angka == False:
                            valid = False
                        else:
                            nilai.append(int(teks))
                    if valid == False:
                        print("Semua isian harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    hari = nilai[0]
                    bulan = nilai[1]
                    tahun = nilai[2]
                    lama = nilai[3]
                    jumlah = nilai[4]
                    # cek tanggal sederhana
                    tanggal_ok = True
                    if tahun < 2026 or tahun > 2100 or bulan < 1 or bulan > 12 or hari < 1 or hari > 31:
                        tanggal_ok = False
                    elif bulan in bulan_30 and hari > 30:
                        tanggal_ok = False
                    elif bulan == 2 and hari > 29:
                        tanggal_ok = False
                    if tanggal_ok == False:
                        print("Tanggal tidak valid!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if lama < 1 or lama > 30 or jumlah < 1:
                        print("Lama sewa harus 1-30 hari dan jumlah unit minimal 1!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if jumlah > pilih[7]:
                        print("Stok tidak cukup. Tersedia:", pilih[7], "unit.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    tgl_mulai = str(hari) + "-" + str(bulan) + "-" + str(tahun)
                    total = pilih[6] * jumlah * lama
                    print("-" * 50)
                    print("Tenda   :", pilih[1], "x", jumlah, "unit")
                    print("Jadwal  : mulai", tgl_mulai, "selama", lama, "hari")
                    print("Biaya   : Rp", total)
                    yakin = input("Konfirmasi pemesanan? (Y/T): ").strip().upper()
                    if yakin == "Y":
                        sewa.append([id_sewa, user_aktif[0], pilih[0], pilih[1], jumlah, tgl_mulai, lama, total, 0, "Dipesan", 0])
                        pilih[7] = pilih[7] - jumlah
                        print("Pesanan berhasil dibuat dengan ID", id_sewa, "- silakan lakukan pembayaran (DP minimal 30%).")
                        id_sewa = id_sewa + 1
                    elif yakin == "T":
                        print("Pemesanan dibatalkan.")
                    else:
                        print("Input harus Y atau T!")
                    input("Tekan Enter untuk lanjut...")

                elif menu in ["3", "4", "5", "6"]:
                    os.system(bersih)
                    saya = []
                    for s in sewa:
                        if s[1] == user_aktif[0]:
                            saya.append(s)
                    if len(saya) == 0:
                        print("Anda belum memiliki pesanan.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    print("=== PESANAN & JADWAL SAYA ===")
                    for i in range(len(saya)):
                        s = saya[i]
                        print(str(i + 1) + ". [ID " + str(s[0]) + "] " + s[3] + " x" + str(s[4]) + " unit")
                        print("   Jadwal : mulai " + s[5] + " selama " + str(s[6]) + " hari")
                        print("   Biaya  : Rp", s[7], "| Terbayar: Rp", s[8])
                        print("   Status :", s[9], "| Denda: Rp", s[10])
                        print("-" * 50)
                    if menu == "3":
                        input("Tekan Enter untuk lanjut...")
                        continue
                    teks = input("Pilih nomor pesanan: ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("Nomor pesanan harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if int(teks) < 1 or int(teks) > len(saya):
                        print("Nomor pesanan tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    s = saya[int(teks) - 1]
                    os.system(bersih)


                    if menu == "4":
                        if s[9] != "Dipesan" or s[8] > 0:
                            print("Pesanan hanya bisa diubah jika berstatus Dipesan dan belum ada pembayaran!")
                        else:
                            nilai = []
                            valid = True
                            for lab in ["Lama sewa baru (hari, maks 30)", "Jumlah unit baru"]:
                                teks = input(lab + " : ").strip()
                                angka = True
                                for h in teks:
                                    if h not in angka_valid:
                                        angka = False
                                if teks == "":
                                    angka = False
                                if angka == False:
                                    valid = False
                                else:
                                    nilai.append(int(teks))
                            if valid == False:
                                print("Lama sewa dan jumlah unit harus berupa angka!")
                            elif nilai[0] < 1 or nilai[0] > 30 or nilai[1] < 1:
                                print("Lama sewa harus 1-30 hari dan jumlah unit minimal 1!")
                            else:
                                lama_baru = nilai[0]
                                jumlah_baru = nilai[1]
                                for t in tenda:
                                    if t[0] == s[2]:
                                        if jumlah_baru > t[7] + s[4]:
                                            print("Stok tidak cukup. Tersedia:", t[7] + s[4], "unit.")
                                        else:
                                            harga = s[7] // (s[4] * s[6])
                                            t[7] = t[7] + s[4] - jumlah_baru
                                            s[4] = jumlah_baru
                                            s[6] = lama_baru
                                            s[7] = harga * jumlah_baru * lama_baru
                                            print("Pesanan diperbarui. Biaya baru: Rp", s[7])
                        input("Tekan Enter untuk lanjut...")

                  
                    elif menu == "5":
                        sisa = s[7] - s[8]
                        if s[9] != "Dipesan":
                            print("Pesanan ini tidak memerlukan pembayaran (status: " + s[9] + ").")
                        else:
                            minimal = s[7] * 30 // 100
                            print("Total biaya : Rp", s[7])
                            print("Terbayar    : Rp", s[8])
                            print("Sisa        : Rp", sisa)
                            if s[8] == 0:
                                print("DP minimal 30% : Rp", minimal)
                            teks = input("Nominal pembayaran (Rp): ").strip()
                            angka = True
                            for h in teks:
                                if h not in angka_valid:
                                    angka = False
                            if teks == "":
                                angka = False
                            print("Metode: 1. Tunai  2. Transfer  3. E-Wallet")
                            metode = input("Pilih metode (1-3): ").strip()
                            if angka == False:
                                print("Nominal harus berupa angka!")
                            elif int(teks) <= 0 or int(teks) > sisa:
                                print("Nominal harus lebih dari 0 dan tidak melebihi sisa tagihan!")
                            elif s[8] == 0 and int(teks) < minimal:
                                print("Pembayaran pertama minimal 30% dari total biaya!")
                            elif metode not in metode_bayar:
                                print("Metode pembayaran tidak valid!")
                            else:
                                pembayaran.append([id_bayar, s[0], user_aktif[0], int(teks), metode_bayar[metode]])
                                id_bayar = id_bayar + 1
                                s[8] = s[8] + int(teks)
                                if s[8] == s[7]:
                                    s[9] = "Lunas"
                                    print("Pembayaran diterima. Pesanan LUNAS.")
                                else:
                                    print("Pembayaran diterima. Sisa tagihan: Rp", s[7] - s[8])
                        input("Tekan Enter untuk lanjut...")


                    elif menu == "6":
                        if s[9] != "Dipesan":
                            print("Hanya pesanan berstatus Dipesan yang bisa dibatalkan!")
                        else:
                            if s[8] > 0:
                                print("PERHATIAN: DP yang sudah dibayar tidak dapat dikembalikan.")
                            yakin = input("Yakin batalkan pesanan ID " + str(s[0]) + "? (Y/T): ").strip().upper()
                            if yakin == "Y":
                                for t in tenda:
                                    if t[0] == s[2]:
                                        t[7] = t[7] + s[4]
                                sewa.remove(s)
                                print("Pesanan dibatalkan dan dihapus. Stok bertambah kembali.")
                            elif yakin == "T":
                                print("Pembatalan dibatalkan.")
                            else:
                                print("Input harus Y atau T!")
                        input("Tekan Enter untuk lanjut...")

                elif menu == "7":
                    os.system(bersih)
                    print("=== UBAH PROFIL ===")
                    print("Nama  :", user_aktif[3])
                    print("No. HP:", user_aktif[4])
                    nama_baru = input("Nama baru (Enter = tetap)     : ").strip()
                    teks = input("No. HP baru (Enter = tetap)  : ").strip()
                    pass_baru = input("Password baru (Enter = tetap): ").strip()
                    angka = True
                    for h in teks:
                        if h not in angka_valid:
                            angka = False
                    if teks != "" and (angka == False or len(teks) < 10 or len(teks) > 13):
                        print("No. HP harus berupa 10-13 digit angka! Perubahan dibatalkan.")
                    elif pass_baru != "" and len(pass_baru) < 4:
                        print("Password minimal 4 karakter! Perubahan dibatalkan.")
                    else:
                        if nama_baru != "":
                            user_aktif[3] = nama_baru
                        if teks != "":
                            user_aktif[4] = teks
                        if pass_baru != "":
                            user_aktif[1] = pass_baru
                        print("Profil diperbarui.")
                    input("Tekan Enter untuk lanjut...")

                else:
                    print("Menu tidak valid!")
                    input("Tekan Enter untuk lanjut...")

    elif pilih_awal == "3":
        print("Terima kasih!")
        break

    else:
        print("Menu tidak valid!")
        input("Tekan Enter untuk lanjut...")