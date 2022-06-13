"""
Мы делаем текстовую игру — гонку, и нам нужно вывести на экран что-то вроде трассы, где будут соревноваться наши машины. Напишите программу, которая выводит такую дорогу на экран (поле 20×50).
"""


def main():
    height = 20
    width = 50

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if height / 2 == i:
                print("-", end="")
            elif j + j == width:
                print("|", end="")
            elif j == (width / 2) - i - 3:
                print("/", end="")
            elif j == (width / 2) + i + 3:
                print("\\", end="")
            else:
                print(' ', end="")
        print() 


if __name__ == "__main__":
    main()

