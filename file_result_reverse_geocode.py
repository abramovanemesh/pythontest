# reverse поиск

coord_1 = {'lat': 55.755843410046594, 'lon': 37.617734670639045}
address_1 = {
    'type': 'object',
    'properties': {
        'category': {'type': 'string', 'enum': ['highway']},
        'address' : {'enum': [{
        'highway': 'Нулевой километр',
        'road': 'проезд Воскресенские Ворота',
        'quarter': '18',
        'suburb': 'Тверской район',
        'city': 'Москва',
        'state':'Москва',
        'ISO3166-2-lvl4': 'RU-MOW',
        'region': 'Центральный федеральный округ',
        'postcode': '103265',
        'country':'Россия',
        'country_code': 'ru'}]}
    },
    'required': ['address']
}


coord_2 = {'lat': 63.57250920316036, 'lon': 53.65243077278138}
address_2 = {
    'type': 'object',
    'properties': {
        'category': {'type': 'string', 'enum': ['building']},
        'type': {'type': 'string', 'enum': ['apartments']},
        'address' : {'enum': [{
        "house_number": "57",
        "road": "Интернациональная улица",
        "town": "Ухта",
        "county": "муниципальный округ Ухта",
        "state": "Республика Коми",
        "ISO3166-2-lvl4": "RU-KO",
        "region": "Северо-Западный федеральный округ",
        "postcode": "169300",
        "country": "Россия",
        "country_code": "ru"
    }]}
    },
    'required': ['address']
}

coord_3 = {'lat': -22.9036181, 'lon': -43.1882037}
address_3 = {
    'type': 'object',
    'properties': {
        'category': {'type': 'string', 'enum': ['building']},
        'type': {'type': 'string', 'enum': ['school']},
        'address' : {'enum': [{
        'building': 'Escola Municipal Rivadávia Corrêa',
        "house_number": "1314",
        "road": "Avenida Presidente Vargas",
        "neighbourhood": "Saara",
        "suburb": "Centro",
        "city": "Рио-де-Жанейро",
        "municipality": "Região Geográfica Imediata do Rio de Janeiro",
        "county": "Região Metropolitana do Rio de Janeiro",
        "state_district": "Região Geográfica Intermediária do Rio de Janeiro",
        "state": "Рио-де-Жанейро",
        "ISO3166-2-lvl4": "BR-RJ",
        "region": "Юго-восточный регион",
        "postcode": "20071-004",
        "country": "Бразилия",
        "country_code": "br"
    }]}
    },
    'required': ['address']
}

coord_4 = {'lat': 41.38683466270279, 'lon': 2.1460247039794926}
address_4 = {
    'type': 'object',
    'properties': {
        'category': {'type': 'string', 'enum': ['shop']},
        'type': {'type': 'string', 'enum': ['electronics']},
        'address' : {'enum': [{
        "shop": "Samsung",
        "house_number": "111",
        "road": "Carrer de Còrsega",
        "quarter": "la Nova Esquerra de l'Eixample",
        "suburb": "Эшампле",
        "city": "Барселона",
        "county": "Барселонес",
        "province": "Барселона",
        "ISO3166-2-lvl6": "ES-B",
        "state": "Каталония",
        "ISO3166-2-lvl4": "ES-CT",
        "postcode": "08029",
        "country": "Испания",
        "country_code": "es"
    }]}
    },
    'required': ['address']
}



#Прямой поиск по адресу

params_for_search_test = [
    {"street": "10/Псковская",
    "city": "Вологда",
    "county": "Вологодская область",
    "country": "Россия",
    "coordinates": {'lat': 59.1987304, 'lon': 39.8335431}
     },
    {
    "street": "94/West Cedar Street",
    "city": "Boston",
    "county": "Suffolk County",
    "country": "Соединенные Штаты Америки",
    "coordinates": {'lat': 42.3606016, 'lon': -71.0702549}
    },
    {
    "street": "309/Rua Bueno Brandão",
    "city": "Сан-Паулу",
    "county": "Região Metropolitana de São Paulo",
    "country": "Бразилия",
    "coordinates": {'lat': -23.5908735, 'lon': -46.6707229}
    },
    {
    "street": "Résidence la Sablière",
    "city": "Иль-де-Франс",
    "county": "Валь-де-Марн",
    "country": "Франция",
    "coordinates": {'lat': 48.8311521, 'lon': 2.5422879}
    },
    {
    "street": "12/Ивановская ",
    "city": "Бухарест",
    "county": "Самарская область ",
    "country": "Испания",
    "coordinates": {}
    }
]

