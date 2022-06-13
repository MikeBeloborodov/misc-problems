"""
Нам дали заказ написать программу для электронной очереди. У каждого человека в очереди есть номер: нулевой, первый, второй, третий и так далее. Каждый час очередь уменьшается на одного человека, то есть уходит сначала нулевой номер, затем первый, второй и так далее. Наша программа получает на вход одно число — количество людей в очереди — и выводит на экран историю обслуживания очереди: какие номера в какой час оставались.
"""


def main():
    ppl_amount = int(input("Enter the amount of people in the queue: "))

    for i in range(ppl_amount):
        print(f"Hour #{i}:")
        print(f"People left: {ppl_amount - i}")
        print("Numbers in the queue: ", end="")
        for j in range(i, ppl_amount):
            print(f"{j}", end=" ")
        print()
    print(f"Hour #{ppl_amount}:")
    print(f"People left: 0")


if __name__ == "__main__":
    main()
