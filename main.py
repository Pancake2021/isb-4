import logging
import time
import argparse
from card_functions import enumerate_card_number
from files_functions import read_data_from_txt_file, write_data_to_txt_file, read_list, load_statistics, \
    write_statistics
from settings import read_settings
from visualization import create_png_with_statistics
from luhn_algorithm import Luhn

logger = logging.getLogger()
logger.setLevel('INFO')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-cus', '--custom', type=str,
                        help='Использует пользовательсткий файл с настройками, необходимо указать путь к файлу')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-crd', '--card_number_enumeration', type=int,
                       help='Ищет номер карты с помощью хеша, необходимо указать количество процессов')
    group.add_argument('-sta', '--statistics',
                       help='Получается статистику подбирая номер карты на разном количестве процессов')
    group.add_argument('-lun', '--lunh_algorithm', help='Проверяет валидность номера карты с помощью алгоритма Луна')
    group.add_argument('-vis', '--visualize_statistics', help='Создает гистограмму по имеющейся статистике')
    args = parser.parse_args()
    if args.custom:
        settings = read_settings(args.custom)
    else:
        settings = read_settings()
    if settings:
        if args.card_number_enumeration:
            hash = "4f9cbbc1e5a60f526a58cde1343acd900b3f918f6fdff73eb82b0b87ae7d8e22",
            bins = ["427409","427695","424542","424543","424544","442197","442194","442195","442196","479578","480110","480111","480112","480113","480114","481776","481777","481779","483983","427400","427402","427403","427404","427406","427407","427408","427411","427412","427413"],
            last_four_numbers = read_data_from_txt_file(settings['last_four_numbers'])
            card_number = enumerate_card_number(hash, bins, last_four_numbers, args.card_number_enumeration)
            if card_number:
                logging.info(f"Номер карты успешно найден: {card_number}")
                write_data_to_txt_file(str(card_number), settings['card_number'])
            else:
                logging.info("Не удалось найти номер карты")
        elif args.statistics:
            hash = "4f9cbbc1e5a60f526a58cde1343acd900b3f918f6fdff73eb82b0b87ae7d8e22",
            bins = ["427409","427695","424542","424543","424544","442197","442194","442195","442196","479578","480110","480111","480112","480113","480114","481776","481777","481779","483983","427400","427402","427403","427404","427406","427407","427408","427411","427412","427413"],
            last_four_numbers = read_data_from_txt_file(settings['last_four_numbers'])
            for i in range(1, 21):
                t1 = time.time()
                enumerate_card_number(hash, bins, last_four_numbers, i)
                t2 = time.time()
                write_statistics(i, t2 - t1, settings['csv_statistics'])
            logging.info("Статистика успешно посчитана")
        elif args.lunh_algorithm:
            card_number = read_data_from_txt_file(settings['card_number'])
            if Luhn(card_number):
                logging.info("Номер карты действителен")
            else:
                logging.info("Номер карты не действителен")
        elif args.visualize_statistics:
            create_png_with_statistics(load_statistics(settings['csv_statistics']), settings['png_statistics'])
            logging.info("Гистограмма успешно создана")