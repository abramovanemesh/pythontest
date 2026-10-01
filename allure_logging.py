import logging

#debug 10, info 20
logger = logging.getLogger("log_geocode") #создание логгера, принимает только его имя
logger.setLevel(logging.INFO)   #Изменили стандартный уровень логирования, по умолчанию 30

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_handlers = logging.StreamHandler()   #вывод в консоль
console_handlers.setLevel(logging.INFO)
console_handlers.setFormatter(formatter)

file_handlers = logging.FileHandler('test.log', mode="w", encoding="utf-8") #вывод в файл
file_handlers.setLevel(logging.INFO)
file_handlers.setFormatter(formatter)

logger.addHandler(console_handlers)
logger.addHandler(file_handlers)
