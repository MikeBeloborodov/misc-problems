"""
Для коров есть 10 стойл. В каждом стойле разные условия для животных, поэтому и молока они дают по-разному. В первом стойле производят 2 литра в день, во втором 4, в третьем — 6, потом 8, 10, 12, 14, 16, 18, 20. Но коровы стоят не во всех стойлах. Свободные и занятые обозначаются строкой из букв a и b, где a — свободное стойло, b — занятое.

Напишите программу для подсчета получаемого молока в коровнике, с учетом следующего взаимодействия пользователя с программой: пользователь вводит строку из 10 символов a и b. Необходимо определить, сколько в итоге будет произведено молока за день.
"""


def main(input_str: str):
    total_milk = 0

    for index, letter in enumerate(input_str, 1):
        if letter == 'a':
            total_milk += index * 2
    
    print(total_milk)


if __name__ == "__main__":
    main("bbaaaaaaaa")

