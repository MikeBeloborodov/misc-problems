"""
Пользователь вводит число N. Напишите программу, которая выводит такую «лесенку» из чисел:
"""

def main():
    size = int(input("Enter size of the ladder: "))

    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print(j, end="\t")
        print()


if __name__ == "__main__":
    main()
