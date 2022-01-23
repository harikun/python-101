# list is array and dictionary is JSON
# book_list = [ 1, -23, 'Seven Habits', 'How to Influence People', 'First Thinfs First']
# print(book_list)

# for book in book_list:
#   print(book)
# book_list.append('The Power of Habit')

# for i in range(0, len(book_list)):
#   print(book_list[i])

# clear() delte all element in list
# book_list.clear()
# print(book_list)

books = ['The Power of Habit', 'Seven Habits', 'How to Influence People', 'First Thinfs First']
books[0] = 'The Power of Habit (2nd Edition)'
for i in range(0, len(books)):
  print(books[i])
# pop() remove from the end and return the value that was removed
print('\n Remove the last item')
book_removed = books.pop()
for i in range(0, len(books)):
  print(books[i])
print(f'\n Removed book: {book_removed}')

#list comprehension
fiction_book = ["Harry Potter", "Lord of the Rings", "The Hobbit"]
# tanda kurung kurawal artinya start dan end [start:end]
del fiction_book[:]
for i in range(0, len(fiction_book)):
  print(fiction_book[i])
# tanda kurung kurawal artinya start dan end [start:end:step]
non_fiction_book = ["The Power of Habit", "Seven Habits", "How to Influence People", "First Thinfs First", "The 4-Hour Workweek"]
del non_fiction_book[::2]
for i in range(0, len(non_fiction_book)):
  print(non_fiction_book[i])



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
# jumlah_botol_susu = 173
# jumlah_telor = 1587
# print(f"Jumlah botol susu: {jumlah_botol_susu} botol")
# print(f"Jumlah telur: {jumlah_telor} butir")

# if jumlah_botol_susu > 0:
#  print("Budi mengecek harganya, dan ternyata uangnya cukup")
#  if jumlah_telor == 0:
#   print("Budi membeli 1 botol susu")
#  else:
#   print("Budi membeli 6 botol sus")
# else :
#  print("Budi tidak membeli botol susu")

# print("Budi Pulang ke rumah")
# print("Menyampaikan hasilnya kepada ibu")

#                     Perulangan
#       perulangan di python hanya for & while

# for perulangan yang jelas berapa jumlah perulangannya
# while tidak jelas berapa kali akan diulang tapi jelas kapan selesainya
# perulangan dengan FOR LOOP
# jumlah_buku = 10
# print('ibu berkata, "Baca semua bukumu!"')

# jumlah_buku_sudah_dibaca = 0
# print(f'jumlah buku yang sudah dibaca {jumlah_buku_sudah_dibaca}')

# for jumlah_buku_sudah_dibaca in range(1, jumlah_buku+1):
#  print(f"Buku ke {jumlah_buku_sudah_dibaca} sudah dibaca")

# print(f'jumlah buku yang sudah dibaca {jumlah_buku_sudah_dibaca}')

#perulangan dengan WHILE LOOP
# jumlah_buku = 10
# print('ibu berkata, "Baca semua bukumu!"')

# jumlah_buku_sudah_dibaca = 0
# print(f'jumlah buku yang sudah dibaca {jumlah_buku_sudah_dibaca}')

# while jumlah_buku_sudah_dibaca < jumlah_buku:
#   jumlah_buku_sudah_dibaca += 1
#   print(f"Buku ke {jumlah_buku_sudah_dibaca} sudah dibaca")

# print(f'jumlah buku yang sudah dibaca {jumlah_buku_sudah_dibaca}')

#perulangan dengan WHILE LOOP sampai paham
# jumlah_buku = 10
# print('ibu berkata, "Baca semua bukumu!"')
# total_jumlah_baca = 0
# jumlah_buku_sudah_dibaca_dan_dipahami = 0
# print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_sudah_dibaca_dan_dipahami}')

# while total_jumlah_baca < jumlah_buku * 2:
#     total_jumlah_baca = total_jumlah_baca + 1
#     if jumlah_buku_sudah_dibaca_dan_dipahami == 9:
#       print(f"buku ke {jumlah_buku_sudah_dibaca_dan_dipahami + 1} belum paham")
#     else:
#       jumlah_buku_sudah_dibaca_dan_dipahami += 1
#       print(f"Buku ke {jumlah_buku_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")
# if jumlah_buku_sudah_dibaca_dan_dipahami == jumlah_buku:
#   print("Buku sudah selesai dibaca dan dipahami")
# else:
#   print(f"tidak semua buku bisa dipahami. Budi hanya bisa memahami {jumlah_buku_sudah_dibaca_dan_dipahami} buku")
# print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_sudah_dibaca_dan_dipahami}')