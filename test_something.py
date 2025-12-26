import pytest
import allure
import requests
from jsonschema import validate
from file_result_reverse_geocode import *
from methods import *

# @allure.title('Проверка обратного геокодирования')
# @pytest.mark.parametrize('lat, lon, result', [
#     (coord_1['lat'], coord_1['lon'], address_1),
#     (coord_2['lat'], coord_2['lon'], address_2),
#     (coord_3['lat'], coord_3['lon'], address_3),
#     (coord_4['lat'], coord_4['lon'], address_4)
# ])
# def test_reverse_geocode(lat, lon, result):
#     with allure.step('Составление запроса по координатам'):
#         response = makes_url_reverse_geocode(lat, lon)
#         response_data = response.json()
#     with allure.step('Проверка статус кода'):
#         assert response.status_code == 200, 'Received status code is not equal to expected' #Проверяем, что соответствует необходимому значению, иначе выводится ошибка, которая указана после запятой
#     with allure.step('Сравнение ожидаемых результатов с действительными'):
#         validate(response_data, result)
# #    print(response.json())

# поиск координат по адресу
@allure.title('Проверка прямого геокодирования')
@pytest.mark.parametrize('params', params_for_search_test)
def test_search_geocode(params):
    with allure.step('Составление запроса по координатам'):
        response = makes_url_search_geocode(street = params['street'], city = params['city'],
                                            county = params['county'], country = params['country'])
        with allure.step('Проверка статус кода'):
            assert response.status_code == 200, 'Статус код отличается от 200'  # Проверяем, что соответствует необходимому значению, иначе выводится ошибка, которая указана после запятой
        response_data = response.json()
    with allure.step('Запись результатов в словарь'):
        if len(response_data) != 0:
            actual_coord = {
                'lat': float(response_data[0]['lat']),
                'lon': float(response_data[0]['lon']),
            }
        else:
            actual_coord = {}

    with allure.step('Сравнение ожидаемых результатов с действительными'):
        assert actual_coord == params['coordinates'], (f'Полученные координаты - {actual_coord}, '
                                                       f'ожидаемые - {params["coordinates"]}')
    print(response.json())

