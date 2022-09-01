"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""

from random import choice

intro_text = """
Здравствуйте! Давайте поиграем в игру "Забери все конфеты!"
Основные правила игры:
    Вам будет дано некоторое количество конфет,
    За один ход вы можете взять не более определённого количества конфет,
    О котором вы договариваетесь с оппонентом.
    Начинаем!
"""
print_outs = 'Ваша очередь', 'возьмите конфеты', 'сколько конфет возьмёте?', 'Ваш ход'


def game(candies_amount: int, max_candies: int, players: list, message: tuple):
    cnt = 0

    while candies_amount > 0:
        print(f'{players[cnt % 2]}', choice(message))
        move = int(input())
        if move > candies_amount or move > max_candies:
            print(f'Это слишком много, можно взять не более {max_candies} конфет, у нас всего {candies_amount} конфет')
            attempt = 3
            while attempt > 0:
                if candies_amount >= move <= max_candies:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -= 1
            else:
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        candies_amount = candies_amount - move
        if candies_amount > 0:
            print(f'Осталось {candies_amount} конфет')
        else:
            print('Все конфеты разобраны.')
        cnt += 1
    return players[not cnt % 2]


if __name__ == '__main__':
    print(intro_text)

    player_1 = input('Первый игрок, как к Вам можно обращаться?: ')
    player_2 = input('Второй игрок, и Вы представьтесь, пожалуйста: ')
    players = [player_1, player_2]

    candies_amount = int(input('Сколько конфет будем разыгрывать?: '))
    max_candies = int(input('Сколько максимально конфет будем брать за один ход: '))

    winner = game(candies_amount, max_candies, players, print_outs)
    if not winner:
        print('ничья')
    else:
        print(f'Выиграл {winner}')