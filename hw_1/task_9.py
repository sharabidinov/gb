# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

from random import randint

quarter = randint(1, 4)
point_ranges = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']

print(f'{quarter}: {point_ranges[quarter - 1]}')
