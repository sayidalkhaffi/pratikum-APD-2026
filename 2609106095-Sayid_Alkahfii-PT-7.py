import os
import datetime

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

status_aktif = {"Dipesan", "Lunas"}
metode_bayar = {"1": "Tunai", "2": "Transfer", "3": "E-Wallet"}
pilihan_medan = {"1": "Pantai", "2": "Gunung", "3": "Umum"}


def buat_kode_tenda():
    """Fungsi tanpa parameter: membuat kode tenda baru dari variabel global no_tenda."""
    global no_tenda
    kode_baru = "T" + str(no_tenda).zfill(2)
    no_tenda += 1
    return kode_baru


def hitung_total_pemasukan():
    """Fungsi tanpa parameter: total pemasukan dari seluruh pembayaran (memakai rekursi)."""
    daftar_nominal = [pembayaran[i]["nominal"] for i in pembayaran]
    return jumlah_rekursif(daftar_nominal, 0)


def input_angka(label, minimum, maksimum):
    """Fungsi dengan parameter: meminta angka bulat sampai valid (error handling ValueError)."""
    while True:
        try:
            nilai = int(input(label + " : ").strip())
            if nilai < minimum or nilai > maksimum:
                raise ValueError("di luar rentang")
            return nilai
        except ValueError:
            print("Input harus berupa angka bulat antara", minimum, "dan", maksimum, "!")


def hitung_denda(total, lama, terlambat):
    """Fungsi dengan parameter: denda = 50% tarif harian per hari keterlambatan."""
    try:
        if lama < 1:
            raise ValueError("lama sewa tidak valid")
        tarif_harian = total // lama
        return terlambat * tarif_harian // 2
    except ValueError:
        print("Lama sewa tidak valid, denda dianggap 0.")
        return 0
    except TypeError:
        print("Total, lama sewa, dan keterlambatan harus berupa angka, denda dianggap 0.")
        return 0


def jumlah_rekursif(daftar, indeks):
    """Fungsi rekursif: menjumlahkan isi list dari indeks sampai akhir."""
    if indeks >= len(daftar):          # basis rekursi
        return 0
    return daftar[indeks] + jumlah_rekursif(daftar, indeks + 1)


def tunggu():
    """Prosedur: jeda sebelum lanjut."""
    input("Tekan Enter untuk lanjut...")


def tampil_katalog(cari):
    """Prosedur: menampilkan katalog tenda. cari = '' untuk semua medan."""
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
            tampil += 1
    if tampil == 0:
        print("Belum ada tenda untuk tampilan ini.")


def tampil_pesanan(pelanggan):
    """Prosedur: tampilkan pesanan. pelanggan=None untuk semua (admin). Mengembalikan jumlah via global tidak dipakai."""
    jumlah = 0
    for id_s in sewa:
        s = sewa[id_s]
        if pelanggan is None or s["pelanggan"] == pelanggan:
            print("[ID " + str(id_s) + "] " + s["nama_tenda"] + " x" + str(s["jumlah"]) + " unit | Pelanggan: " + s["pelanggan"])
            print("   Jadwal : mulai " + s["tgl_mulai"] + " selama " + str(s["lama"]) + " hari")
            print("   Biaya  : Rp", s["total"], "| Terbayar: Rp", s["terbayar"])
            print("   Status :", s["status"], "| Denda: Rp", s["denda"])
            print("-" * 50)
            jumlah += 1
    if jumlah == 0:
        print("Belum ada data pesanan.")


def konfirmasi(pesan):
    """Fungsi dengan parameter: True jika Y, False jika T (ulang sampai valid)."""
    while True:
        jawab = input(pesan + " (Y/T): ").strip().upper()
        if jawab == "Y":
            return True
        if jawab == "T":
            return False
        print("Input harus Y atau T!")


def pilih_pesanan(pelanggan):
    """Fungsi dengan parameter: minta ID pesanan, return ID atau None jika tidak ada."""
    try:
        id_pilih = int(input("Masukkan ID pesanan: ").strip())
        s = sewa[id_pilih]                       # bisa KeyError
        if pelanggan is not None and s["pelanggan"] != pelanggan:
            raise KeyError(id_pilih)
        return id_pilih
    except ValueError:
        print("ID pesanan harus berupa angka!")
    except KeyError:
        print("ID pesanan tidak ada!")
    return None


def register():
    global pengguna
    print("=== REGISTER PELANGGAN ===")
    username_baru = input("Username                : ").strip()
    password_baru = input("Password (min 4 karakter): ").strip()
    nama_baru = input("Nama lengkap            : ").strip()
    hp_baru = input("No. HP (10-13 digit)    : ").strip()
    sudah_ada = username_baru.lower() in [u.lower() for u in pengguna]
    if username_baru == "" or sudah_ada:
        print("Username kosong atau sudah dipakai!")
    elif len(password_baru) < 4:
        print("Password minimal 4 karakter!")
    elif nama_baru == "":
        print("Nama lengkap tidak boleh kosong!")
    elif not hp_baru.isdigit() or len(hp_baru) < 10 or len(hp_baru) > 13:
        print("No. HP harus berupa 10-13 digit angka!")
    else:
        pengguna[username_baru] = {"password": password_baru, "peran": "Pengguna Biasa", "nama": nama_baru, "hp": hp_baru}
        print("Register berhasil! Silakan login.")


def login():
    """Return username jika berhasil, None jika gagal 3 kali."""
    percobaan = 0
    while percobaan < 3:
        os.system(bersih)
        print("=== LOGIN ===")
        input_user = input("Username : ").strip()
        input_pass = input("Password : ").strip()
        try:
            if pengguna[input_user]["password"] == input_pass:
                return input_user
            raise KeyError("password salah")
        except KeyError:
            percobaan += 1
            print("Username/password salah! Sisa percobaan:", 3 - percobaan)
            tunggu()
    print("Login gagal 3 kali. Kembali ke menu awal.")
    return None


def ubah_profil():
    print("=== UBAH PROFIL ===")
    print("Nama  :", pengguna[user_aktif]["nama"])
    print("No. HP:", pengguna[user_aktif]["hp"])
    nama_baru = input("Nama baru (Enter = tetap)     : ").strip()
    hp_baru = input("No. HP baru (Enter = tetap)  : ").strip()
    pass_baru = input("Password baru (Enter = tetap): ").strip()
    if hp_baru != "" and (not hp_baru.isdigit() or len(hp_baru) < 10 or len(hp_baru) > 13):
        print("No. HP harus berupa 10-13 digit angka! Perubahan dibatalkan.")
    elif pass_baru != "" and len(pass_baru) < 4:
        print("Password minimal 4 karakter! Perubahan dibatalkan.")
    else:
        if nama_baru != "":
            pengguna[user_aktif]["nama"] = nama_baru
        if hp_baru != "":
            pengguna[user_aktif]["hp"] = hp_baru
        if pass_baru != "":
            pengguna[user_aktif]["password"] = pass_baru
        print("Profil diperbarui.")



    print("=== TAMBAH TENDA ===")
    nama = input("Nama tenda                    : ").strip()
    ukuran = input("Ukuran (mis. 3 x 3 m (Kecil)): ").strip()
    model = input("Model/jenis tenda             : ").strip()
    medan = input("Medan (1=Pantai 2=Gunung 3=Umum): ").strip()
    if nama == "" or ukuran == "" or model == "" or medan not in pilihan_medan:
        print("Nama, ukuran, model, dan pilihan medan harus diisi dengan benar!")
        return
    kapasitas = input_angka("Kapasitas (orang)", 1, 1000)
    harga = input_angka("Harga sewa per hari (Rp)", 1, 100000000)
    stok = input_angka("Stok (unit)", 1, 10000)
    kode_baru = buat_kode_tenda()
    tenda[kode_baru] = {"nama": nama, "ukuran": ukuran, "model": model, "medan": pilihan_medan[medan],
                        "kapasitas": kapasitas, "harga": harga, "stok": stok}
    print("Tenda berhasil ditambahkan dengan kode", kode_baru)


def pilih_tenda_admin():
    """Tampilkan daftar & minta kode tenda. Return kode atau None."""
    if len(tenda) == 0:
        print("Belum ada data tenda.")
        return None
    print("=== DAFTAR TENDA ===")
    for kode in tenda:
        t = tenda[kode]
        print("[" + kode + "] " + t["nama"] + " | " + t["medan"] + " | Rp " + str(t["harga"]) + "/hari | Stok: " + str(t["stok"]))
    kode_pilih = input("Masukkan kode tenda (mis. T01): ").strip().upper()
    try:
        tenda[kode_pilih]
        return kode_pilih
    except KeyError:
        print("Kode tenda tidak ditemukan!")
        return None


def ubah_tenda():
    kode_pilih = pilih_tenda_admin()
    if kode_pilih is None:
        return
    t = tenda[kode_pilih]
    print("=== UBAH TENDA:", t["nama"], "===")
    t["harga"] = input_angka("Harga baru per hari (Rp)", 1, 100000000)
    t["stok"] = input_angka("Stok baru (unit)", 0, 10000)
    print("Data tenda diperbarui.")


def hapus_tenda():
    kode_pilih = pilih_tenda_admin()
    if kode_pilih is None:
        return
    for id_s in sewa:
        if sewa[id_s]["kode_tenda"] == kode_pilih and sewa[id_s]["status"] in status_aktif:
            print("Tenda tidak bisa dihapus: masih ada pesanan aktif.")
            return
    if konfirmasi("Yakin hapus " + tenda[kode_pilih]["nama"] + "?"):
        del tenda[kode_pilih]
        print("Tenda dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def proses_kembali():
    if len(sewa) == 0:
        print("Belum ada data penyewaan.")
        return
    print("=== JADWAL & DATA PENYEWAAN ===")
    tampil_pesanan(None)
    id_pilih = pilih_pesanan(None)
    if id_pilih is None:
        return
    s = sewa[id_pilih]
    if s["status"] != "Lunas":
        print("Hanya pesanan berstatus Lunas yang dapat diproses pengembaliannya!")
        return
    terlambat = input_angka("Keterlambatan pengembalian (hari, 0 jika tepat waktu)", 0, 365)
    denda = hitung_denda(s["total"], s["lama"], terlambat)
    print("Keterlambatan :", terlambat, "hari")
    print("Denda         : Rp", denda)
    if konfirmasi("Proses pengembalian?"):
        s["status"] = "Dikembalikan"
        s["denda"] = denda
        if s["kode_tenda"] in tenda:
            tenda[s["kode_tenda"]]["stok"] += s["jumlah"]
        print("Tenda dikembalikan. Stok bertambah kembali.")
    else:
        print("Pengembalian dibatalkan.")


def lihat_pelanggan():
    """Return jumlah pelanggan."""
    jumlah_pelanggan = 0
    print("=== DATA PELANGGAN ===")
    for username in pengguna:
        if pengguna[username]["peran"] == "Pengguna Biasa":
            print("Username: " + username + " | " + pengguna[username]["nama"] + " | HP: " + pengguna[username]["hp"])
            jumlah_pelanggan += 1
    if jumlah_pelanggan == 0:
        print("Belum ada data pelanggan.")
    return jumlah_pelanggan


def hapus_pelanggan():
    if lihat_pelanggan() == 0:
        return
    target = input("Masukkan username pelanggan yang dihapus: ").strip()
    try:
        if pengguna[target]["peran"] != "Pengguna Biasa":
            raise KeyError(target)
    except KeyError:
        print("Pelanggan tidak ditemukan!")
        return
    for id_s in sewa:
        if sewa[id_s]["pelanggan"] == target and sewa[id_s]["status"] in status_aktif:
            print("Pelanggan tidak bisa dihapus: masih ada pesanan aktif.")
            return
    if konfirmasi("Yakin hapus " + pengguna[target]["nama"] + "?"):
        id_hapus = [i for i in sewa if sewa[i]["pelanggan"] == target]
        for i in id_hapus:
            del sewa[i]
        del pengguna[target]
        print("Pelanggan beserta riwayat sewanya dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def riwayat_bayar():
    print("=== RIWAYAT PEMBAYARAN ===")
    if len(pembayaran) == 0:
        print("Belum ada pembayaran.")
        return
    for id_b in pembayaran:
        b = pembayaran[id_b]
        print("[Bayar #" + str(id_b) + "] Pesanan ID " + str(b["id_sewa"]) + " | " + b["pelanggan"] + " | " + b["metode"] + " | Rp " + str(b["nominal"]))
    print("-" * 50)
    print("Total pemasukan: Rp", hitung_total_pemasukan())



def sewa_tenda():
    global id_sewa
    print("=== SEWA TENDA ===")
    for kode in tenda:
        t = tenda[kode]
        print("[" + kode + "] " + t["nama"] + " | " + t["medan"] + " | " + t["ukuran"] + " | " + str(t["kapasitas"]) + " orang | Rp " + str(t["harga"]) + "/hari | Stok " + str(t["stok"]))
    kode_pilih = input("Masukkan kode tenda (mis. T01): ").strip().upper()
    try:
        pilih = tenda[kode_pilih]
    except KeyError:
        print("Kode tenda tidak ditemukan!")
        return
    print("Jadwal sewa untuk", pilih["nama"])
    hari = input_angka("Tanggal mulai (1-31)", 1, 31)
    bulan = input_angka("Bulan mulai (1-12)", 1, 12)
    tahun = input_angka("Tahun mulai (mis. 2026)", 2026, 2100)
    try:
        tanggal = datetime.date(tahun, bulan, hari)     
    except ValueError:
        print("Tanggal tidak valid!")
        return
    lama = input_angka("Lama sewa (hari, maks 30)", 1, 30)
    jumlah = input_angka("Jumlah unit tenda", 1, 10000)
    if jumlah > pilih["stok"]:
        print("Stok tidak cukup. Tersedia:", pilih["stok"], "unit.")
        return
    tgl_mulai = str(tanggal.day) + "-" + str(tanggal.month) + "-" + str(tanggal.year)
    total = pilih["harga"] * jumlah * lama
    print("-" * 50)
    print("Tenda   :", pilih["nama"], "x", jumlah, "unit")
    print("Jadwal  : mulai", tgl_mulai, "selama", lama, "hari")
    print("Biaya   : Rp", total)
    if konfirmasi("Konfirmasi pemesanan?"):
        sewa[id_sewa] = {"pelanggan": user_aktif, "kode_tenda": kode_pilih, "nama_tenda": pilih["nama"],
                         "jumlah": jumlah, "tgl_mulai": tgl_mulai, "lama": lama, "total": total,
                         "terbayar": 0, "status": "Dipesan", "denda": 0}
        pilih["stok"] -= jumlah
        print("Pesanan berhasil dibuat dengan ID", id_sewa, "- silakan lakukan pembayaran (DP minimal 30%).")
        id_sewa += 1
    else:
        print("Pemesanan dibatalkan.")


def ubah_pesanan(id_pilih):
    s = sewa[id_pilih]
    if s["status"] != "Dipesan" or s["terbayar"] > 0:
        print("Pesanan hanya bisa diubah jika berstatus Dipesan dan belum ada pembayaran!")
        return
    lama_baru = input_angka("Lama sewa baru (hari, maks 30)", 1, 30)
    jumlah_baru = input_angka("Jumlah unit baru", 1, 10000)
    t = tenda[s["kode_tenda"]]
    if jumlah_baru > t["stok"] + s["jumlah"]:
        print("Stok tidak cukup. Tersedia:", t["stok"] + s["jumlah"], "unit.")
        return
    try:
        if s["jumlah"] * s["lama"] < 1:
            raise ValueError("data pesanan rusak")
        harga = s["total"] // (s["jumlah"] * s["lama"])
    except ValueError:
        print("Data pesanan rusak, perubahan dibatalkan.")
        return
    t["stok"] = t["stok"] + s["jumlah"] - jumlah_baru
    s["jumlah"] = jumlah_baru
    s["lama"] = lama_baru
    s["total"] = harga * jumlah_baru * lama_baru
    print("Pesanan diperbarui. Biaya baru: Rp", s["total"])


def bayar_pesanan(id_pilih):
    global id_bayar
    s = sewa[id_pilih]
    if s["status"] != "Dipesan":
        print("Pesanan ini tidak memerlukan pembayaran (status: " + s["status"] + ").")
        return
    sisa = s["total"] - s["terbayar"]
    minimal = s["total"] * 30 // 100
    print("Total biaya : Rp", s["total"])
    print("Terbayar    : Rp", s["terbayar"])
    print("Sisa        : Rp", sisa)
    if s["terbayar"] == 0:
        print("DP minimal 30% : Rp", minimal)
    try:
        nominal = int(input("Nominal pembayaran (Rp): ").strip())
    except ValueError:
        print("Nominal harus berupa angka!")
        return
    print("Metode: 1. Tunai  2. Transfer  3. E-Wallet")
    metode = input("Pilih metode (1-3): ").strip()
    if nominal <= 0 or nominal > sisa:
        print("Nominal harus lebih dari 0 dan tidak melebihi sisa tagihan!")
    elif s["terbayar"] == 0 and nominal < minimal:
        print("Pembayaran pertama minimal 30% dari total biaya!")
    elif metode not in metode_bayar:
        print("Metode pembayaran tidak valid!")
    else:
        pembayaran[id_bayar] = {"id_sewa": id_pilih, "pelanggan": user_aktif, "nominal": nominal, "metode": metode_bayar[metode]}
        id_bayar += 1
        s["terbayar"] += nominal
        if s["terbayar"] == s["total"]:
            s["status"] = "Lunas"
            print("Pembayaran diterima. Pesanan LUNAS.")
        else:
            print("Pembayaran diterima. Sisa tagihan: Rp", s["total"] - s["terbayar"])


def batal_pesanan(id_pilih):
    s = sewa[id_pilih]
    if s["status"] != "Dipesan":
        print("Hanya pesanan berstatus Dipesan yang bisa dibatalkan!")
        return
    if s["terbayar"] > 0:
        print("PERHATIAN: DP yang sudah dibayar tidak dapat dikembalikan.")
    if konfirmasi("Yakin batalkan pesanan ID " + str(id_pilih) + "?"):
        if s["kode_tenda"] in tenda:
            tenda[s["kode_tenda"]]["stok"] += s["jumlah"]
        del sewa[id_pilih]
        print("Pesanan dibatalkan dan dihapus. Stok bertambah kembali.")
    else:
        print("Pembatalan dibatalkan.")


def menu_pesanan_pengguna(menu):
    """Menu 3-6 pengguna: lihat/ubah/bayar/batal pesanan."""
    print("=== PESANAN & JADWAL SAYA ===")
    tampil_pesanan(user_aktif)
    punya = any(sewa[i]["pelanggan"] == user_aktif for i in sewa)
    if not punya or menu == "3":
        return
    id_pilih = pilih_pesanan(user_aktif)
    if id_pilih is None:
        return
    os.system(bersih)
    if menu == "4":
        ubah_pesanan(id_pilih)
    elif menu == "5":
        bayar_pesanan(id_pilih)
    else:
        batal_pesanan(id_pilih)



def menu_katalog():
    print("=== KATALOG TENDA ===")
    print("1. Semua medan")
    print("2. Medan Pantai")
    print("3. Medan Gunung")
    pilihan = input("Pilih tampilan (1-3): ").strip()
    daftar_medan = ["", "Pantai", "Gunung"]
    try:
        cari = daftar_medan[int(pilihan) - 1]     
        if int(pilihan) < 1:
            raise IndexError("indeks negatif")
    except (ValueError, IndexError):
        print("Pilihan tidak valid!")
        return
    os.system(bersih)
    tampil_katalog(cari)


def jalankan_menu_admin(menu):
    os.system(bersih)
    if menu == "2":
        tambah_tenda()
    elif menu == "3":
        ubah_tenda()
    elif menu == "4":
        hapus_tenda()
    elif menu == "5":
        print("=== JADWAL & DATA PENYEWAAN ===")
        tampil_pesanan(None)
    elif menu == "6":
        proses_kembali()
    elif menu == "7":
        lihat_pelanggan()
    elif menu == "8":
        hapus_pelanggan()
    elif menu == "9":
        riwayat_bayar()
    else:
        print("Menu tidak valid!")


def jalankan_menu_pengguna(menu):
    os.system(bersih)
    if menu == "2":
        sewa_tenda()
    elif menu in ["3", "4", "5", "6"]:
        menu_pesanan_pengguna(menu)
    elif menu == "7":
        ubah_profil()
    else:
        print("Menu tidak valid!")


def menu_setelah_login():
    global user_aktif
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

        if menu == "0":
            user_aktif = None
            print("Berhasil logout.")
        elif menu == "1":
            os.system(bersih)
            menu_katalog()
        elif peran == "Admin":
            jalankan_menu_admin(menu)
        else:
            jalankan_menu_pengguna(menu)
        tunggu()



def main():
    global user_aktif
    while True:
        try:
            os.system(bersih)
            print("=" * 50)
            print("          SISTEM SEWA TENDA")
            print("   Pantai | Gunung | Pernikahan | Pesta")
            print("=" * 50)
            print("1. Login")
            print("2. Register")
            print("3. Keluar")
            pilih_awal = input("Pilih menu (1-3): ").strip()

            if pilih_awal == "1":
                user_aktif = login()
                if user_aktif is None:
                    tunggu()
                else:
                    menu_setelah_login()
            elif pilih_awal == "2":
                os.system(bersih)
                register()
                tunggu()
            elif pilih_awal == "3":
                print("Terima kasih!")
                break
            else:
                print("Menu tidak valid!")
                tunggu()
        except (KeyError, ValueError, TypeError, IndexError):
            print("Terjadi kesalahan pada data atau input, kembali ke menu awal.")
            tunggu()


main()