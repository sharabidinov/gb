"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""


def encode(string: str):
    encoded_string = ""
    i = 0

    while i <= len(string) - 1:
        count = 1
        ch = string[i]
        j = i
        while j < len(string) - 1:
            if string[j] == string[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string


def decode(string: str):
    result = ''
    num = ''
    for i in string:
        if i.isalpha():
            result += i * int(num)
            num = ''
        else:
            num += i
    return result


if __name__ == '__main__':
    string = "hhhheeeelllloooo"
    print(encode(string))
    print(decode(encode(string)))
