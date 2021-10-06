"""
Name: Jeremy Miller
lab6.py
"""


def name_reverse():
    name = input('Enter a name in first/last order: ')
    split_name = name.split(" ")
    print(split_name[1] + ', ' + split_name[0])


def company_name():
    domain = input('Enter the domain name: ')
    domain_split = domain.split(".")
    print(domain_split[1])


def initials():
    num_names = eval(input('How many names will be inputted?'))
    for i in range(num_names):
        first_name = input('Enter the first name of student ' + str(i+1) + ': ')
        last_name = input('Enter ' + first_name + "'s last name: ")
        print(first_name + "'s initials are " + first_name[0] + last_name[0])


def names():
    n = input("Enter people's names, separated by commas: ")
    split_names = n.split(", ")
    for name in split_names:
        ini = name.split(" ")
        print('The initials are ' + ini[0][0] + ini[1][0])


def thirds():
    num_s = eval(input('How many sentences are you inputting: '))
    for _ in range(num_s):
        sentence = input('Enter the sentence: ')
        print(sentence[2::3])


def word_average():
    x = input('Enter a sentence: ')
    acc = 0
    words = x.split(" ")
    for word in words:
        acc = acc + len(word)
    print(acc / len(words))


def pig_latin():
    sentence = input('Enter a sentence: ').lower()
    words = sentence.split(" ")
    for word in words:
        pig = word[1:] + word[0] + "ay"
        print(pig, end=" ")


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
