"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
from random import randint
import itertools

k = int(input('Введите k: '))


def ratio(num: int):
    ratio_lst = [randint(0, 10) for i in range(num + 1)]

    while ratio_lst[0] == 0:
        ratio_lst[0] = randint(1, 10)

    return ratio_lst


def get_result(num: int, ratio_lst: list):
    values = ['*x^'] * (k - 1) + ['*x']
    lst = [[a, b, c] for a, b, c in itertools.zip_longest(ratio_lst, values, range(num, 1, -1), fillvalue='') if a != 0]

    for i in lst:
        i.append(' + ')

    lst = list(itertools.chain(*lst))
    lst[-1] = ' = 0'

    return ''.join(map(str, lst)).replace(' 1*x', ' x')


if __name__ == '__main__':
    ratios = ratio(k)
    result = get_result(k, ratios)
    print(result)

    with open('file.txt', 'w') as f:
        f.write(result)