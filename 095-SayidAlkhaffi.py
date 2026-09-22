merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000

biaya_bungkus_kado = 7500

# Total harga dihitung manual (tanpa sum())
total_harga = (merchandise_1 + merchandise_2 + merchandise_3 +
               merchandise_4 + merchandise_5 + merchandise_6 +
               biaya_bungkus_kado)

# Rata-rata (boleh pakai len())
daftar_merchandise = [merchandise_1, merchandise_2, merchandise_3,
                       merchandise_4, merchandise_5, merchandise_6]
rata_rata = total_harga / len(daftar_merchandise)

nim = 95

bolean = nim > rata_rata

print("Total Harga:", total_harga)
print("Rata-rata:", rata_rata)
print("NIM:", nim)
print("Boolean (nim > rata_rata):", bolean)