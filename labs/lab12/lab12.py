"""
Name: Jeremy Miller
lab12.py
"""
from random import randint


def main():
    find_and_remove_first([1, 2, 3], 2)
    # is_in_linear(225, read_data('dataSorted.txt'))
    good_input()
    num_digits()
    hi_lo_game()
    pass


def find_and_remove_first(big_list, value):
    try:
        i = big_list.index(value)
        big_list[i] = 'Jeremy'
    except:
        pass


def read_data(filename):
    in_file = open(filename, 'r')
    data = in_file.readline()
    data.split()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if i == search_val:
            return True
        else:
            return False


def good_input():
    x = eval(input('Enter a number between 1 and 10: '))
    while x < 1 or x > 10:
        x = eval(input("Input wasn't in the range. Try again."))
    return x


def num_digits():
    x = eval(input('Enter a positive integer: '))
    while x > 0:
        i = 0
        while x != 0:
            i += 1
            x //= 10
        print('Number of digits = ', i)
        x = eval(input('Enter a positive integer: '))


def hi_lo_game():
    number = randint(1, 100)
    guess = eval(input('Guess a number: '))
    guesses = 0
    while guess != number and guesses < 7:
        if guess > number and guesses != 6:
            guess = eval(input('Number was too high! Try again.'))
        elif guess < number and guesses != 6:
            guess = eval(input('Number was too low! Try again.'))
        guesses += 1
    if guess == number:
        print('You Won!')
    else:
        print('You Lost :(')


main()
