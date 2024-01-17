import json
import re
from datetime import datetime
from config import *


def load_json():
    """
    Открытие файла operations.json
    :return: json_user_operations
    """
    with open(OPERATION, 'r', encoding="UTF-8") as file:
        json_user_operations = json.load(file)
    return json_user_operations


def get_executed_operations(values):
    """
    Сортировка operations.json есть ли EXECUTTED
    :return: executed_operations
    """
    executed_operations = []
    for value in values:
        if value == {}:
            continue
        elif value['state'] == 'EXECUTED':
            executed_operations.append(value)
    return executed_operations


def sort_date_operations(operations):
    """
    Функция вывода последних 5 операций
    :return: list_operation
    """
    sort_list = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    list_operation = sort_list[:5]
    return list_operation


def change_date(date):
    """
    Функция форматирования даты, пример: 14.10.2018
    :return: date_operations
    проверка print(change_date(sort_date_operations(get_executed_operations(load_json()))))
    """
    date_operations = []
    for list_data in date:
        sort_data = datetime.strptime(list_data['date'], "%Y-%m-%dT%H:%M:%S.%f")
        format_date = f"{sort_data:%d.%m.%Y}"
        date_operations.append(format_date)
    return date_operations


def mask_card_number(card_numbers):
    """
    скрытие номера карты
    check_format = re.findall('....', card_number['from'])
    проверка: print(mask_card_number("Maestro 1596837868705199"))
    """
    card_number_operations = []
    for card_number in card_numbers:
        if card_number['description'] == "Открытие вклада":
            card_number['from'] = f"Счёт клиента: {card_number['to'][5:]}"
        mask_card = card_number['from'].split()
        mask_card_copy = mask_card.copy()
        del mask_card_copy[-1]
        card_mask = re.findall('....', mask_card[-1])
        number_card = card_mask[0], card_mask[1][0:2] + '**', card_mask[2].replace(card_mask[2], '****'), card_mask[3:]
        mask_number = " ".join(number_card[3])
        card_number_operations.append(f"{' '.join(mask_card_copy)} {' '.join(list(number_card[0:3]))} {mask_number}")
    return card_number_operations


def mask_amount_number(amount_numbers):
    """
    скрытие номера счета
    проверка print(mask_amount_number("Счет 35383033474447895560"))
    """
    amount_number_operations = []
    for amount_number in amount_numbers:
        format_to_check = re.findall('....', amount_number['to'])
        check_to_format = format_to_check[4:]
        number_amount = check_to_format[0].replace(check_to_format[0], '**'), check_to_format[1]
        amount_mask = ''.join(list(number_amount))
        amount_number_operations.append(amount_mask)
    return amount_number_operations