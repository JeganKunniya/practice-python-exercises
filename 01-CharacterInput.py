# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date


def calculate_when_user_turns_100():
    """
    Calculates the year by which the user turns 100 based on his age.

    :return: none.
    """
    user_name = input('Enter your name : ')
    age = int(input('Enter your age : '))  # age is an integer and not a decimal. Hence the typecast

    print('Hello {}, you will be 100 years by {}'.format(user_name, date.today().year + 100 - age))


if __name__ == '__main__':
    calculate_when_user_turns_100()
