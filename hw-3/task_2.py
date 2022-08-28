"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
lst_1 = [2, 3, 5, 6]
lst_2 = [2, 3, 4, 5, 6]


def multiply_odd_index(lst: list):
    start = 0
    end = len(lst) - 1
    result = []

    while start <= end:
        result.append(lst[start] * lst[end])
        start += 1
        end -= 1
    return result


if __name__ == '__main__':
    print(multiply_odd_index(lst_1))
    print(multiply_odd_index(lst_2))