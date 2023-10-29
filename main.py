import requests
from bs4 import BeautifulSoup



date = input( "Öğrenmek istediğiniz tarihi 2023-10-03 formatında giriniz.")
time = input("Lütfen saati 03:27:35 formatında giriniz ")
enlem =input("Bulunduğunuz bölgenin enlemini(38.4333) formatında giriniz:")
boylam =input("Bulunduğunuz bölgenin enlemini(38.4333) formatında giriniz:")



url = f"https://api.meteomatics.com/{date}T{time}Z/t_2m:C/{enlem},{boylam}/html"
user_name = "your_username"
password = "your_password"
response = requests.get(url, auth=(user_name, password))
html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')
pre_content = soup.find('pre', id='csv').text
lines = pre_content.strip().split('\n')
data_line = lines[1]
values = data_line.split(';')
temperature = values[1]
print(temperature)
