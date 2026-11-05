"""Modul data: penyimpanan data program dan state global (dipakai bersama oleh semua modul)."""
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

# State yang berubah-ubah disimpan dalam dict agar bisa dimodifikasi dari modul lain
# (variabel global biasa tidak bisa di-assign lintas modul).
state = {
    "id_sewa": 1,
    "id_bayar": 1,
    "no_tenda": 9,
    "user_aktif": None,
}

status_aktif = {"Dipesan", "Lunas"}
metode_bayar = {"1": "Tunai", "2": "Transfer", "3": "E-Wallet"}
pilihan_medan = {"1": "Pantai", "2": "Gunung", "3": "Umum"}
