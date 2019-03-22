"""
Задача: дана строка с кодом шахматного хода, например, "E2-E4". Необходимо определить, является ли заданный код - ходом коня.
Входные данные: строка с 5ю символами: (Буква)(Цифра)(Дефис)(Буква)(Цифра). Буквы - заглавные буквы англ.алфавита. Все символы заданы в кодировке ASCII.
Вывод: TRUE/FALSE - является ли заданный ход - ходом коня.
Пример:
"E2-E4" -> False
"B1-C3" - True
"""


def is_horse(way):
    letters = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    try:
        a, b = way.split("-")
    except Exception as error:
        print("Некорректный ход. Пример \"E2-E4\"")
        exit()

    if abs(letters[a[0]] - letters[b[0]]) == 1 and abs(int(a[1]) - int(b[1])) == 2 \
            or abs(letters[a[0]] - letters[b[0]]) == 2 and abs(int(a[1]) - int(b[1])) == 1:
        print('Это конь')
    else:
        print('Не конь')


is_horse(input('Введите желаемый ход для проверки: '))
