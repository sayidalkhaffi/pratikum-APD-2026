"""Modul utilitas: fungsi bantu umum (input, validasi, hitung, tampilan pesan berwarna)."""
import os

import pwinput                                   # library tambahan: input password tersamarkan
from colorama import Fore, init                  # library tambahan: warna teks terminal

init(autoreset=True)

BERSIH = "cls" if os.name == "nt" else "clear"


def bersihkan():
    """Prosedur: membersihkan layar terminal."""
    os.system(BERSIH)


def tunggu():
    """Prosedur: jeda sebelum lanjut."""
    input("Tekan Enter untuk lanjut...")


def sukses(pesan):
    print(Fore.GREEN + pesan)


def gagal(pesan):
    print(Fore.RED + pesan)


def peringatan(pesan):
    print(Fore.YELLOW + pesan)


def judul(teks):
    print(Fore.CYAN + "=== " + teks + " ===")


def rupiah(nilai):
    """Fungsi dengan parameter: format angka menjadi Rp 1.000.000."""
    return "Rp " + f"{nilai:,}".replace(",", ".")


def input_password(label):
    """Fungsi dengan parameter: input password dengan tampilan bintang (*)."""
    return pwinput.pwinput(prompt=label, mask="*").strip()


def input_angka(label, minimum, maksimum):
    """Fungsi dengan parameter: meminta angka bulat sampai valid (error handling ValueError)."""
    while True:
        try:
            nilai = int(input(label + " : ").strip())
            if nilai < minimum or nilai > maksimum:
                raise ValueError("di luar rentang")
            return nilai
        except ValueError:
            gagal("Input harus berupa angka bulat antara " + str(minimum) + " dan " + str(maksimum) + "!")


def konfirmasi(pesan):
    """Fungsi dengan parameter: True jika Y, False jika T (ulang sampai valid)."""
    while True:
        jawab = input(pesan + " (Y/T): ").strip().upper()
        if jawab == "Y":
            return True
        if jawab == "T":
            return False
        gagal("Input harus Y atau T!")


def jumlah_rekursif(daftar, indeks):
    """Fungsi rekursif: menjumlahkan isi list dari indeks sampai akhir."""
    if indeks >= len(daftar):          # basis rekursi
        return 0
    return daftar[indeks] + jumlah_rekursif(daftar, indeks + 1)


def hitung_denda(total, lama, terlambat):
    """Fungsi dengan parameter: denda = 50% tarif harian per hari keterlambatan."""
    try:
        if lama < 1:
            raise ValueError("lama sewa tidak valid")
        tarif_harian = total // lama
        return terlambat * tarif_harian // 2
    except ValueError:
        gagal("Lama sewa tidak valid, denda dianggap 0.")
        return 0
    except TypeError:
        gagal("Total, lama sewa, dan keterlambatan harus berupa angka, denda dianggap 0.")
        return 0
