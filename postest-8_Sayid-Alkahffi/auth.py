"""Modul autentikasi: register, login, dan ubah profil."""
from data import pengguna, state
from utils import (bersihkan, tunggu, judul, sukses, gagal, input_password)


def register():
    judul("REGISTER PELANGGAN")
    username_baru = input("Username                : ").strip()
    password_baru = input_password("Password (min 4 karakter): ")
    nama_baru = input("Nama lengkap            : ").strip()
    hp_baru = input("No. HP (10-13 digit)    : ").strip()
    sudah_ada = username_baru.lower() in [u.lower() for u in pengguna]
    if username_baru == "" or sudah_ada:
        gagal("Username kosong atau sudah dipakai!")
    elif len(password_baru) < 4:
        gagal("Password minimal 4 karakter!")
    elif nama_baru == "":
        gagal("Nama lengkap tidak boleh kosong!")
    elif not hp_baru.isdigit() or len(hp_baru) < 10 or len(hp_baru) > 13:
        gagal("No. HP harus berupa 10-13 digit angka!")
    else:
        pengguna[username_baru] = {"password": password_baru, "peran": "Pengguna Biasa",
                                   "nama": nama_baru, "hp": hp_baru}
        sukses("Register berhasil! Silakan login.")


def login():
    """Return username jika berhasil, None jika gagal 3 kali."""
    percobaan = 0
    while percobaan < 3:
        bersihkan()
        judul("LOGIN")
        input_user = input("Username : ").strip()
        input_pass = input_password("Password : ")
        try:
            if pengguna[input_user]["password"] == input_pass:
                return input_user
            raise KeyError("password salah")
        except KeyError:
            percobaan += 1
            gagal("Username/password salah! Sisa percobaan: " + str(3 - percobaan))
            tunggu()
    gagal("Login gagal 3 kali. Kembali ke menu awal.")
    return None


def ubah_profil():
    user = state["user_aktif"]
    judul("UBAH PROFIL")
    print("Nama  :", pengguna[user]["nama"])
    print("No. HP:", pengguna[user]["hp"])
    nama_baru = input("Nama baru (Enter = tetap)     : ").strip()
    hp_baru = input("No. HP baru (Enter = tetap)  : ").strip()
    pass_baru = input_password("Password baru (Enter = tetap): ")
    if hp_baru != "" and (not hp_baru.isdigit() or len(hp_baru) < 10 or len(hp_baru) > 13):
        gagal("No. HP harus berupa 10-13 digit angka! Perubahan dibatalkan.")
    elif pass_baru != "" and len(pass_baru) < 4:
        gagal("Password minimal 4 karakter! Perubahan dibatalkan.")
    else:
        if nama_baru != "":
            pengguna[user]["nama"] = nama_baru
        if hp_baru != "":
            pengguna[user]["hp"] = hp_baru
        if pass_baru != "":
            pengguna[user]["password"] = pass_baru
        sukses("Profil diperbarui.")
