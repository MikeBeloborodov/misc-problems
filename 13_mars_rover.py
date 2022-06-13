"""
К роботу Валли отправили ещё одного робота — Билли. Это его первая высадка на Марс, поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров. Марсоход высаживается в центре комнаты (в точке 8, 10), после чего управление им передаётся оператору — пользователю вашей программы. Программа спрашивает, в какую сторону оператор хочет направить робота: север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D). Оператор делает выбор, марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию марсохода. Если марсоход упёрся в стену, то он не должен пытаться перемещаться в сторону стены, в этом случае его позиция не меняется. Создайте программу для управления роботом Билли.
"""
from getch import getch
import os


WIDTH = 20
HEIGHT = 15
INIT_POS_Y = 8
INIT_POS_X = 10
CONTROLS = {"w": -1, "a": -1, "s": 1, "d": 1}


def draw_screen(pos_x: int, pos_y: int) -> None:
    for row in range(1, HEIGHT + 1):
        for col in range(1, WIDTH + 1):
            if row == 1 or row == HEIGHT:
                print("-", end="")
            elif col == 1 or col == WIDTH:
                print("|", end="")
            elif row == pos_y and col == pos_x:
                print("*", end="")
            else:
                print(" ", end = "")
        print()


def handle_movement(user_input: str, current_pos_x: int, current_pos_y: int) -> list:
    if user_input == 'w' and current_pos_y > 2:
        current_pos_y += CONTROLS['w']
    if user_input == 'a' and current_pos_x > 2:
        current_pos_x += CONTROLS['a']
    if user_input == 's' and current_pos_y < HEIGHT - 1:
        current_pos_y += CONTROLS['s']
    if user_input == 'd' and current_pos_x < WIDTH - 1:
        current_pos_x += CONTROLS['d']

    return [current_pos_x, current_pos_y]


def main():
    user_input = ""
    current_pos_y = INIT_POS_Y
    current_pos_x = INIT_POS_X
    while True:
        os.system('clear')
        draw_screen(current_pos_x, current_pos_y)
        if user_input == "":
            print("\nYour input: ", end="")
        else:
            print(f"\nYour input: {user_input}", end="")
        user_input = getch()
        if user_input == "q":
            exit()
        if not user_input in CONTROLS:
            user_input = "Controls are w, a, s, d. Enter again."
        else:
            current_pos_x, current_pos_y = handle_movement(user_input, current_pos_x, current_pos_y)


if __name__ == "__main__":
    main()

