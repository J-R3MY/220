"""
Name: Jeremy Miller
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math


def main():
    print(sphere_area(3))
    print(sphere_volume(2))
    print(sum_n(5))
    print(sum_n_cubes(7))


def sphere_area(radius):
    area = 4 * math.pi * radius**2
    return area


def sphere_volume(radius):
    volume = 4/3 * math.pi * radius**3
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + i**3
    return acc


def cash_conversion():
    integer = eval(input('Enter an integer: '))
    print('${:.2f}'.format(integer))


def encode():
    message = input('Enter your message: ')
    key = eval(input('Enter a number to shift by: '))
    acc = ''
    for c in message:
        x = ord(c)
        shift = x + key
        new_character = chr(shift)
        acc = acc + new_character
    print(acc)


def read_file():
    file = open('input.txt', 'r')
    for line in file.readlines():
        print(line[:-1])
    file.close()


def encode_better():
    s = input('Enter a message: ')
    k = input('Enter a key: ')
    acc = ''

    for i in range(len(s)):
        c = ord(s[i])
        key = ord(k[i % len(k)]) - 97
        shift = chr(c + key)
        acc = acc + shift
    print(acc)


main()
cash_conversion()
encode()
read_file()
encode_better()
