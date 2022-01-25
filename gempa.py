# earth quake detection
from bs4 import BeautifulSoup
# beautiful soup hanya mengolah data tidak mengambil
import requests
# request untuk mengambil data dari website
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
  try:
    content = requests.get("https://www.bmkg.go.id/")
  except Exception:
    print("Tidak dapat mengambil data")
    return None
  if content.status_code == 200:
    soup = BeautifulSoup(content.text, 'html.parser')
    dateFull = soup.find('span', {'class': 'waktu'}).text
    date = dateFull.split(', ')[1]
    time = dateFull.split(', ')[0]
    alldata = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
    alldata = alldata.findChildren('li')

    magnitude = None
    deep = None
    ls = None
    bt = None
    epicenter = None
    feel = None

    i = 0
    for data in alldata:
      print(i, data)
      if i == 1:
        magnitude = data.text
      elif i == 2:
        deep = data.text
      elif i == 3:
        location = data.text.split(' - ')
        ls = location[0]
        bt = location[1]
      elif i == 4:
        epicenter = data.text
      elif i == 5:
        feel = data.text
      i += 1

    hasil = dict()
    hasil['date'] = date
    hasil['time'] = time
    hasil['magnitude'] = magnitude
    hasil['deep'] = deep
    hasil['location'] = {'LS':ls, 'BT': bt}
    hasil['epicenter'] = epicenter
    hasil['feel'] = feel
    return hasil
  else:
    print("Tidak dapat mengambil data")
    return None


def show_data(result):
  if result is None:
    print("Tidak dapat mengambil data")
    return
  print("Gempa terakhir yang terjadi di Indonesia")
  print("======================================")
  print(f"Tanggal: {result['date']}")
  print(f"Jam: {result['time']}")
  print(f"Magnitude: {result['magnitude']}")
  print(f"Lokasi: {result['location']['LS']}, {result['location']['BT']}")
  print(f"Kedalaman: {result['deep']}")
  print(f"Epicentern: {result['epicenter']}")
  print(f"Dirasakan: {result['feel']}")


# if __name__ == '__main__':
print("Main Aplication")
result = data_extraction()
print(result)
show_data(result)