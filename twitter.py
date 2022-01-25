from bs4 import BeautifulSoup
import requests


datayellow = None
try:
  datayellow = requests.get("www.yellowpages.com.au")
except Exception:
  print("Tidak dapat mengambil data")
if datayellow.status_code == 200:
  soup = BeautifulSoup(datayellow.text, 'html.parser')
  print(soup.prettify())