"""
Name: Jeremy Miller
hello.py

Problem: This program prints "hello, world!"

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    initial = first_name[0]
    last_seven = last_name[0:7]

    user_name = initial + last_name
    print(user_name)


def get_month(pos):
    index = (pos - 1) * 3
    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    month_abbrev = months[index:index + 3]
    print('Month', pos, 'is ' + month_abbrev)


def get_month_alt(pos):
    end_index = pos * 3
    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    start = end_index - 3


def get_month_list(pos):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_abbrev = months[pos - 1]
    print('Month', pos, 'is ' + month_abbrev)


# main()
# get_month(4)
get_month_list(6)
