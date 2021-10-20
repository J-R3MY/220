"""
Name: Jeremy Miller
lab 8.py
"""
from encode import encode


def main():
    number_words('walrus.txt', 'new_walrus.txt')
    hourly_wages('hourly_wages.txt', 'new_hourly_wages.txt')
    calc_check_sum('0072946520')
    send_message('message.txt', 'Erin')
    send_safe_message('safe_message.txt', 'Liam', 2)
    send_uncrackable_message('uncrackable_message.txt', 'Dude', 'pad.txt')
    pass


def encode_better(message, key):
    s = message
    k = key
    acc = ''
    for i in range(len(s)):
        c = ord(s[i])
        key = ord(k[i % len(k)]) - 97
        shift = chr(c + key)
        acc = acc + shift
    return acc


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    i = 1
    for line in in_file:
        new_line = line.split()
        for word in new_line:
            out_file.write(str(i) + " " + word + "\n")
            i += 1
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        out_file.write(" ".join(new_line) + "\n")
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    total = 0
    for i in range(len(isbn)):
        num = int(isbn[i]) * (10-i)
        total = total + num
    return total % 11


def send_message(file, friend):
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w')
    for line in in_file:
        out_file.write(line + "\n")
    in_file.close()
    out_file.close()


def send_safe_message(file, friend, key):
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w')

    for line in in_file:
        new_line = encode(line, key)
        out_file.write(new_line + "\n")
    in_file.close()
    out_file.close()


def send_uncrackable_message(file, friend, pad):
    in_file = open(file, 'r')
    out_file = open(friend + ".txt", 'w')
    in_pad_file = open(pad, 'r')

    for line in in_file:
        new_line = encode_better(line, in_pad_file.read())
        out_file.write(new_line + "\n")


main()
