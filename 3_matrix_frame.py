"""
Напишите программу, которая рисует с помощью символьной графики прямоугольную рамку. Для вертикальных линий используйте символ вертикального штриха |, а для горизонтальных — дефис -.

Пусть пользователь вводит ширину и высоту рамки.
"""
def main():
    height = int(input("Enter height of the frame: "))
    width = int(input("Enter width of the frame: "))

    for i in range(height):
        for j in range(width):
            if j == 0:
                print("|", end="")
            elif j == width - 1:
                print("|", end="")
            elif i == 0:
                print("-", end="")
            elif i == height - 1:
                print("-", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
