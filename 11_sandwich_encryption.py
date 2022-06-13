"""
Секретное агентство «Super-Secret-no» решило для шифрования переписки своих сотрудников использовать «метод бутерброда». Сначала буквы слова нумеруются в таком порядке: первая буква получает номер 1, последняя буква — номер 2, вторая – номер 3, предпоследняя – номер 4, потом третья… и так для всех букв (см. рисунок). Затем все буквы записываются в шифр в порядке своих номеров.

К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился. И теперь агенты не могут понять, что же они написали друг другу. Помогите им написать программу-дешифратор, которая бы расшифровывала введенные сообщения.

Пример:

Введите зашифрованное сообщение: shacnidw

Расшифрованное сообщение: sandwich
"""

def main(input_str: str) -> str:
    decrypted_str = ""
    
    for index, letter in enumerate(input_str, 1):
        if index % 2 == 0:
            pass
        else:
            decrypted_str += letter
    for index, letter in enumerate(input_str[::-1], 1):
        if index % 2 == 0:
            pass
        else:
            decrypted_str += letter

    print(decrypted_str)


if __name__ == "__main__":
    main("shacnidw")

