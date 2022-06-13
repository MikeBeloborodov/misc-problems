"""
Напишите программу, которая получает на вход размер квадратной матрицы и выводит на экран по такому принципу диагональ из единиц с левого нижнего угла до верхнего правого, ниже диагонали — двойки, выше — нули.
"""


def main():
    size = int(input("Enter the size of the matrix: "))

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if i + j == size + 1:
                print("1", end=" ")
            elif i + j < size + 1:
                print("0", end=" ")
            elif i + j > size + 1:
                print("2", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    main()

