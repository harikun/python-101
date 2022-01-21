# semua sintaksis dasar bahasa pemrograman terdiri dari:
# 1. Sekuensial: langkah berurutan
# 2. Percabangan: langkah melompat jika kondisi terpenuhi
# 3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi

# Sekuensial
# print("Hello World!")
# print("Ibu berkata, \"Pergi ke Toko!\"")
# print("Budy menjawab, \"Baik, apa yang harus saya lakukan di toko?!\"")
# print("Ibu menjawab, \"Beli satu botol susu, dan jika ada telor beli beli 6?\"")
# print("maka budi berangkat ke toko")
# print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 173
jumlah_telor = 1587
print(f"Jumlah botol susu: {jumlah_botol_susu} botol")
print(f"Jumlah telur: {jumlah_telor} butir")

if jumlah_botol_susu > 0:
 print("Budi mengecek harganya, dan ternyata uangnya cukup")
 if jumlah_telor == 0:
  print("Budi membeli 1 botol susu")
 else:
  print("Budi membeli 6 botol sus")
else :
 print("Budi tidak membeli botol susu")

print("Budi Pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")