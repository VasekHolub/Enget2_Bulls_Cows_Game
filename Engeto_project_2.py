"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Václav Holub
email: vaclavholub5@seznam.cz
discord: .avalok
"""

# imports
from random import randint


# functions
def duplicate_detector(number, sequence):
    return True if number in sequence else False


def sep_print():
    return "-" * 47


def game_number_generator():
    random_number_sequence = []
    i = 4
    while i > 0:
        random_number = randint(0, 9)
        if duplicate_detector(random_number, random_number_sequence):
            continue
        random_number_sequence.append(random_number)
        if random_number_sequence[0] == 0:
            random_number_sequence.remove(0)
            continue
        i -= 1
    return random_number_sequence


def welcome_message():
    print(
        f"""Hi there!
{sep_print()}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{sep_print()}"""
    )


def user_number_input():
    while True:
        user_number = input("Enter a number: ")
        if (
            len(user_number) > 4
            or len(set(user_number)) < 4
            or user_number[0] == "0"
            or not user_number.isnumeric()
        ):
            print("Invalid number, please try again.")
            continue
        else:
            user_number_list = []
            for i in user_number:
                user_number_list.append(int(i))
            return user_number_list


def cows_bulls_evaulation():
    random_number = [1, 2, 3, 4]
    user_number = user_number_input()
    bulls = 0
    cows = 0
    for i in random_number:
        if i in user_number and random_number.index(i) == user_number.index(i):
            bulls += 1
        elif i in user_number and random_number.index(i) != user_number.index(i):
            cows += 1
    return bulls, cows


def main():
    welcome_message()
    cows_bulls_evaulation()


print(cows_bulls_evaulation())


# tests of functions
def test_game_number_generator():
    Error_count = 0
    i = 1000
    while i > 0:
        test_sequence = game_number_generator()
        if test_sequence[0] == 0 or len(set(test_sequence)) != 4:
            Error_count += 1
        i -= 1
    return print("Number of errors =", Error_count)


# main execution
if __name__ == "__main__":
    ...
