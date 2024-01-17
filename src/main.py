"""
### Требования

- Последние 5 выполненных (EXECUTED) операций выведены на экран.
- Операции разделены пустой строкой.
- Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
- Сверху списка находятся самые последние операции (по дате).
- Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом).
- Номер счета замаскирован и не отображается целиком в формате  **XXXX
    (видны только последние 4 цифры номера счета).
"""
from utils import *

executed = get_executed_operations(load_json())
operations = sort_date_operations(executed)
dates = change_date(operations)
card_number = mask_card_number(operations)
amount_number = mask_amount_number(operations)

for operation in range(len(operations)):
    print(f"{dates[operation]} {operations[operation]['description']}")
    print(f"{card_number[operation]} -> Счет {amount_number[operation]}")
    print(f"{operations[operation]['operationAmount']['amount']} {operations[operation]['operationAmount']['currency']['name']}\n")