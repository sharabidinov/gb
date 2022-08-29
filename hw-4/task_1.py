"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""
usr_input = int(input('Введите N: '))


def is_prime(num: int):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_list(n):
    result = []

    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)

    return result


if __name__ == '__main__':
    print(prime_list(usr_input))