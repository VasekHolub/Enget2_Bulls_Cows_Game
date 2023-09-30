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
    return "-" * 53


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


def bulls_cows_logger(bulls, cows):
    if bulls == 1 and cows == 1:
        print(f"{bulls} bull, {cows} cow\n{sep_print()}")
    elif bulls != 1 and cows != 1:
        print(f"{bulls} bulls, {cows} cows\n{sep_print()}")
    elif bulls == 1 and cows != 1:
        print(f"{bulls} bull, {cows} cows\n{sep_print()}")
    elif bulls != 1 and cows == 1:
        print(f"{bulls} bulls, {cows} cow\n{sep_print()}")


def results_logger(guesses):
    if guesses == 1:
        print(
            f"""Correct, you've guessed the right number in 1 guess!\n{sep_print()}\nYou must have gotten lucky!\n{sep_print()}"""
        )
    else:
        performance = ""
    if guesses <= 5:
        performance = "amazing"
    elif guesses <= 10:
        performance = "great"
    elif guesses <= 20:
        performance = "pretty good"
    elif guesses <= 30:
        performance = "could be better"
    elif guesses > 30:
        performance = "not great"
    print(
        f"""Correct, you've guessed the right number in {guesses} guesses!\n{sep_print()}\nThat's {performance}!\n{sep_print()}"""
    )


def welcome_message():
    print(
        f"""Hi there!
{sep_print()}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a four digit number that doesn't start\nwith zero and is compoused of unique numbers. 
{sep_print()}"""
    )


def main():
    welcome_message()
    while True:
        random_number = game_number_generator()
        guesses = 0
        while True:
            bulls_cows = cows_bulls_evaulation(random_number)
            bulls = bulls_cows[0]
            cows = bulls_cows[1]
            if bulls != 4:
                bulls_cows_logger(bulls, cows)
            else:
                guesses += 1
                results_logger(guesses)
                break
            guesses += 1
            continue
        if input('Write "y" to play again or anything else to exit the game: ') == "y":
            continue
        else:
            break


# main function execution
if __name__ == "__main__":
    main()
