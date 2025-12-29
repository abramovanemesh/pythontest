import requests
from file_result_reverse_geocode import *


# проверка на то, какой ответ будет, и что делать, если ошибка
def check_response(response):
    assert response.status_code == 200, 'Статус код отличается от 200' #Проверяем, что соответствует необходимому значению, иначе выводится ошибка, которая указана после запятой
    response_data = response.json()
    return response_data

# ф-я на генерирование url для обратного поиска
def makes_url_reverse_geocode(lat, lon):
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
    response = requests.get(base_url, params=params, headers=headers)
    response_data = check_response(response)  #во втором файле ничего не сделано для этого
    return response_data
    # return response




# функция для нахождения координат по адресу
def makes_url_search_geocode(street, city, county, country):
    base_url = 'https://nominatim.openstreetmap.org'
    params = {
        'street': street,
        'city': city,
        'county': county,
        'country': country,
        'format': 'jsonv2',
        'accept-language': 'ru'
    }
    headers = {
        'User-Agent': 'MyGeocodingApp/1.0 (abramova-nemesh@gmail.com)',
        'Accept': 'application/json'
    }
    response = requests.get(base_url, params=params, headers=headers)
    response_data = check_response(response)
    return response_data

# Получение координат из ответа
def get_coordinates(response_data):
    if len(response_data) != 0:
        actual_coord = {
            'lat': float(response_data[0]['lat']),
            'lon': float(response_data[0]['lon']),
        }
    else:
        actual_coord = {}
    return actual_coord