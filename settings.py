import json
import logging

logger = logging.getLogger()
logger.setLevel('INFO')

SETTINGS = {
    'hash': "4f9cbbc1e5a60f526a58cde1343acd900b3f918f6fdff73eb82b0b87ae7d8e22",
    'bin':  ["427409","427695","424542","424543","424544","442197","442194","442195","442196","479578","480110","480111","480112","480113","480114","481776","481777","481779","483983","427400","427402","427403","427404","427406","427407","427408","427411","427412","427413"],
    'last_four_numbers': 'files/last_four_numbers.txt',
    'card_number': 'files/card_number.txt',
    'csv_statistics': 'files/statistics.csv',
    'png_statistics': 'files/statistics.png'
}


def read_settings(file_with_settings: str = 'files/settings.json') -> dict:
    """
    Фукнция считывает настройки из файла
    :param file_with_settings: Путь к файлу с настройками
    :return: Настройки
    """
    settings = None
    try:
        with open(file_with_settings, 'r') as f:
            settings = json.load(f)
        logging.info("Настройки успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать настройки")
    return settings


if __name__ == "__main__":
    with open('files/settings.json', 'w') as f:
        json.dump(SETTINGS, f)