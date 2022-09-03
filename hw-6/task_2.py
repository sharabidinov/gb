"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""
usr_input = int(input('Введите N: '))


def primes(num: int):
    result = [True] * num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if result[i]:
            result[i * i::2 * i] = [False] * ((num - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, num, 2) if result[i]]


if __name__ == '__main__':
    print(primes(usr_input))
