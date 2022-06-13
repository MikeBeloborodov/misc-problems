"""
Напишите программу, которая выводит на экран крест из символов ^

(символы выводятся по диагоналям воображаемого квадрата).
"""

def main():
    side = int(input("Enter size of the square side: "))

    for i in range(side):
        for j in range(side):
            if i == j:
                print("^", end=" ")
            elif i + j == side - 1:
                print("^", end=" ")
            else:
                print(" ", end=" ")
        print()



if __name__ == "__main__":
    main()
