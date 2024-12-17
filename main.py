import logging
from proxy_checker import ProxyChecker
import time


logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(message)s', 
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


def check_proxy(proxy_str):
    try:

        checker = ProxyChecker()


        result = checker.check_proxy(proxy_str)

        if result:
            logging.info(f"Прокси {proxy_str} работает")
            logging.info(f"Информация о прокси: {result}")
        else:
            logging.warning(f"Прокси {proxy_str} не работает")
    except Exception as e:
        logging.error(f"Ошибка при проверке прокси {proxy_str}: {e}")


def check_proxies_from_file(file_path):
    # Читаем прокси из файла
    with open(file_path, 'r') as file:
        proxy_str = file.readline().strip() 

    # Получаем IP, порт, логин и пароль
    ip, port, login, password = proxy_str.split(':')


    for i in range(256):
        modified_ip = f"{ip.rsplit('.', 1)[0]}.{i}"  
        new_proxy_str = f"{modified_ip}:{port}:{login}:{password}"
        check_proxy(new_proxy_str)

file_path = 'proxy.txt'

check_proxies_from_file(file_path)