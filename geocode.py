#Реверсивный поиск
import requests
import time
import json
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
        with open('test_lag_lon.json', 'r', encoding='utf-8') as file:
            dict_from_file = json.load(file)
            if dict_from_file == response.json():
                print('Сошлось')
        print(f"Результат поиска {response.json()}")
    else:
        print(f"Ошибка: {response.status_code}")
        result = None


reverse_geocode(lat=63.57239690319817, lon=53.65161001682282)
reverse_geocode(lat=-22.906626805986644, lon=-43.18848431110382)
reverse_geocode(lat=41.38683466270279, lon=2.1460247039794926)


# Прямой поиск

# import requests
# import time
# import json
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
#         print(f"Результат поиска {result}")
#         with open ('search_geocode_test.json', 'a', encoding = 'utf-8') as f: #это я вроде дозазаписываю результаты в json
#             json.dump(result, f, ensure_ascii=False, indent=2)
#         if result:
#             print("Широта:", result[0]['lat'])
#             print("Долгота:", result[0]['lon'])
#     else:
#         print(f"Ошибка: {response.status_code}")
#         result = None
#
#
# search_geocode("10/Псковская", "Вологда", "Вологодская область", "Россия")
# search_geocode("26/West Cedar Street", "Boston", "Suffolk County", "Соединенные Штаты Америки")
# search_geocode("445/Rua Bueno Brandão", "Сан-Паулу", "Região Metropolitana de São Paulo", "Бразилия")
# search_geocode("Résidence la Sablière", "Иль-де-Франс", "Валь-де-Марн", "Франция")
# #негативные сцении
# search_geocode("", "", "", "")
# search_geocode("123123", "Санкт-Петербург", "Вологодская область", "Испания")


