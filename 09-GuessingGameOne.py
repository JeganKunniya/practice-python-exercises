# Exercise - 09: Guessing Game One

import random


def guess_the_number():
    """
    Generate a random number between 1 and 9 (including 1 and 9).
    Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
    :return: None
    """
    number_of_guesses = 0
    while True:
        guessed_number = input('Enter the number you guess : ')

        if guessed_number == 'exit':
            break

        number_of_guesses += 1
        guessed_number = int(guessed_number)
        if guessed_number < random_number:
            print('Your guess is too low than the number!')
        elif guessed_number > random_number:
            print('Your guess is too high than the number!')
        else:
            print('Yay! You got the correct number! in {} guesses'.format(number_of_guesses))
            break


if __name__ == '__main__':
    random_number = random.randint(1, 9)
    print('Welcome to the game of number guess. I will randomly pick a number between 1 and 9 that you have to guess')
    print('You can continue to guess until you type the word \'exit\' for guess')
    print('Let\'s play')
    guess_the_number()

