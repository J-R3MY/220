"""
Name: Jeremy Miller
lab11.py
"""
from random import *


def get_word(words):
    in_file = open(words, 'r')
    lines = []
    for line in in_file:
        lines.append(line.strip())
    return lines


def pick_word(words):
    rand_num = randint(0, len(words))
    return words[rand_num]


def guess_word(secret_word, guessed_letters, guessed_word, turn_count, letter):
    check = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            guessed_word[i] = letter
            check = True
    if check == True:
        return True
    guessed_letters.append(letter)
    return False


def word_spelled(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    else:
        return False


def guess_letter(guessed_letters, turn_count, secret_word, guessed_word):
    letter = input('Guess a letter!')
    check = False
    while check == False:
        check = True
        for ch in guessed_letters:
            if letter == ch:
                print('This letter has already been guessed!')
                letter = input('Guess a letter!')
                check = False
        if len(letter) != 1:
            print('Invalid entry, try again.')
            letter = input('Guess a letter!')
            check = False
    if guess_word(secret_word, guessed_letters, guessed_word, turn_count, letter):
        return True
    else:
        return False


def print_board(guessed_word, turn_count, guessed_letters):
    print("--" + ("-----" * len(guessed_word) + "--"))
    print(guessed_word)
    print("--" + ("-----" * len(guessed_word) + "--"))
    print()
    print('Number of Guesses: ' + str(turn_count))
    print('Guessed letters: ' + str(guessed_letters))
    print()


def play_game():
    words = get_word('list.txt')
    secret_word = pick_word(words)
    guessed_word = ["_"] * len(secret_word)
    guessed_letters = []
    turn_count = 0
    print_board(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not word_spelled(guessed_word, secret_word):
        if guess_letter(guessed_letters, turn_count, secret_word, guessed_word) == False:
            turn_count += 1
        print_board(guessed_word, turn_count, guessed_letters)
    if turn_count == 7:
        print('Game Over! You Lost!')
    else:
        print('Game Over! You Won!')


def main():
    play_game()


main()
