"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""

text = "Напишите программу, удаляющую из текста все слова, содержащие ""абв""."


def delete_abc(text: str):
    return ' '.join(list(filter(lambda x: 'абв' not in x, text.split())))


if __name__ == '__main__':
    print(delete_abc(text))
