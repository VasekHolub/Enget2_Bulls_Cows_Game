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


def cows_bulls_evaulation(random_number):
    user_number = user_number_input()
    bulls = 0
    cows = 0
    for i in random_number:
        if i in user_number and random_number.index(i) == user_number.index(i):
            bulls += 1
        elif i in user_number and random_number.index(i) != user_number.index(i):
            cows += 1
    return bulls, cows


def welcome_message():
    print(
        f"""Hi there!
{sep_print()}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{sep_print()}"""
    )


def main():
    welcome_message()
    random_number = game_number_generator()
    guesses = 0
    while True:
        bulls_cows = cows_bulls_evaulation(random_number)
        bulls = bulls_cows[0]
        cows = bulls_cows[1]
        if bulls != 4:
            if bulls == 1 and cows == 1:
                print(f"{bulls} bull, {cows} cow\n{sep_print()}")
            elif bulls != 1 and cows != 1:
                print(f"{bulls} bulls, {cows} cows\n{sep_print()}")
            elif bulls == 1 and cows != 1:
                print(f"{bulls} bull, {cows} cows\n{sep_print()}")
            elif bulls != 1 and cows == 1:
                print(f"{bulls} bulls, {cows} cow\n{sep_print()}")
        else:
            guesses += 1
            if guesses == 1:
                print(
                    f"""Correct, you've guessed the right number in {guesses} guess\n{sep_print()}!"""
                )
            else:
                print(
                    f"""Correct, you've guessed the right number in {guesses} guesses\n{sep_print()}!"""
                )
            break
        guesses += 1
        continue


# main execution
if __name__ == "__main__":
    main()
