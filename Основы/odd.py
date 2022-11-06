from datetime import datetime
import time
import random

# модуль и суб-модуль

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    # Создается объект, представляющий текущее время, из него извлекается значение атрибута minute
    right_this_minute = datetime.today().minute
    # in это супер оператор
    if right_this_minute in odds:
        print(f" This {right_this_minute} seems a little add")
    else:
        print(f" Not an odd {right_this_minute}")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)





