"""
Напишите программу, которая выводит квадратную матрицу размера N на N. В каждой нечётной строке матрицы идут числа от 1 до N, а в каждой чётной — просто числа, равные номеру этой строки.
"""

# my version
def main():
    size = int(input("Enter size of the matrix: "))
    matrix = ""

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if i % 2 == 0:
                matrix += f"{i} "
            else:
                matrix += f"{j} "
        matrix += "\n"
    print(matrix)


# another version
def another_version():
    size = int(input("Enter size of the matrix: "))

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if i % 2 == 0:
                print(i, end='\t')
            else:
                print(j, end='\t')
        print()


if __name__ == "__main__":
    main()
    another_version()
