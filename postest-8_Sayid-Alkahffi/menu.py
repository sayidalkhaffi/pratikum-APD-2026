"""Modul menu: navigasi menu admin dan pengguna setelah login."""
from data import pengguna, state
from tampilan import tampil_katalog, tampil_menu
from utils import bersihkan, tunggu, judul, sukses, gagal
import admin
import auth
import pelanggan


def menu_katalog():
    judul("KATALOG TENDA")
    tampil_menu([("1", "Semua medan"), ("2", "Medan Pantai"), ("3", "Medan Gunung")])
    pilihan = input("Pilih tampilan (1-3): ").strip()
    daftar_medan = ["", "Pantai", "Gunung"]
    try:
        cari = daftar_medan[int(pilihan) - 1]
        if int(pilihan) < 1:
            raise IndexError("indeks negatif")
    except (ValueError, IndexError):
        gagal("Pilihan tidak valid!")
        return
    bersihkan()
    tampil_katalog(cari)


def jalankan_menu_admin(menu):
    bersihkan()
    if menu == "2":
        admin.tambah_tenda()
    elif menu == "3":
        admin.ubah_tenda()
    elif menu == "4":
        admin.hapus_tenda()
    elif menu == "5":
        admin.lihat_sewa()
    elif menu == "6":
        admin.proses_kembali()
    elif menu == "7":
        admin.lihat_pelanggan()
    elif menu == "8":
        admin.hapus_pelanggan()
    elif menu == "9":
        admin.riwayat_bayar()
    else:
        gagal("Menu tidak valid!")


def jalankan_menu_pengguna(menu):
    bersihkan()
    if menu == "2":
        pelanggan.sewa_tenda()
    elif menu in ["3", "4", "5", "6"]:
        pelanggan.menu_pesanan_pengguna(menu)
    elif menu == "7":
        auth.ubah_profil()
    else:
        gagal("Menu tidak valid!")


def menu_setelah_login():
    while state["user_aktif"] is not None:
        bersihkan()
        user = state["user_aktif"]
        peran = pengguna[user]["peran"]
        judul("Login sebagai: " + pengguna[user]["nama"] + " (" + peran + ")")
        daftar = [("1", "Lihat katalog tenda")]
        if peran == "Admin":
            daftar += [("2", "Tambah tenda"), ("3", "Ubah data tenda (harga/stok)"), ("4", "Hapus tenda"),
                       ("5", "Lihat jadwal & data penyewaan"), ("6", "Proses pengembalian tenda"),
                       ("7", "Lihat data pelanggan"), ("8", "Hapus pelanggan"), ("9", "Riwayat pembayaran")]
        else:
            daftar += [("2", "Sewa tenda"), ("3", "Lihat pesanan & jadwal saya"),
                       ("4", "Ubah pesanan (lama sewa/jumlah)"), ("5", "Bayar pesanan"),
                       ("6", "Batalkan pesanan"), ("7", "Ubah profil")]
        daftar.append(("0", "Logout"))
        tampil_menu(daftar)
        menu = input("Pilih menu: ").strip()

        if menu == "0":
            state["user_aktif"] = None
            sukses("Berhasil logout.")
        elif menu == "1":
            bersihkan()
            menu_katalog()
        elif peran == "Admin":
            jalankan_menu_admin(menu)
        else:
            jalankan_menu_pengguna(menu)
        tunggu()
