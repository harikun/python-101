# earth quake detection
from bs4 import BeautifulSoup
# beautiful soup hanya mengolah data tidak mengambil
def data_extraction():

  """
  Date: 23 Januari 2022,
  Time: 12:20:13 WIB
  Magnitude: 3.8
  Deep: 9 km
  Location: LS=7.41 LS BT: 121.87
  epicenter: Pusat gempa berada di laut 139 km Barat Laut Maumere
  feel: Dirasakan (Skala MMI): II Pulau Kalaotoa
  """
  soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
  print(soup.prettify())

  hasil = dict()
  hasil['date'] = '23 Januari 2022'
  hasil['time'] = '12:20:13 WIB'
  hasil['magnitude'] = 3.8
  hasil['deep'] = '9 km'
  hasil['location'] = {'LS':7.41, 'BT': 121.87}
  hasil['epicenter'] = 'Pusat gempa berada di laut 139 km Barat Laut Maumere'
  hasil['feel'] = 'Dirasakan (Skala MMI): II Pulau Kalaotoa'
  return hasil


def show_data(result):
  print("Gempa terakhir yang terjadi di Indonesia")
  print("======================================")
  print(f"Tanggal: {result['date']}")
  print(f"Jam: {result['time']}")
  print(f"Magnitude: {result['magnitude']}")
  print(f"Lokasi: {result['location']['LS']} LS {result['location']['BT']} BT")
  print(f"Kedalaman: {result['deep']}")
  print(f"Epicentern: {result['epicenter']}")
  print(f"Dirasakan: {result['feel']}")


# if __name__ == '__main__':
print("Main Aplication")
result = data_extraction()
print(result)
show_data(result)