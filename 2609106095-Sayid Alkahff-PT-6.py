import os
bersih = "cls" if os.name == "nt" else "clear"
pengguna = {
    "admin": {"password": "admin123", "peran": "Admin", "nama": "Administrator", "hp": "0812544567961"},
    "sayid": {"password": "domeng", "peran": "Pengguna Biasa", "nama": "Sayid Alkaffi", "hp": "081234567890"},
}

tenda = {
    "T01": {"nama": "Kanopi Pantai", "ukuran": "3 x 3 m (Kecil)", "model": "Kanopi atap anti-UV, tanpa dinding", "medan": "Pantai", "kapasitas": 6, "harga": 75000, "stok": 8},
    "T02": {"nama": "Pop-up Beach Shelter", "ukuran": "2 x 2 m (Kecil)", "model": "Pop-up lipat, anti-UV, ventilasi", "medan": "Pantai", "kapasitas": 3, "harga": 50000, "stok": 10},
    "T03": {"nama": "Gazebo Pantai", "ukuran": "4 x 4 m (Sedang)", "model": "Gazebo rangka besi, tahan angin laut", "medan": "Pantai", "kapasitas": 12, "harga": 150000, "stok": 5},
    "T04": {"nama": "Tenda Pesta Pantai", "ukuran": "5 x 10 m (Besar)", "model": "Tenda pesta/pernikahan, rangka aluminium anti karat", "medan": "Pantai", "kapasitas": 60, "harga": 600000, "stok": 3},
    "T05": {"nama": "Dome 2P", "ukuran": "2 x 1,5 m (Kecil)", "model": "Dome double layer, ringan", "medan": "Gunung", "kapasitas": 2, "harga": 40000, "stok": 12},
    "T06": {"nama": "Dome 4P", "ukuran": "2,4 x 2,4 m (Sedang)", "model": "Dome double layer, waterproof 3000 mm", "medan": "Gunung", "kapasitas": 4, "harga": 70000, "stok": 10},
    "T07": {"nama": "Tunnel 6P", "ukuran": "4 x 2,5 m (Sedang)", "model": "Tunnel 2 kamar, tahan angin kencang", "medan": "Gunung", "kapasitas": 6, "harga": 110000, "stok": 6},
    "T08": {"nama": "Basecamp 12P", "ukuran": "4 x 5 m (Besar)", "model": "Tenda basecamp/rombongan, flysheet tebal", "medan": "Gunung", "kapasitas": 12, "harga": 220000, "stok": 4},
}


sewa = {}

pembayaran = {}

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
            if u.lower() == username_baru.lower():
                sudah_ada = True
        angka = True
        for huruf in teks:
            if huruf not in angka_valid:
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
            pengguna[username_baru] = {"password": password_baru, "peran": "Pengguna Biasa", "nama": nama_baru, "hp": teks}
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
            if input_user in pengguna:
                if pengguna[input_user]["password"] == input_pass:
                    user_aktif = input_user
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
            peran = pengguna[user_aktif]["peran"]
            print("=" * 50)
            print("Login sebagai:", pengguna[user_aktif]["nama"], "(" + peran + ")")
            print("=" * 50)
            print("1. Lihat katalog tenda")
            if peran == "Admin":
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
                for kode in tenda:
                    t = tenda[kode]
                    if cari == "" or t["medan"] == cari or t["medan"] == "Umum":
                        print("[" + kode + "] " + t["nama"] + "   (Medan: " + t["medan"] + ")")
                        print("    Ukuran    :", t["ukuran"])
                        print("    Model     :", t["model"])
                        print("    Kapasitas :", t["kapasitas"], "orang")
                        print("    Harga     : Rp", t["harga"], "/ hari")
                        print("    Stok      :", t["stok"], "unit")
                        print("-" * 50)
                        tampil = tampil + 1
                if tampil == 0:
                    print("Belum ada tenda untuk tampilan ini.")
                input("Tekan Enter untuk lanjut...")

            elif menu == "0":
                user_aktif = None
                print("Berhasil logout.")
                input("Tekan Enter untuk lanjut...")

     
            elif peran == "Admin":

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
                        for huruf in teks:
                            if huruf not in angka_valid:
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
                        tenda[kode_baru] = {"nama": nama, "ukuran": ukuran, "model": model, "medan": pilihan_medan[medan], "kapasitas": nilai[0], "harga": nilai[1], "stok": nilai[2]}
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
                    for kode in tenda:
                        t = tenda[kode]
                        print("[" + kode + "] " + t["nama"] + " | " + t["medan"] + " | Rp " + str(t["harga"]) + "/hari | Stok: " + str(t["stok"]))
                    kode_pilih = input("Masukkan kode tenda (mis. T01): ").strip().upper()
                    if kode_pilih not in tenda:
                        print("Kode tenda tidak ditemukan!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    t = tenda[kode_pilih]
                    os.system(bersih)

                    if menu == "3":
                        print("=== UBAH TENDA:", t["nama"], "===")
                        nilai = []
                        valid = True
                        for lab in ["Harga baru per hari (Rp)", "Stok baru (unit)"]:
                            teks = input(lab + " : ").strip()
                            angka = True
                            for huruf in teks:
                                if huruf not in angka_valid:
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
                            t["harga"] = nilai[0]
                            t["stok"] = nilai[1]
                            print("Data tenda diperbarui.")
                        input("Tekan Enter untuk lanjut...")

                    else:
                        aktif = False
                        for id_s in sewa:
                            if sewa[id_s]["kode_tenda"] == kode_pilih and sewa[id_s]["status"] in status_aktif:
                                aktif = True
                        if aktif:
                            print("Tenda tidak bisa dihapus: masih ada pesanan aktif.")
                        else:
                            yakin = input("Yakin hapus " + t["nama"] + "? (Y/T): ").strip().upper()
                            if yakin == "Y":
                                del tenda[kode_pilih]
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
                    for id_s in sewa:
                        s = sewa[id_s]
                        print("[ID " + str(id_s) + "] " + s["nama_tenda"] + " x" + str(s["jumlah"]) + " unit | Pelanggan: " + s["pelanggan"])
                        print("   Jadwal : mulai " + s["tgl_mulai"] + " selama " + str(s["lama"]) + " hari")
                        print("   Biaya  : Rp", s["total"], "| Terbayar: Rp", s["terbayar"])
                        print("   Status :", s["status"], "| Denda: Rp", s["denda"])
                        print("-" * 50)
                    if menu == "5":
                        input("Tekan Enter untuk lanjut...")
                        continue
                    teks = input("Masukkan ID pesanan yang dikembalikan: ").strip()
                    angka = True
                    for huruf in teks:
                        if huruf not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("ID pesanan harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if int(teks) not in sewa:
                        print("ID pesanan tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    id_pilih = int(teks)
                    s = sewa[id_pilih]
                    os.system(bersih)
                    if s["status"] != "Lunas":
                        print("Hanya pesanan berstatus Lunas yang dapat diproses pengembaliannya!")
                    else:
                        teks = input("Keterlambatan pengembalian (hari, isi 0 jika tepat waktu): ").strip()
                        angka = True
                        for huruf in teks:
                            if huruf not in angka_valid:
                                angka = False
                        if teks == "":
                            angka = False
                        if angka == False:
                            print("Keterlambatan harus berupa angka!")
                        else:
                            terlambat = int(teks)
                         
                            denda = terlambat * (s["total"] // s["lama"]) // 2
                            print("Keterlambatan :", terlambat, "hari")
                            print("Denda         : Rp", denda)
                            yakin = input("Proses pengembalian? (Y/T): ").strip().upper()
                            if yakin == "Y":
                                s["status"] = "Dikembalikan"
                                s["denda"] = denda
                                if s["kode_tenda"] in tenda:
                                    tenda[s["kode_tenda"]]["stok"] = tenda[s["kode_tenda"]]["stok"] + s["jumlah"]
                                print("Tenda dikembalikan. Stok bertambah kembali.")
                            elif yakin == "T":
                                print("Pengembalian dibatalkan.")
                            else:
                                print("Input harus Y atau T!")
                    input("Tekan Enter untuk lanjut...")

                elif menu in ["7", "8"]:
                    os.system(bersih)
                    jumlah_pelanggan = 0
                    print("=== DATA PELANGGAN ===")
                    for username in pengguna:
                        if pengguna[username]["peran"] == "Pengguna Biasa":
                            print("Username: " + username + " | " + pengguna[username]["nama"] + " | HP: " + pengguna[username]["hp"])
                            jumlah_pelanggan = jumlah_pelanggan + 1
                    if jumlah_pelanggan == 0:
                        print("Belum ada data pelanggan.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if menu == "7":
                        input("Tekan Enter untuk lanjut...")
                        continue
                    target = input("Masukkan username pelanggan yang dihapus: ").strip()
                    if target not in pengguna or pengguna[target]["peran"] != "Pengguna Biasa":
                        print("Pelanggan tidak ditemukan!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    aktif = False
                    for id_s in sewa:
                        if sewa[id_s]["pelanggan"] == target and sewa[id_s]["status"] in status_aktif:
                            aktif = True
                    if aktif:
                        print("Pelanggan tidak bisa dihapus: masih ada pesanan aktif.")
                    else:
                        yakin = input("Yakin hapus " + pengguna[target]["nama"] + "? (Y/T): ").strip().upper()
                        if yakin == "Y":
                            id_hapus = []
                            for id_s in sewa:
                                if sewa[id_s]["pelanggan"] == target:
                                    id_hapus.append(id_s)
                            for id_s in id_hapus:
                                del sewa[id_s]
                            del pengguna[target]
                            print("Pelanggan beserta riwayat sewanya dihapus.")
                        elif yakin == "T":
                            print("Penghapusan dibatalkan.")
                        else:
                            print("Input harus Y atau T!")
                    input("Tekan Enter untuk lanjut...")

              
                elif menu == "9":
                    os.system(bersih)
                    print("=== RIWAYAT PEMBAYARAN ===")
                    if len(pembayaran) == 0:
                        print("Belum ada pembayaran.")
                    else:
                        jumlah = 0
                        for id_b in pembayaran:
                            b = pembayaran[id_b]
                            print("[Bayar #" + str(id_b) + "] Pesanan ID " + str(b["id_sewa"]) + " | " + b["pelanggan"] + " | " + b["metode"] + " | Rp " + str(b["nominal"]))
                            jumlah = jumlah + b["nominal"]
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
                    for kode in tenda:
                        t = tenda[kode]
                        print("[" + kode + "] " + t["nama"] + " | " + t["medan"] + " | " + t["ukuran"] + " | " + str(t["kapasitas"]) + " orang | Rp " + str(t["harga"]) + "/hari | Stok " + str(t["stok"]))
                    kode_pilih = input("Masukkan kode tenda (mis. T01): ").strip().upper()
                    if kode_pilih not in tenda:
                        print("Kode tenda tidak ditemukan!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    pilih = tenda[kode_pilih]
                    print("Jadwal sewa untuk", pilih["nama"])
                    nilai = []
                    valid = True
                    for lab in ["Tanggal mulai (1-31)", "Bulan mulai (1-12)", "Tahun mulai (mis. 2026)", "Lama sewa (hari, maks 30)", "Jumlah unit tenda"]:
                        teks = input(lab + " : ").strip()
                        angka = True
                        for huruf in teks:
                            if huruf not in angka_valid:
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
                    if jumlah > pilih["stok"]:
                        print("Stok tidak cukup. Tersedia:", pilih["stok"], "unit.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    tgl_mulai = str(hari) + "-" + str(bulan) + "-" + str(tahun)
                    total = pilih["harga"] * jumlah * lama
                    print("-" * 50)
                    print("Tenda   :", pilih["nama"], "x", jumlah, "unit")
                    print("Jadwal  : mulai", tgl_mulai, "selama", lama, "hari")
                    print("Biaya   : Rp", total)
                    yakin = input("Konfirmasi pemesanan? (Y/T): ").strip().upper()
                    if yakin == "Y":
                        sewa[id_sewa] = {
                            "pelanggan": user_aktif,
                            "kode_tenda": kode_pilih,
                            "nama_tenda": pilih["nama"],
                            "jumlah": jumlah,
                            "tgl_mulai": tgl_mulai,
                            "lama": lama,
                            "total": total,
                            "terbayar": 0,
                            "status": "Dipesan",
                            "denda": 0,
                        }
                        pilih["stok"] = pilih["stok"] - jumlah
                        print("Pesanan berhasil dibuat dengan ID", id_sewa, "- silakan lakukan pembayaran (DP minimal 30%).")
                        id_sewa = id_sewa + 1
                    elif yakin == "T":
                        print("Pemesanan dibatalkan.")
                    else:
                        print("Input harus Y atau T!")
                    input("Tekan Enter untuk lanjut...")

               
                elif menu in ["3", "4", "5", "6"]:
                    os.system(bersih)
                    jumlah_pesanan = 0
                    print("=== PESANAN & JADWAL SAYA ===")
                    for id_s in sewa:
                        s = sewa[id_s]
                        if s["pelanggan"] == user_aktif:
                            print("[ID " + str(id_s) + "] " + s["nama_tenda"] + " x" + str(s["jumlah"]) + " unit")
                            print("   Jadwal : mulai " + s["tgl_mulai"] + " selama " + str(s["lama"]) + " hari")
                            print("   Biaya  : Rp", s["total"], "| Terbayar: Rp", s["terbayar"])
                            print("   Status :", s["status"], "| Denda: Rp", s["denda"])
                            print("-" * 50)
                            jumlah_pesanan = jumlah_pesanan + 1
                    if jumlah_pesanan == 0:
                        print("Anda belum memiliki pesanan.")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if menu == "3":
                        input("Tekan Enter untuk lanjut...")
                        continue
                    teks = input("Masukkan ID pesanan: ").strip()
                    angka = True
                    for huruf in teks:
                        if huruf not in angka_valid:
                            angka = False
                    if teks == "":
                        angka = False
                    if angka == False:
                        print("ID pesanan harus berupa angka!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    if int(teks) not in sewa:
                        print("ID pesanan tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    id_pilih = int(teks)
                    s = sewa[id_pilih]
                    if s["pelanggan"] != user_aktif:
                        print("ID pesanan tidak ada!")
                        input("Tekan Enter untuk lanjut...")
                        continue
                    os.system(bersih)

              
                    if menu == "4":
                        if s["status"] != "Dipesan" or s["terbayar"] > 0:
                            print("Pesanan hanya bisa diubah jika berstatus Dipesan dan belum ada pembayaran!")
                        else:
                            nilai = []
                            valid = True
                            for lab in ["Lama sewa baru (hari, maks 30)", "Jumlah unit baru"]:
                                teks = input(lab + " : ").strip()
                                angka = True
                                for huruf in teks:
                                    if huruf not in angka_valid:
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
                                t = tenda[s["kode_tenda"]]
                                if jumlah_baru > t["stok"] + s["jumlah"]:
                                    print("Stok tidak cukup. Tersedia:", t["stok"] + s["jumlah"], "unit.")
                                else:
                                    harga = s["total"] // (s["jumlah"] * s["lama"])
                                    t["stok"] = t["stok"] + s["jumlah"] - jumlah_baru
                                    s["jumlah"] = jumlah_baru
                                    s["lama"] = lama_baru
                                    s["total"] = harga * jumlah_baru * lama_baru
                                    print("Pesanan diperbarui. Biaya baru: Rp", s["total"])
                        input("Tekan Enter untuk lanjut...")

                    elif menu == "5":
                        sisa = s["total"] - s["terbayar"]
                        if s["status"] != "Dipesan":
                            print("Pesanan ini tidak memerlukan pembayaran (status: " + s["status"] + ").")
                        else:
                            minimal = s["total"] * 30 // 100
                            print("Total biaya : Rp", s["total"])
                            print("Terbayar    : Rp", s["terbayar"])
                            print("Sisa        : Rp", sisa)
                            if s["terbayar"] == 0:
                                print("DP minimal 30% : Rp", minimal)
                            teks = input("Nominal pembayaran (Rp): ").strip()
                            angka = True
                            for huruf in teks:
                                if huruf not in angka_valid:
                                    angka = False
                            if teks == "":
                                angka = False
                            print("Metode: 1. Tunai  2. Transfer  3. E-Wallet")
                            metode = input("Pilih metode (1-3): ").strip()
                            if angka == False:
                                print("Nominal harus berupa angka!")
                            elif int(teks) <= 0 or int(teks) > sisa:
                                print("Nominal harus lebih dari 0 dan tidak melebihi sisa tagihan!")
                            elif s["terbayar"] == 0 and int(teks) < minimal:
                                print("Pembayaran pertama minimal 30% dari total biaya!")
                            elif metode not in metode_bayar:
                                print("Metode pembayaran tidak valid!")
                            else:
                                pembayaran[id_bayar] = {"id_sewa": id_pilih, "pelanggan": user_aktif, "nominal": int(teks), "metode": metode_bayar[metode]}
                                id_bayar = id_bayar + 1
                                s["terbayar"] = s["terbayar"] + int(teks)
                                if s["terbayar"] == s["total"]:
                                    s["status"] = "Lunas"
                                    print("Pembayaran diterima. Pesanan LUNAS.")
                                else:
                                    print("Pembayaran diterima. Sisa tagihan: Rp", s["total"] - s["terbayar"])
                        input("Tekan Enter untuk lanjut...")

            
                    elif menu == "6":
                        if s["status"] != "Dipesan":
                            print("Hanya pesanan berstatus Dipesan yang bisa dibatalkan!")
                        else:
                            if s["terbayar"] > 0:
                                print("PERHATIAN: DP yang sudah dibayar tidak dapat dikembalikan.")
                            yakin = input("Yakin batalkan pesanan ID " + str(id_pilih) + "? (Y/T): ").strip().upper()
                            if yakin == "Y":
                                tenda[s["kode_tenda"]]["stok"] = tenda[s["kode_tenda"]]["stok"] + s["jumlah"]
                                del sewa[id_pilih]
                                print("Pesanan dibatalkan dan dihapus. Stok bertambah kembali.")
                            elif yakin == "T":
                                print("Pembatalan dibatalkan.")
                            else:
                                print("Input harus Y atau T!")
                        input("Tekan Enter untuk lanjut...")

          
                elif menu == "7":
                    os.system(bersih)
                    print("=== UBAH PROFIL ===")
                    print("Nama  :", pengguna[user_aktif]["nama"])
                    print("No. HP:", pengguna[user_aktif]["hp"])
                    nama_baru = input("Nama baru (Enter = tetap)     : ").strip()
                    teks = input("No. HP baru (Enter = tetap)  : ").strip()
                    pass_baru = input("Password baru (Enter = tetap): ").strip()
                    angka = True
                    for huruf in teks:
                        if huruf not in angka_valid:
                            angka = False
                    if teks != "" and (angka == False or len(teks) < 10 or len(teks) > 13):
                        print("No. HP harus berupa 10-13 digit angka! Perubahan dibatalkan.")
                    elif pass_baru != "" and len(pass_baru) < 4:
                        print("Password minimal 4 karakter! Perubahan dibatalkan.")
                    else:
                        if nama_baru != "":
                            pengguna[user_aktif]["nama"] = nama_baru
                        if teks != "":
                            pengguna[user_aktif]["hp"] = teks
                        if pass_baru != "":
                            pengguna[user_aktif]["password"] = pass_baru
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