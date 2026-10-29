import pytest
import allure

from methods import makes_url_reverse_geocode, makes_url_search_geocode, get_coordinates, load_json
#from file_result_geocode import params_for_search_test, params_for_revers_test

params_for_revers_test = load_json("file_for_reverse_test.json")
params_for_search_test = load_json("file_for_search_test.json")

class TestGeocode:

    @allure.title('Проверка обратного геокодирования - поиск адреса по координатам')
    @pytest.mark.parametrize("params", params_for_revers_test)
    def test_reverse_geocode(self, params):
        with allure.step('Получение адреса по координатам'):
            response_data = makes_url_reverse_geocode(lat = params["coordinates"]["lat"],
                                                      lon = params["coordinates"]["lon"])
        with allure.step('Сравнение ожидаемых результатов с действительными'):
            actual_address = response_data.get("address", None)
            assert actual_address is not None, "В ответе нет параметра address"
            mistakes = 0
            for key in params:
                if key == "coordinates":
                    continue
                if key not in actual_address or actual_address[key] != params[key]:
                    mistakes += 1
                assert mistakes == 0, (f" actual_address[key]={actual_address[key]},"
                                      f"params[key]={params[key]}")




    @allure.title('Проверка прямого геокодирования - поиск координат по адресу')
    @pytest.mark.parametrize('params', params_for_search_test)
    def test_search_geocode(self, params):
        with allure.step('Составление запроса через задание адреса'):
            response_data = makes_url_search_geocode(street = params['street'], city = params['city'],
                                                county = params['county'], country = params['country'])
        with allure.step('Получение координат из ответа'):
            actual_coord = get_coordinates(response_data)
        with allure.step('Сравнение ожидаемых результатов с действительными'):
            assert actual_coord is not None, "Координаты не получены"
            assert actual_coord == params['coordinates'], (f'Полученные координаты - {actual_coord}, '
                                                           f'ожидаемые - {params["coordinates"]}')


