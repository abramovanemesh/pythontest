import logging

#debug 10, info 20
logger = logging.getLogger("log_geocode") #создание логгера, принимает только его имя
logger.setLevel(logging.INFO)   #Изменили стандартный уровень логирования, по умолчанию 30
handlers = [                     #обработчик (будет зависеть от уровня сообщений)
    logging.StreamHandler(),   #вывод в консоль
#    logging.FileHandler('test.log', mode="w", encoding="utf-8") #вывод в файл
    ]