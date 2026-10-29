import time
import requests
from logger_conf import logger
import allure
import json
from pathlib import Path

headers = {
    'User-Agent': 'MyGeocodingApp/1.0 (abramova-nemesh@gmail.com)',
    'Accept': 'application/json'
}
# Получение ответа
def check_response(response):
    with allure.step("Получение статус кода запроса"):
        logger.info(f"URL запроса: {response.url}. \n Получен статус код: {response.status_code}")
        assert response.status_code == 200, f'Статус код отличается от 200 - {response.status_code}'
    with allure.step("Получение тела ответа response_data"):
        response_data = response.json()
        logger.info(f"Получено тело ответа: {response_data}")
        return response_data

# ф-я на генерирование url для поиска по координатам
def makes_url_reverse_geocode(lat, lon):
    with allure.step("Отправка URL-запроса"):
        base_url = 'https://nominatim.openstreetmap.org/reverse'
        params = {
            'lat': lat,
            'lon': lon,
            'format': 'jsonv2',
            'accept-language': 'ru'
        }
        logger.info(f"Координаты для обратного геокодинга lat={lat}, lon={lon}")
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        response_data = check_response(response)
        time.sleep(1)
        return response_data






# функция для нахождения координат по адресу
def makes_url_search_geocode(street, city, county, country):
    with allure.step("Отправка URL-запроса"):
        base_url = 'https://nominatim.openstreetmap.org/search'
        params = {
            'street': street,
            'city': city,
            'county': county,
            'country': country,
            'format': 'jsonv2',
            'accept-language': 'ru'
        }
        logger.info(f"Поиск по адресу: {street}, {city}, {county}, {country}")
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        response_data = check_response(response)
        time.sleep(1)
        return response_data

# Получение координат из ответа
def get_coordinates(response_data):
    if len(response_data) != 0:
        actual_coord = {
            'lat': float(response_data[0]['lat']),
            'lon': float(response_data[0]['lon']),
        }
        logger.info(f"Получены координаты: {actual_coord}")
    else:
        actual_coord = None
        logger.info(f"По указанному адресу координаты не найдены")
    return actual_coord



#Чтение json файла
DATA_DIR = Path(__file__).parent

def load_json(filename: str):
    path =   DATA_DIR / filename
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)