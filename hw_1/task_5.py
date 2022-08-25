# Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

user_input = int(input('Введите число: '))

if user_input % 5 == 0 and user_input % 10 == 0:
    print(f'{user_input} кратен 5 и 10')
elif user_input % 15 == 0 and not user_input % 30 == 0:
    print(f'{user_input} кратен 15, но не 30')
else:
    print('something happened')
