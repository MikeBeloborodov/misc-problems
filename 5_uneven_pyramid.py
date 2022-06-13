"""
Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами 
"""


def main():
    current_level_num = 1

    levels = int(input("Enter the amount of pyramid levels: "))

    for level in range(1, levels + 1):
        current_tab = ""
        for tab_num in range(levels - level, 0, -1):
            current_tab += "\t"
        print(current_tab, end='')
        for num in range(level):
            print(str( current_level_num ) + '\t\t', end='')
            current_level_num += 2
        print()


if __name__ == "__main__":
    main()

