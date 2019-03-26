def calc(*args):
    sum = 0
    for i in range(0, len(args)):
        sum += args[i]
    return sum / len(args)


if __name__ == "__main__":
    print(calc(1, 2, 3, 4, 5, 6, 7, 8))     # списком
    print(calc(*tuple(range(1, 8 + 1))))    # по дипазону
