"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
"""

user_input = input('Введите число: ')
sum_num = 0

for i in user_input:
    sum_num += int(i)

print(sum_num)
