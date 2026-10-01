import logging

logger = logging.getLogger("log_geocode")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_handlers = logging.StreamHandler()
console_handlers.setLevel(logging.INFO)
console_handlers.setFormatter(formatter)

file_handlers = logging.FileHandler('test.log', mode="w", encoding="utf-8")
file_handlers.setLevel(logging.INFO)
file_handlers.setFormatter(formatter)

logger.addHandler(console_handlers)
logger.addHandler(file_handlers)
