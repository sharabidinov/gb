"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

from decimal import Decimal

lst = [1.1, 1.2, 3.1, 5, 10.01]


def subtract_fraction_part(lst):
    frctn_lst = []
    for i in lst:
        if type(i) == float:
            decim = Decimal(str(i))
            fraction_part = decim - decim.to_integral_exact()
            frctn_lst.append(fraction_part)
    return max(frctn_lst) - min(frctn_lst)


if __name__ == '__main__':
    print(subtract_fraction_part(lst))
