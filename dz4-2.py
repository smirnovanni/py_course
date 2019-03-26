if __name__ == "__main__":
    str = input('Введите фразу для сортировки: ').replace('  ', ' ')
    print('Прямая сортировка')
    print(sorted(str.split()))
    print('Обратная сортировка')
    print(sorted(str.split(), reverse=1))
