"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Václav Holub
email: vaclavholub5@seznam.cz
discord: .avalok
"""

# imports
from random import randint

# variables
sep = "-" * 47


# functions
def duplicate_detector(number, sequence):
    return True if number in sequence else False


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


# game introduction
print(
    f"""Hi there!
{sep}
I've generated a random 4 digit number for you.
{sep}"""
)
input("Enter a number: ")
