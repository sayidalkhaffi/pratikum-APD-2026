"""Titik masuk program Sistem Sewa Tenda. Jalankan dengan: python main.py"""
from data import state
from utils import bersihkan, tunggu, judul, gagal
from tampilan import tampil_menu
import auth
import menu


def main():
    while True:
        try:
            bersihkan()
            judul("SISTEM SEWA TENDA")
            print("Pantai | Gunung | Pernikahan | Pesta")
            tampil_menu([("1", "Login"), ("2", "Register"), ("3", "Keluar")])
            pilih_awal = input("Pilih menu (1-3): ").strip()

            if pilih_awal == "1":
                state["user_aktif"] = auth.login()
                if state["user_aktif"] is None:
                    tunggu()
                else:
                    menu.menu_setelah_login()
            elif pilih_awal == "2":
                bersihkan()
                auth.register()
                tunggu()
            elif pilih_awal == "3":
                print("Terima kasih!")
                break
            else:
                gagal("Menu tidak valid!")
                tunggu()
        except (KeyError, ValueError, TypeError, IndexError):
            gagal("Terjadi kesalahan pada data atau input, kembali ke menu awal.")
            tunggu()


if __name__ == "__main__":
    main()
