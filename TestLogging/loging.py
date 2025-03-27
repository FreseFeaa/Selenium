import logging 

"""
5 Уровней Логгирования:
Debug - Отладочные сообщения
Info - информационный уровень
Warning - Предупреждения 
Error - Уровень ошибок
Critical - Критические ошибки
"""

logger = logging.getLogger("Selenium")
logger.setLevel(logging.INFO)

handler_file = logging.FileHandler("Selenium_log.log",mode = "a")
formater = logging.Formatter("%(asctime)s %(filename)s %(message)s")
handler_console = logging.StreamHandler()

handler_file.setLevel(logging.ERROR)

handler_file.setFormatter(formater)
handler_console.setFormatter(formater)

logger.addHandler(handler_file)
logger.addHandler(handler_console)

logger.info("Оно работает!")
logger.error("Шок ошибка!")