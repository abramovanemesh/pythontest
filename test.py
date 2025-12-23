import requests
import time
# функция для нахождения адреса по реверсивному поиску
def reverse_geocode(lat, lon):
    base_url = 'https://nominatim.openstreetmap.org/reverse'
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'jsonv2',
        'accept-language': 'ru'
    }
    headers = {
        'User-Agent': 'MyGeocodingApp/1.0 (abramova-nemesh@gmail.com)',
        'Accept': 'application/json'
    }
    time.sleep(3)
    response = requests.get(base_url, params=params, headers=headers)
    print(f"Статус код {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Результат поиска {response.json()}")
    else:
        print(f"Ошибка: {response.status_code}")
        result = None
    if result:
        print("Адрес:", result.get('display_name'))
        print("Тип объекта:", result.get('type'))
        print("Категория:", result.get('category'))



reverse_geocode(lat=63.57239690319817, lon=53.65161001682282)
reverse_geocode(lat=-22.906626805986644, lon=-43.18848431110382)
reverse_geocode(lat=41.38683466270279, lon=2.1460247039794926)

#
# import requests
# import time
# # функция для нахождения координат по адресу
# def search_geocode(street, city, county, country):
#     base_url = 'https://nominatim.openstreetmap.org'
#     params = {
#         'street': street,
#         'city': city,
#         'county': county,
#         'country': country,
#         'format': 'jsonv2',
#         'accept-language': 'ru'
#     }
#     headers = {
#         'User-Agent': 'MyGeocodingApp/1.0 (abramova-nemesh@gmail.com)',
#         'Accept': 'application/json'
#     }
#     time.sleep(3)
#     response = requests.get(base_url, params=params, headers=headers)
#     print(f"Статус код {response.status_code}")
#     if response.status_code == 200:
#         result = response.json()
#         print(f"Результат поиска {response.json()}")
#     else:
#         print(f"Ошибка: {response.status_code}")
#         result = None
#     if result:
#         print("Широта:", result.get('lat'))
#         print("Долгота:", result.get('lon'))
#
# search_geocode(10, "Псковская", "Вологда", "Россия")
#

