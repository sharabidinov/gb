# Показать первую цифру дробной части числа

flt = float(input('Введите дробное число: '))
first_digit = int((flt*10) % 10)
print(f'flt: {flt}\nfirst_digit: {first_digit}')
