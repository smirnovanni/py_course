"""
Модуль для вычисления случайного простого числа
"""
from random import randint


def is_prime(x):
    """
    Проверка числа на простоту
    :param x: int
    :return: bool
    """
    if x > 3 and x % 2 == 0 or x <= 1:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def get_prime_num():
    """
    В цикле проверяйем псевдослучаные числа на простоту и возвращаем первое попавшееся
    :return: int
    """
    while True:
        num = randint(1, 10000)
        if is_prime(num):
            break

    return num
