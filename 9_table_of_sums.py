"""
Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 1 до N.
"""


def main():
    max_sum_num = int(input("Enter the number: "))

    for col in range(max_sum_num + 1):
        for row in range(max_sum_num + 1):
            print(f"{col + row}", end=" ")
        print()


if __name__ == "__main__":
    main()

