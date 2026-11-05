"""Modul admin: kelola tenda, pelanggan, pengembalian, dan pembayaran."""
from data import tenda, sewa, pembayaran, pengguna, state, status_aktif, pilihan_medan
from tampilan import (tampil_daftar_tenda, tampil_pesanan, tampil_pelanggan,
                      tampil_pembayaran, tampil_ringkasan)
from utils import (judul, sukses, gagal, peringatan, rupiah, input_angka, konfirmasi,
                   jumlah_rekursif, hitung_denda)
from pelanggan import pilih_pesanan


def buat_kode_tenda():
    """Fungsi tanpa parameter: membuat kode tenda baru dari state no_tenda."""
    kode_baru = "T" + str(state["no_tenda"]).zfill(2)
    state["no_tenda"] += 1
    return kode_baru


def hitung_total_pemasukan():
    """Fungsi tanpa parameter: total pemasukan dari seluruh pembayaran (memakai rekursi)."""
    daftar_nominal = [pembayaran[i]["nominal"] for i in pembayaran]
    return jumlah_rekursif(daftar_nominal, 0)


def tambah_tenda():
    judul("TAMBAH TENDA")
    nama = input("Nama tenda                    : ").strip()
    ukuran = input("Ukuran (mis. 3 x 3 m (Kecil)): ").strip()
    model = input("Model/jenis tenda             : ").strip()
    medan = input("Medan (1=Pantai 2=Gunung 3=Umum): ").strip()
    if nama == "" or ukuran == "" or model == "" or medan not in pilihan_medan:
        gagal("Nama, ukuran, model, dan pilihan medan harus diisi dengan benar!")
        return
    kapasitas = input_angka("Kapasitas (orang)", 1, 1000)
    harga = input_angka("Harga sewa per hari (Rp)", 1, 100000000)
    stok = input_angka("Stok (unit)", 1, 10000)
    kode_baru = buat_kode_tenda()
    tenda[kode_baru] = {"nama": nama, "ukuran": ukuran, "model": model, "medan": pilihan_medan[medan],
                        "kapasitas": kapasitas, "harga": harga, "stok": stok}
    sukses("Tenda berhasil ditambahkan dengan kode " + kode_baru)


def pilih_tenda_admin():
    """Tampilkan daftar & minta kode tenda. Return kode atau None."""
    if len(tenda) == 0:
        peringatan("Belum ada data tenda.")
        return None
    tampil_daftar_tenda()
    kode_pilih = input("Masukkan kode tenda (mis. T01): ").strip().upper()
    try:
        tenda[kode_pilih]
        return kode_pilih
    except KeyError:
        gagal("Kode tenda tidak ditemukan!")
        return None


def ubah_tenda():
    kode_pilih = pilih_tenda_admin()
    if kode_pilih is None:
        return
    t = tenda[kode_pilih]
    judul("UBAH TENDA: " + t["nama"])
    t["harga"] = input_angka("Harga baru per hari (Rp)", 1, 100000000)
    t["stok"] = input_angka("Stok baru (unit)", 0, 10000)
    sukses("Data tenda diperbarui.")


def hapus_tenda():
    kode_pilih = pilih_tenda_admin()
    if kode_pilih is None:
        return
    for id_s in sewa:
        if sewa[id_s]["kode_tenda"] == kode_pilih and sewa[id_s]["status"] in status_aktif:
            gagal("Tenda tidak bisa dihapus: masih ada pesanan aktif.")
            return
    if konfirmasi("Yakin hapus " + tenda[kode_pilih]["nama"] + "?"):
        del tenda[kode_pilih]
        sukses("Tenda dihapus.")
    else:
        peringatan("Penghapusan dibatalkan.")


def lihat_sewa():
    judul("JADWAL & DATA PENYEWAAN")
    tampil_pesanan(None)


def proses_kembali():
    if len(sewa) == 0:
        peringatan("Belum ada data penyewaan.")
        return
    lihat_sewa()
    id_pilih = pilih_pesanan(None)
    if id_pilih is None:
        return
    s = sewa[id_pilih]
    if s["status"] != "Lunas":
        gagal("Hanya pesanan berstatus Lunas yang dapat diproses pengembaliannya!")
        return
    terlambat = input_angka("Keterlambatan pengembalian (hari, 0 jika tepat waktu)", 0, 365)
    denda = hitung_denda(s["total"], s["lama"], terlambat)
    tampil_ringkasan([("Keterlambatan", str(terlambat) + " hari"), ("Denda", rupiah(denda))])
    if konfirmasi("Proses pengembalian?"):
        s["status"] = "Dikembalikan"
        s["denda"] = denda
        if s["kode_tenda"] in tenda:
            tenda[s["kode_tenda"]]["stok"] += s["jumlah"]
        sukses("Tenda dikembalikan. Stok bertambah kembali.")
    else:
        peringatan("Pengembalian dibatalkan.")


def lihat_pelanggan():
    """Return jumlah pelanggan."""
    return tampil_pelanggan()


def hapus_pelanggan():
    if lihat_pelanggan() == 0:
        return
    target = input("Masukkan username pelanggan yang dihapus: ").strip()
    try:
        if pengguna[target]["peran"] != "Pengguna Biasa":
            raise KeyError(target)
    except KeyError:
        gagal("Pelanggan tidak ditemukan!")
        return
    for id_s in sewa:
        if sewa[id_s]["pelanggan"] == target and sewa[id_s]["status"] in status_aktif:
            gagal("Pelanggan tidak bisa dihapus: masih ada pesanan aktif.")
            return
    if konfirmasi("Yakin hapus " + pengguna[target]["nama"] + "?"):
        id_hapus = [i for i in sewa if sewa[i]["pelanggan"] == target]
        for i in id_hapus:
            del sewa[i]
        del pengguna[target]
        sukses("Pelanggan beserta riwayat sewanya dihapus.")
    else:
        peringatan("Penghapusan dibatalkan.")


def riwayat_bayar():
    judul("RIWAYAT PEMBAYARAN")
    if len(pembayaran) == 0:
        peringatan("Belum ada pembayaran.")
        return
    tampil_pembayaran()
    print("Total pemasukan:", rupiah(hitung_total_pemasukan()))
