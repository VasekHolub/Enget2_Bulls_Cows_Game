"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie (Bulls & Cows)
author: Václav Holub
email: vaclavholub5@seznam.cz
discord: .avalok
"""

# imports
from random import randint


# functions
def sep_print():
    return "-" * 55


def welcome_message():
    print(
        f"""
Hi there!
{sep_print()}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game!
Enter a four digit number that doesn't start
with zero and is compoused of unique numbers.
{sep_print()}"""
    )


def game_number_generator():
    random_number_sequence = []
    i = 4
    while i > 0:
        random_number = randint(0, 9)
        if random_number in random_number_sequence:
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
            len(user_number) != 4
            or len(set(user_number)) < 4
            or user_number[0] == "0"
            or not user_number.isnumeric()
        ):
            print(f"Invalid number, please try again.\n{sep_print()}")
            continue
        else:
            user_number_list = []
            for i in user_number:
                user_number_list.append(int(i))
            return user_number_list


def evaluate_guess(random_number: list):
    user_number = user_number_input()
    bulls = 0
    cows = 0
    for i in random_number:
        if i in user_number and random_number.index(i) == user_number.index(i):
            bulls += 1
        elif i in user_number and random_number.index(i) != user_number.index(i):
            cows += 1
    return bulls, cows


def bulls_cows_logger(bulls_cows: tuple):
    bulls = bulls_cows[0]
    cows = bulls_cows[1]
    if bulls == 1 and cows == 1:
        print(f"{bulls} bull, {cows} cow\n{sep_print()}")
    elif bulls != 1 and cows != 1:
        print(f"{bulls} bulls, {cows} cows\n{sep_print()}")
    elif bulls == 1 and cows != 1:
        print(f"{bulls} bull, {cows} cows\n{sep_print()}")
    elif bulls != 1 and cows == 1:
        print(f"{bulls} bulls, {cows} cow\n{sep_print()}")


def results_logger(guesses: int):
    """
    Displayes results of the game and evaluates
    users results according to the number of guesses.
    """
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
            performance = "not great"
        elif guesses > 30:
            performance = "bad"
        print(
            f"""Correct, you've guessed the right number in {guesses} guesses!\n{sep_print()}\nThat's {performance}!\n{sep_print()}"""
        )


def sorted_game_stats_logger(game_scores: dict):
    """
    Functions takes the game scores dict of the number of games the user played.
    It sorts this dict from the game with the lowest amount of guesses to the one
    with the highest amount.
    It then prints the sorted dict to the user.
    """
    sorted_values = sorted(game_scores.values(), reverse=False)
    sorted_dict = dict()
    for i in sorted_values:
        for k in game_scores.keys():
            if game_scores[k] == i:
                sorted_dict[k] = game_scores[k]
    for key, value in sorted_dict.items():
        if value == 1:
            print(f"Game {key}: {value} guess")
        else:
            print(f"Game {key}: {value} guesses")


def main():
    game_number = 0
    game_scores = dict()
    welcome_message()
    while True:
        random_number = game_number_generator()
        guesses = 0
        while True:
            bulls_cows = evaluate_guess(random_number)
            if bulls_cows[0] != 4:
                bulls_cows_logger(bulls_cows)
            else:
                game_number += 1
                guesses += 1
                game_scores[str(game_number)] = guesses
                results_logger(guesses)
                break
            guesses += 1
            continue
        user_input = input(
            'Type "y" to play again, "s" to show game statistics\nof your best games or anything else to exit the game: '
        )
        print(sep_print())
        if user_input == "y":
            continue
        elif user_input == "s":
            sorted_game_stats_logger(game_scores)
            if (
                input('Type "y" to play again or anything else\nto exit the game: ')
                == "y"
            ):
                print(sep_print())
                continue
            else:
                break
        else:
            break


# main function execution
if __name__ == "__main__":
    main()
