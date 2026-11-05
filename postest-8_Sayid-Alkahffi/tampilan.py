"""Modul tampilan: semua output tabel memakai library prettytable."""
from prettytable import PrettyTable

from data import tenda, sewa, pembayaran, pengguna
from utils import rupiah, judul, peringatan


def _buat_tabel(kolom, rata_kiri=()):
    """Fungsi dengan parameter: membuat PrettyTable dengan nama kolom; kolom lain rata tengah."""
    tabel = PrettyTable()
    tabel.field_names = kolom
    for k in kolom:
        tabel.align[k] = "l" if k in rata_kiri else "c"
    return tabel


def tampil_katalog(cari):
    """Prosedur: menampilkan katalog tenda. cari = '' untuk semua medan."""
    judul("KATALOG TENDA")
    tabel = _buat_tabel(["Kode", "Nama", "Medan", "Ukuran", "Model", "Kapasitas", "Harga/Hari", "Stok"],
                        rata_kiri=("Nama", "Ukuran", "Model"))
    for kode in tenda:
        t = tenda[kode]
        if cari == "" or t["medan"] == cari or t["medan"] == "Umum":
            tabel.add_row([kode, t["nama"], t["medan"], t["ukuran"], t["model"],
                           str(t["kapasitas"]) + " orang", rupiah(t["harga"]), str(t["stok"]) + " unit"])
    if len(tabel.rows) == 0:
        peringatan("Belum ada tenda untuk tampilan ini.")
    else:
        print(tabel)


def tampil_daftar_tenda():
    """Prosedur: tabel ringkas daftar tenda (untuk memilih kode tenda)."""
    judul("DAFTAR TENDA")
    tabel = _buat_tabel(["Kode", "Nama", "Medan", "Ukuran", "Kapasitas", "Harga/Hari", "Stok"],
                        rata_kiri=("Nama", "Ukuran"))
    for kode in tenda:
        t = tenda[kode]
        tabel.add_row([kode, t["nama"], t["medan"], t["ukuran"],
                       str(t["kapasitas"]) + " orang", rupiah(t["harga"]), t["stok"]])
    print(tabel)


def tampil_pesanan(pelanggan):
    """Prosedur: tampilkan pesanan. pelanggan=None untuk semua (admin)."""
    tabel = _buat_tabel(["ID", "Pelanggan", "Tenda", "Unit", "Mulai", "Lama", "Biaya", "Terbayar", "Status", "Denda"],
                        rata_kiri=("Pelanggan", "Tenda"))
    for id_s in sewa:
        s = sewa[id_s]
        if pelanggan is None or s["pelanggan"] == pelanggan:
            tabel.add_row([id_s, s["pelanggan"], s["nama_tenda"], s["jumlah"], s["tgl_mulai"],
                           str(s["lama"]) + " hari", rupiah(s["total"]), rupiah(s["terbayar"]),
                           s["status"], rupiah(s["denda"])])
    if len(tabel.rows) == 0:
        peringatan("Belum ada data pesanan.")
    else:
        print(tabel)


def tampil_pelanggan():
    """Fungsi: tabel pelanggan. Mengembalikan jumlah pelanggan."""
    judul("DATA PELANGGAN")
    tabel = _buat_tabel(["Username", "Nama", "No. HP"], rata_kiri=("Username", "Nama"))
    for username in pengguna:
        if pengguna[username]["peran"] == "Pengguna Biasa":
            tabel.add_row([username, pengguna[username]["nama"], pengguna[username]["hp"]])
    if len(tabel.rows) == 0:
        peringatan("Belum ada data pelanggan.")
    else:
        print(tabel)
    return len(tabel.rows)


def tampil_pembayaran():
    """Prosedur: tabel riwayat pembayaran."""
    tabel = _buat_tabel(["No. Bayar", "ID Pesanan", "Pelanggan", "Metode", "Nominal"], rata_kiri=("Pelanggan",))
    for id_b in pembayaran:
        b = pembayaran[id_b]
        tabel.add_row([id_b, b["id_sewa"], b["pelanggan"], b["metode"], rupiah(b["nominal"])])
    print(tabel)


def tampil_ringkasan(daftar_baris):
    """Prosedur: tabel ringkasan dua kolom (Keterangan | Nilai)."""
    tabel = _buat_tabel(["Keterangan", "Nilai"], rata_kiri=("Keterangan", "Nilai"))
    for ket, nilai in daftar_baris:
        tabel.add_row([ket, nilai])
    print(tabel)


def tampil_menu(daftar_menu):
    """Prosedur: tabel menu. daftar_menu = list of (nomor, teks)."""
    tabel = _buat_tabel(["No", "Menu"], rata_kiri=("Menu",))
    for nomor, teks in daftar_menu:
        tabel.add_row([nomor, teks])
    print(tabel)
