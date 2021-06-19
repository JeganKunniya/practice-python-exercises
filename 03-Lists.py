# Exercise 03 - List Less than 10
number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def list_less_than_5():
    """
    Take a list, say for example this one:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are less than 5
    """
    for i in number_list:
        if i < 5:
            print(i)


def list_less_than_5_as_new_list():
    """
    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list
    in it and print out this new list.
    :return: new list of numbers from number_list that are less than 5
    """
    new_list = []
    for i in number_list:
        if i < 5:
            new_list.append(i)
    return new_list


def list_less_than_5_as_new_list_in_one_line_of_python():
    """
    Write this in one line of Python..
    :return: new list of numbers from number_list that are less than 5
    """
    return [i for i in number_list if i < 5]


def list_less_than_user_input():
    """
    Ask the user for a number and return a list that contains only elements from the original list a that are
    smaller than that number given by the user.
    :return: new list of number from number_list than are less than user input number
    """
    return [i for i in number_list if i < user_input]


if __name__ == '__main__':
    print('Print all the numbers less than 5, one by one')
    list_less_than_5()

    print('Print all the numbers less than 5, as a new list')
    print(list_less_than_5_as_new_list())

    print('Print all the numbers less than 5, as a new list, in a single line of python')
    print(list_less_than_5_as_new_list_in_one_line_of_python())

    user_input = int(input('Enter a number to filter from the number list : '))
    print('Print all the numbers less than {}'.format(user_input))
    print(list_less_than_user_input())
