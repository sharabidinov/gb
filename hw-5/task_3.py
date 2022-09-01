"""
Создайте программу для игры в ""Крестики-нолики"".
"""

board = list(range(1, 10))


def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def take_input(choice):
    valid = False
    while not valid:
        answer = input("Куда поставим " + choice + "? ")
        try:
            answer = int(answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= answer <= 9:
            if str(board[answer - 1]) not in "XO":
                board[answer - 1] = choice
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for _ in win_coord:
        if board[_[0]] == board[_[1]] == board[_[2]]:
            return board[_[0]]
    return False


def main(board):
    cnt = 0
    win = False
    while not win:
        draw_board(board)
        if cnt % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        cnt += 1
        if cnt > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if cnt == 9:
            print("Ничья!")
            break
    draw_board(board)


if __name__ == '__main__':
    main(board)
