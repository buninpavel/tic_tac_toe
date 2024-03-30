# test.py
from functools import lru_cache
import time

numbers = [1, 3, 4, 6, 9, 11]
squares = (x**2 for x in numbers if x % 3 == 0)
print(sum(squares))


people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func, sequence):
    for item in sequence:
        func(item)


say_to_all(lambda name: print(f'Привет, {name}!'), people)
say_to_all(lambda name: print(f'До завтра, {name}!'), people)
say_to_all(lambda name: print(f'Здравствуй, {name}!')
           if name[0] == 'С' else print(f'Привет, {name}!'), people)


def sleep_one_sec():
    print('Функция sleep_one_sec() начала вычисления.')
    print('Вычисляю...')
    time.sleep(1)
    return 'Функция sleep_one_sec() завершила вычисления.'


def time_of_function(func):
    def wrapper():
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 3)
        print(f'Время выполнения: {execution_time} сек.')
        return result
    return wrapper


# После первого запуска программы раскомментируйте декоратор @lru_cache:
# результаты выполнения функции expensive_computation() закешируются;
# при втором и третьем вызовах выполнение функции будет почти мгновенным.
@time_of_function
@lru_cache
def expensive_computation():
    sequence = [1]
    for item in range(10000):
        sequence.append(sum(sequence))
    return sequence[10]


print(expensive_computation())

print(expensive_computation())

print(expensive_computation())
