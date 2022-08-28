"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


num = int(input('Введите n: '))


def fibonacci(n: int):
    sequence = []
    start = 1
    end = 1

    for i in range(n):
        sequence.append(start)
        start, end = end, start + end

    start = 0
    end = 1
    for i in range(n+1):
        sequence.insert(0, start)
        start, end = end, start - end

    return sequence


if __name__ == '__main__':
    print(fibonacci(num))
