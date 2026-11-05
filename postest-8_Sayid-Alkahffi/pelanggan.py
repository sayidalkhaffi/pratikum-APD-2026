"""Modul pelanggan: sewa, ubah, bayar, dan batalkan pesanan."""
import datetime

from data import tenda, sewa, pembayaran, state, metode_bayar
from tampilan import tampil_daftar_tenda, tampil_pesanan, tampil_ringkasan
from utils import (bersihkan, judul, sukses, gagal, peringatan, rupiah, input_angka, konfirmasi)


def pilih_pesanan(pelanggan):
    """Fungsi dengan parameter: minta ID pesanan, return ID atau None jika tidak ada."""
    try:
        id_pilih = int(input("Masukkan ID pesanan: ").strip())
        s = sewa[id_pilih]                       # bisa KeyError
        if pelanggan is not None and s["pelanggan"] != pelanggan:
            raise KeyError(id_pilih)
        return id_pilih
    except ValueError:
        gagal("ID pesanan harus berupa angka!")
    except KeyError:
        gagal("ID pesanan tidak ada!")
    return None


def sewa_tenda():
    judul("SEWA TENDA")
    tampil_daftar_tenda()
    kode_pilih = input("Masukkan kode tenda (mis. T01): ").strip().upper()
    try:
        pilih = tenda[kode_pilih]
    except KeyError:
        gagal("Kode tenda tidak ditemukan!")
        return
    print("Jadwal sewa untuk", pilih["nama"])
    hari = input_angka("Tanggal mulai (1-31)", 1, 31)
    bulan = input_angka("Bulan mulai (1-12)", 1, 12)
    tahun = input_angka("Tahun mulai (mis. 2026)", 2026, 2100)
    try:
        tanggal = datetime.date(tahun, bulan, hari)
    except ValueError:
        gagal("Tanggal tidak valid!")
        return
    lama = input_angka("Lama sewa (hari, maks 30)", 1, 30)
    jumlah = input_angka("Jumlah unit tenda", 1, 10000)
    if jumlah > pilih["stok"]:
        gagal("Stok tidak cukup. Tersedia: " + str(pilih["stok"]) + " unit.")
        return
    tgl_mulai = str(tanggal.day) + "-" + str(tanggal.month) + "-" + str(tanggal.year)
    total = pilih["harga"] * jumlah * lama
    tampil_ringkasan([("Tenda", pilih["nama"] + " x " + str(jumlah) + " unit"),
                      ("Jadwal", "mulai " + tgl_mulai + " selama " + str(lama) + " hari"),
                      ("Biaya", rupiah(total))])
    if konfirmasi("Konfirmasi pemesanan?"):
        id_baru = state["id_sewa"]
        sewa[id_baru] = {"pelanggan": state["user_aktif"], "kode_tenda": kode_pilih, "nama_tenda": pilih["nama"],
                         "jumlah": jumlah, "tgl_mulai": tgl_mulai, "lama": lama, "total": total,
                         "terbayar": 0, "status": "Dipesan", "denda": 0}
        pilih["stok"] -= jumlah
        sukses("Pesanan berhasil dibuat dengan ID " + str(id_baru) + " - silakan lakukan pembayaran (DP minimal 30%).")
        state["id_sewa"] += 1
    else:
        peringatan("Pemesanan dibatalkan.")


def ubah_pesanan(id_pilih):
    s = sewa[id_pilih]
    if s["status"] != "Dipesan" or s["terbayar"] > 0:
        gagal("Pesanan hanya bisa diubah jika berstatus Dipesan dan belum ada pembayaran!")
        return
    lama_baru = input_angka("Lama sewa baru (hari, maks 30)", 1, 30)
    jumlah_baru = input_angka("Jumlah unit baru", 1, 10000)
    t = tenda[s["kode_tenda"]]
    if jumlah_baru > t["stok"] + s["jumlah"]:
        gagal("Stok tidak cukup. Tersedia: " + str(t["stok"] + s["jumlah"]) + " unit.")
        return
    try:
        if s["jumlah"] * s["lama"] < 1:
            raise ValueError("data pesanan rusak")
        harga = s["total"] // (s["jumlah"] * s["lama"])
    except ValueError:
        gagal("Data pesanan rusak, perubahan dibatalkan.")
        return
    t["stok"] = t["stok"] + s["jumlah"] - jumlah_baru
    s["jumlah"] = jumlah_baru
    s["lama"] = lama_baru
    s["total"] = harga * jumlah_baru * lama_baru
    sukses("Pesanan diperbarui. Biaya baru: " + rupiah(s["total"]))


def bayar_pesanan(id_pilih):
    s = sewa[id_pilih]
    if s["status"] != "Dipesan":
        gagal("Pesanan ini tidak memerlukan pembayaran (status: " + s["status"] + ").")
        return
    sisa = s["total"] - s["terbayar"]
    minimal = s["total"] * 30 // 100
    baris = [("Total biaya", rupiah(s["total"])), ("Terbayar", rupiah(s["terbayar"])), ("Sisa", rupiah(sisa))]
    if s["terbayar"] == 0:
        baris.append(("DP minimal 30%", rupiah(minimal)))
    tampil_ringkasan(baris)
    try:
        nominal = int(input("Nominal pembayaran (Rp): ").strip())
    except ValueError:
        gagal("Nominal harus berupa angka!")
        return
    print("Metode: 1. Tunai  2. Transfer  3. E-Wallet")
    metode = input("Pilih metode (1-3): ").strip()
    if nominal <= 0 or nominal > sisa:
        gagal("Nominal harus lebih dari 0 dan tidak melebihi sisa tagihan!")
    elif s["terbayar"] == 0 and nominal < minimal:
        gagal("Pembayaran pertama minimal 30% dari total biaya!")
    elif metode not in metode_bayar:
        gagal("Metode pembayaran tidak valid!")
    else:
        id_b = state["id_bayar"]
        pembayaran[id_b] = {"id_sewa": id_pilih, "pelanggan": state["user_aktif"],
                            "nominal": nominal, "metode": metode_bayar[metode]}
        state["id_bayar"] += 1
        s["terbayar"] += nominal
        if s["terbayar"] == s["total"]:
            s["status"] = "Lunas"
            sukses("Pembayaran diterima. Pesanan LUNAS.")
        else:
            sukses("Pembayaran diterima. Sisa tagihan: " + rupiah(s["total"] - s["terbayar"]))


def batal_pesanan(id_pilih):
    s = sewa[id_pilih]
    if s["status"] != "Dipesan":
        gagal("Hanya pesanan berstatus Dipesan yang bisa dibatalkan!")
        return
    if s["terbayar"] > 0:
        peringatan("PERHATIAN: DP yang sudah dibayar tidak dapat dikembalikan.")
    if konfirmasi("Yakin batalkan pesanan ID " + str(id_pilih) + "?"):
        if s["kode_tenda"] in tenda:
            tenda[s["kode_tenda"]]["stok"] += s["jumlah"]
        del sewa[id_pilih]
        sukses("Pesanan dibatalkan dan dihapus. Stok bertambah kembali.")
    else:
        peringatan("Pembatalan dibatalkan.")


def menu_pesanan_pengguna(menu):
    """Menu 3-6 pengguna: lihat/ubah/bayar/batal pesanan."""
    user = state["user_aktif"]
    judul("PESANAN & JADWAL SAYA")
    tampil_pesanan(user)
    punya = any(sewa[i]["pelanggan"] == user for i in sewa)
    if not punya or menu == "3":
        return
    id_pilih = pilih_pesanan(user)
    if id_pilih is None:
        return
    bersihkan()
    if menu == "4":
        ubah_pesanan(id_pilih)
    elif menu == "5":
        bayar_pesanan(id_pilih)
    else:
        batal_pesanan(id_pilih)
