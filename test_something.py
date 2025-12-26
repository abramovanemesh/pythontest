import pytest
import allure
import requests
from jsonschema import validate
from file_result_reverse_geocode import *
from methods import *

# реверсивный поиск
@pytest.mark.parametrize('lat, lon, result', [
    (coord_1['lat'], coord_1['lon'], address_1),
    (coord_2['lat'], coord_2['lon'], address_2),
    (coord_3['lat'], coord_3['lon'], address_3),
    (coord_4['lat'], coord_4['lon'], address_4)
])
# Запуск теста на проверку реверсивного поиска
def test_reverse_geocode(lat, lon, result):
    # Создание запроса на проверку
    with allure.step('Составление запроса'):
        response = makes_url_reverse_geocode(lat, lon)
        response_data = response.json()
    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, 'Received status code is not equal to expected' #Проверяем, что соответствует необходимому значению, иначе выводится ошибка, которая указана после запятой
    with allure.step('Сравнение ожидаемых результатов с действительными'):
        validate(response_data, result)
#    print(response.json())

# поиск координат по адресу
#
# @pytest.mark.parametrize('street, city, county, country, result', [
#     (search_1['street'], search_1['city'], search_1['county'], search_1['country'], result_search_1),
#     (search_2['street'], search_2['city'], search_2['county'], search_2['country'], result_search_2),
#     (search_3['street'], search_3['city'], search_3['county'], search_3['country'], result_search_3),
#     (search_4['street'], search_4['city'], search_4['county'], search_4['country'], result_search_4),
#     (search_5['street'], search_5['city'], search_5['county'], search_5['country'], result_search_5)
# ])
# def test_search_geocode(street, city, county, country, result):
#     response = makes_url_search_geocode(street, city, county, country)
#     response_data = response.json()
#     assert response.status_code == 200, 'Received status code is not equal to expected' #Проверяем, что соответствует необходимому значению, иначе выводится ошибка, которая указана после запятой
#     validate(response_data, result)
#     print(response.json())

